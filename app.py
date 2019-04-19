from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)
app.config['SECRET_KEY'] = '0f9dc56d2288afa6e10b8d97577fe25b'



# Home route
@app.route('/')
def home():
    return render_template('index.html')



# frequency route
@app.route('/frequency/')
def frequency():
    return render_template('frequency.html')



# touchpoint-banks route
@app.route('/touchpoint-banks/')
def touchpoint_banks():
    return render_template('touchpoint-banks.html')




if __name__ == '__main__':
    app.run(debug = True)
