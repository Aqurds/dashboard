from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)
app.config['SECRET_KEY'] = '0f9dc56d2288afa6e10b8d97577fe25b'



# Home route
@app.route('/')
def home():
    return render_template('index.html')



# Frequency route
@app.route('/frequency/')
def frequency():
    return render_template('frequency.html')



# Touchpoint-banks route
@app.route('/touchpoint-banks/')
def touchpoint_banks():
    return render_template('touchpoint-banks.html')



# Customer Journey route
@app.route('/customer-journey/')
def customer_journey():
    return render_template('customer-journey.html')



# Product Category route
@app.route('/product-category/')
def product_category():
    return render_template('product-category.html')



# Promotions route
@app.route('/promotions/')
def promotions():
    return render_template('promotions.html')



# Topics route
@app.route('/topics/')
def topics():
    return render_template('topics.html')



# Mail route
@app.route('/mail/')
def mail():
    return render_template('mail.html')




if __name__ == '__main__':
    app.run(debug = True)
