from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", test="test")

# URLから直接パラメータを受け取る方法
@app.route("/<name>", methods=["GET"])
def hello_world(name):
    return render_template("hello.html", name=name, method=request.method)

@app.route("/param", methods=["GET","POST"])
def hello_world_with_parameter():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')

    return render_template("hello.html", name=name, method=request.method)

if __name__ == "__main__":
    app.run(port=8000)