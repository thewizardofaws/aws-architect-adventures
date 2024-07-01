from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/podcast')
def podcast():
    return render_template('podcast.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/aws-utah')
def aws_utah():
    return render_template('aws-utah.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)
