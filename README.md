# MP3 to MIDI Converter

A web application that allows you to convert MP3 audio files into MIDI files. The application uses Python with Flask for the backend and essentia-tensorflow for audio analysis.

## Features

- Simple and intuitive user interface
- Drag-and-drop file support
- Real-time conversion
- Standard MIDI file generation
- Progress bar to track conversion

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone [REPO_URL]
cd [FOLDER_NAME]
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
.\venv\Scripts\activate  # On Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. To convert an MP3 file:
   - Drag and drop your MP3 file into the designated area
   - Or click the area to select a file
   - Click "Convert to MIDI"
   - The MIDI file will be automatically downloaded

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # User interface
└── README.md          # Documentation
```

## Main Dependencies

- Flask: Web framework
- essentia-tensorflow: Audio analysis
- numpy: Numerical computations
- librosa: Audio processing
- python-midi: MIDI file generation

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