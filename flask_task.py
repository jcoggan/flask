from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'hello {name}'


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=0):
    celsius = float(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"{celsius} celsius = {fahrenheit} fahrenheit"


@app.route('/c')
@app.route('/c/<fahrenheit>')
def convert_fehrenheit_to_celsius(fahrenheit=0):
    fahrenheit = float(fahrenheit)
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"{fahrenheit} fahrenheit = {celsius} celsius"


if __name__ == '__main__':
    app.run()