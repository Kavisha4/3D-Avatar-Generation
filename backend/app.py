import os
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate_avatar', methods=['POST'])
def generate_avatar():
    # Implement your code to process the image and generate a 3D avatar here.
    # Replace the following code with your actual implementation.
    # For demonstration purposes, it saves a sample image.
    
    sample_image = request.files['image']
    if sample_image:
        sample_image.save('generated_avatar.obj')
        return send_file('generated_avatar.obj', as_attachment=True)
    else:
        return "Error generating avatar", 500

if __name__ == '__main__':
    app.run(debug=True)
