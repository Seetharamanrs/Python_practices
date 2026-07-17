from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "I am AI/ML engineer"
@app.route("/skills")
def skills():
    return "Python, SQL, Machine Learning"
@app.route("/contact")
def contact():
    return "Email: seetha@gmail.com"

if __name__=="__main__":
    app.run(debug=True)

