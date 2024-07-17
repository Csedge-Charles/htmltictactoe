from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def hello():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('index.html', spot1='1', spot2='2', spot3='3', spot4='4', spot5='5', spot6='6', spot7='7', spot8='8', spot9='9')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)