from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)

# Folder containing images
IMAGE_FOLDER = os.path.join(app.static_folder, 'images')

@app.route('/')
def gallery():
    images = [img for img in os.listdir(IMAGE_FOLDER) if img.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template('gallery.html', images=images)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(IMAGE_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('gallery'))  # Refresh the page after deletion

if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug=True)
