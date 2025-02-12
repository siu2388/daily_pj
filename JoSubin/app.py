from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/sql')
def index():
    return render_template('index.html')    

@app.route('/command', methods=['POST'])
def command():
    print(request.form.get('first_test'))
    return "TEST" + request.form.get('first_test')

if __name__ == "__name__":
    app.run()