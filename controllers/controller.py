from app import app
from flask import render_template
from models.online_shop import orders

@app.route('/')
def index():
    return "Hello World!"

@app.route('/orders')
def get_orders():
    return render_template('index.html', title="Orders Page", orders=orders)

@app.route('/orders/1')
def show_order():
    return render_template('order.html', title="Customer Order", orders=orders)