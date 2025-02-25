from flask import Flask, render_template, request
from model import calculate_color_accuracy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', accuracy=None, error=None)

@app.route('/upload', methods=['POST'])
def upload():
    target_image = request.files['target_image']
    input_image = request.files['input_image']
    
    if target_image and input_image:
        # Calculate the accuracy by passing the file-like objects
        accuracy = calculate_color_accuracy(target_image, input_image)
        return render_template('index.html', accuracy=accuracy)

    return render_template('index.html', accuracy=None, error='Please upload both images.')

if __name__ == '__main__':
    app.run(debug=True)
