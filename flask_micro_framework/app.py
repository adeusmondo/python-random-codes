from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Decorator que define a rota
@app.route('/lista')
def retorna_lista():
    return render_template('lista.html', titulo='Jinja2')


if __name__ == '__main__':
    app.run(debug=True)
