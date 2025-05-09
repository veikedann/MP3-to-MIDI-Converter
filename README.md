# MP3 to MIDI Converter

A web application that converts MP3 audio files into MIDI files using Python, Flask, and audio processing libraries.

## Features

- Simple and intuitive user interface
- Drag-and-drop file support
- Real-time conversion
- Standard MIDI file generation
- Progress bar to track conversion

## Project Structure

```
.
├── app.py              # Main Flask application
├── wsgi.py            # WSGI entry point for production
├── requirements.txt    # Python dependencies
├── runtime.txt        # Python version specification
├── templates/         # HTML templates
│   └── index.html    # User interface
└── README.md         # Documentation
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## Local Development

1. Clone the repository:
```bash
git clone [REPO_URL]
cd mp3-to-midi-converter
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and go to:
```
http://localhost:5000
```

## Deployment on Railway

1. Fork or clone this repository to your GitHub account

2. Create a new project on Railway:
   - Connect your GitHub repository
   - Railway will automatically detect the Python project

3. Configure the following in Railway:
   - Build Command:
     ```
     pip install --no-cache-dir -r requirements.txt
     ```
   - Start Command:
     ```
     gunicorn wsgi:app --bind 0.0.0.0:$PORT
     ```
   - Environment Variables:
     ```
     PYTHON_VERSION=3.9.18
     PORT=8000
     ```

4. Deploy the application

## Main Dependencies

- Flask: Web framework
- numpy: Numerical computations
- librosa: Audio processing
- midiutil: MIDI file generation
- gunicorn: Production server

## Limitations

- The conversion is optimized for music files with clearly defined notes
- Very complex files may yield less accurate results
- The maximum file size is limited by the Flask configuration

## Contribution

Contributions are welcome! Feel free to:
1. Fork the project
2. Create a branch for your feature
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is under the MIT license. See the `LICENSE` file for more details.

## Support

If you encounter any issues or have questions, feel free to open an issue on the GitHub repository. 