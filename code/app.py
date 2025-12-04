from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Create Flask app instance.
# static_folder='.' allows serving static files (like index.html) from the current directory.
app = Flask(__name__, static_folder='.')

# Enable CORS so that a front-end (e.g., a webpage hosted somewhere else)
# can send requests to this backend without being blocked by the browser.
CORS(app)

# Import the crash analysis function from your local module.
from crash_analyzer import analyze_crash

# Serve the main webpage (index.html) when the root URL is accessed.
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Endpoint that accepts a crash log file and returns the analysis.
@app.route('/analyze', methods=['POST'])
def analyze():
    # Retrieve uploaded file (form field name: 'file')
    f = request.files.get('file')
    if not f:
        # Client failed to upload a file
        return jsonify({'error': 'no file uploaded'}), 400

    # Read raw file bytes
    raw = f.read()

    # Try decoding the file as UTF-8 first
    try:
        text = raw.decode('utf-8')
    except Exception:
        # If UTF-8 fails, fall back to Latin-1 and ignore invalid bytes
        text = raw.decode('latin-1', errors='ignore')

    try:
        # Run your custom crash analyzer
        result = analyze_crash(text)

        # Return the structured analysis as JSON
        return jsonify({'analysis': result})
    except Exception as e:
        # Print the full traceback to the server logs for debugging
        import traceback
        traceback.print_exc()

        # Return error message to client
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    # Start Flask dev server
    # host='0.0.0.0' makes it accessible externally (e.g., on a VPS or local network)
    # debug=False because debug mode shows too much internal info if errors occur
    app.run(host='0.0.0.0', port=5001, debug=False)
