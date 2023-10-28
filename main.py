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

@app.route('/demo', defaults={'wd': os.getcwd()+'/files'})
@app.route('/demo/<wd>')
def demo(wd):
    files,folders = list(), list()
    print(wd)
    for dirpath, dirnames, filenames in os.walk(wd):
        folders.append(dirnames)
        files.append(filenames)
    return render_template('fileviewer.html',files=files,folders = folders)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8888)
    #, port=80, host='0.0.0.0'
