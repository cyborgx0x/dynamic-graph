from flask import Flask, render_template
app = Flask(__name__, static_folder="int/dist", template_folder="int")
import random

@app.route("/")
def index():
    return render_template("index.html")
	
def get_hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
    return random.choice(greeting_list)

@app.route("/hello")
def hello():
    return get_hello()

if __name__ == "__main__":
    app.run()
