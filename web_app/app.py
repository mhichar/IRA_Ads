from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('landing.html', methods = ['GET'])


@app.route('/AFAM/', methods = ['GET'])
def AFAM():
    return render_template('profile.html')








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)