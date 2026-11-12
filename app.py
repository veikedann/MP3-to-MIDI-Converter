from flask import Flask, render_template, request, send_file
import io
import librosa
import numpy as np
from midiutil import MIDIFile
import os
import tempfile

app = Flask(__name__)


def is_mp3_file(filename):
    return isinstance(filename, str) and filename.lower().endswith('.mp3')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get('file')
    if file is None:
        return {'error': 'No file uploaded'}, 400

    if file.filename == '':
        return {'error': 'No file selected'}, 400

    if not is_mp3_file(file.filename):
        return {'error': 'File must be in MP3 format'}, 400

    temp_mp3_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_mp3:
            file.save(temp_mp3.name)
            temp_mp3_path = temp_mp3.name

        audio, sr = librosa.load(temp_mp3_path)
        pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)

        midi = MIDIFile(1)
        midi.addTempo(0, 0, 120)

        for time_idx in range(pitches.shape[1]):
            pitch_idx = magnitudes[:, time_idx].argmax()
            pitch = pitches[pitch_idx, time_idx]

            if pitch > 0:
                midi_note = int(round(69 + 12 * np.log2(pitch / 440.0)))
                midi_note = max(0, min(127, midi_note))
                time = time_idx * 512 / sr
                midi.addNote(0, 0, midi_note, time, 0.1, 100)

        midi_buffer = io.BytesIO()
        midi.writeFile(midi_buffer)
        midi_buffer.seek(0)

        return send_file(
            io.BytesIO(midi_buffer.getvalue()),
            mimetype='audio/midi',
            as_attachment=True,
            download_name='converted.mid'
        )

    except Exception as e:
        return {'error': str(e)}, 500
    finally:
        if temp_mp3_path and os.path.exists(temp_mp3_path):
            os.unlink(temp_mp3_path)