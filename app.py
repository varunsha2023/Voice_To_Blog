from flask import Flask, request, render_template
from utils.audio_processor import process_audio
from utils.blog_generator import generate_blog_post
from utils.seo_optimizer import optimize_content
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['audio']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        transcript = process_audio(filepath)
        blog = generate_blog_post(transcript)
        seo_data = optimize_content(blog)

        return render_template('index.html', blog=blog, seo=seo_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
