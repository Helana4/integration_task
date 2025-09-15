
from flask import Flask, render_template, redirect
import paymob_checkout   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pay.html")

@app.route("/pay")
def pay():
    try:
    
        checkout_url = paymob_checkout.create_intention()
        return redirect(checkout_url) 
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
