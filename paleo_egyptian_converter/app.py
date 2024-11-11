from flask import Flask, render_template, request
from conversion_logic import convert_to_egyptian

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    paleo_text = request.form['paleo_text']
    egyptian_text = convert_to_egyptian(paleo_text)
    return render_template('index.html', paleo_text=paleo_text, egyptian_text=egyptian_text)

if __name__ == "__main__":
    app.run(debug=True)
