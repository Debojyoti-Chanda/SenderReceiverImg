from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory to store received screenshots
UPLOAD_FOLDER = "screenshots"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"message": f"File {file.filename} uploaded successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7500)
