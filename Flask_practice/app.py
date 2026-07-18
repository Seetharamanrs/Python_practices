from flask import Flask, jsonify

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
@app.route("/profile")
def profile():
    return jsonify({ "name": "Seetharaman",
        "age": 24,
        "course": "AI"})   
@app.route("/student/<id>")
def student(id):
    return f"student ID is {id}"
@app.route("/company")
def company():
    return jsonify({"company": "ABC Technologies",
    "location": "Chennai"})
if __name__=="__main__":
    app.run(debug=True)

