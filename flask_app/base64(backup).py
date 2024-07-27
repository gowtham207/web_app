from flask import Flask, jsonify
import base64
import os

app = Flask(__name__)

# Function to convert image to base64
def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

# Function to find all image files in a directory and its subdirectories
def find_images(directory):
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
                image_files.append(os.path.join(root, file))
    return image_files

@app.route('/')
def index():
    images = []
    images_dir = os.path.join("/mnt/efs", 'images')
    
    if not os.path.exists(images_dir):
        return jsonify({"error": "Images directory not found"}), 404
    
    image_files = find_images(images_dir)
    
    for image_path in image_files:
        filename = os.path.relpath(image_path, images_dir)
        encoded_image = encode_image(image_path)
        if encoded_image:
            images.append({"filename": filename, "base64": encoded_image})
        else:
            return jsonify({"error": f"Failed to encode {filename}"}), 500

    return jsonify(images)

@app.route('/image_paths', methods=['GET'])
def image_paths():
    images_dir = os.path.join("/mnt/efs", 'images')
    if not os.path.exists(images_dir):
        return jsonify({"error": "Images directory not found"}), 404
    
    image_files = find_images(images_dir)
    file_paths = [os.path.relpath(image_path, images_dir) for image_path in image_files]
    return jsonify(file_paths)

@app.route('/image_base64/<path:filename>', methods=['GET'])
def image_base64(filename):
    images_dir = os.path.join("/mnt/efs", 'images')
    image_path = os.path.join(images_dir, filename)
    
    if not os.path.exists(images_dir):
        return jsonify({"error": "Images directory not found"}), 404
    
    if os.path.exists(image_path):
        encoded_image = encode_image(image_path)
        if encoded_image:
            return jsonify({"filename": filename, "base64": encoded_image})
        else:
            return jsonify({"error": f"Failed to encode {filename}"}), 500
    else:
        return jsonify({"error": f"File {filename} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
