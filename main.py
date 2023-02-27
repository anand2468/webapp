from flask import Flask, render_template,request, redirect
import os
from fileinput import filename

app = Flask(__name__)

@app.route('/')
def hello():
    files = os.listdir()
    return render_template("index.html", files = files)

@app.route('/upload', methods=["POST"])
def upload():
    f = request.files['file']
    print(f, f.filename)
    try:
        f.save("files/{}".format(f.filename))
        return f"<h1> uploaded</h1> <a href='/'>go back </a>{f}"
    except:
        return redirect('/')
    

@app.route('/fileviewer', defaults={'folder': 'home'})
@app.route('/fileviewer/<folder>')
def viewer(folder):
    if folder == 'home':
        files=os.listdir()
    else:
        files=os.listdir(folder)
    return render_template('fileviewer.html',files=files)

if __name__ == '__main__':
    app.run(debug=True)
    #, port=80, host='0.0.0.0'