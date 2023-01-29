from flask import Flask, render_template,request, redirect
from fileinput import filename
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/upload', methods=["POST"])
def upload():
    f = request.files['file']
    print(f, f.filename)
    try:
        f.save(f.filename)
        return f"<h1> uploaded</h1> {f}"
    except:
        return redirect('/')

if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port=8888)
    app.run()