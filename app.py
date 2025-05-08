from flask import Flask, render_template, request, send_file
import librosa
import numpy as np
from midiutil import MIDIFile
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return {'error': 'Aucun fichier n\'a été envoyé'}, 400
    
    file = request.files['file']
    if file.filename == '':
        return {'error': 'Aucun fichier sélectionné'}, 400
    
    if not file.filename.endswith('.mp3'):
        return {'error': 'Le fichier doit être au format MP3'}, 400
    
    try:
        # Sauvegarder le fichier temporairement
        temp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        file.save(temp_mp3.name)
        
        # Charger l'audio avec librosa
        audio, sr = librosa.load(temp_mp3.name)
        
        # Extraire les caractéristiques audio
        pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
        
        # Créer le fichier MIDI
        midi_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mid')
        midi = MIDIFile(1)  # Un seul track
        midi.addTempo(0, 0, 120)  # Track 0, temps 0, tempo 120 BPM
        
        # Convertir les hauteurs en notes MIDI
        for time_idx in range(pitches.shape[1]):
            pitch_idx = magnitudes[:, time_idx].argmax()
            pitch = pitches[pitch_idx, time_idx]
            
            if pitch > 0:  # Si une note est détectée
                # Convertir la fréquence en note MIDI
                midi_note = int(round(69 + 12 * np.log2(pitch / 440.0)))
                # Limiter les notes à la plage MIDI valide (0-127)
                midi_note = max(0, min(127, midi_note))
                # Calculer le temps en secondes
                time = time_idx * 512/sr
                # Ajouter la note (track 0, channel 0, pitch, time, duration, volume)
                midi.addNote(0, 0, midi_note, time, 0.1, 100)
        
        # Sauvegarder le fichier MIDI
        with open(midi_file.name, 'wb') as f:
            midi.writeFile(f)
        
        # Nettoyer le fichier MP3 temporaire
        os.unlink(temp_mp3.name)
        
        return send_file(
            midi_file.name,
            mimetype='audio/midi',
            as_attachment=True,
            download_name='converted.mid'
        )
        
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 