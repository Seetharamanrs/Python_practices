from flask import Flask, jsonify,request

app=Flask(__name__)

employees_data={
    1:{"name":"Alice","department":"AI"},
    2:{"name":"Bob","department":"HR"}
}
@app.route("/employees")
def employees():
    jsonify(employees_data)
@app.route("/employees",methods=["POST"])
def employees_p():
    data=request.get_json()
    if "name" not in data:
        return jsonify({"error":"Name not found"})
    if "department" not in data:
        return jsonify({"error":"department not found"})
    else:
        name=data["name"]
        dept=data["department"]
        last_key=list(employees_data)[-1]
        employees_data[(last_key+1)]={"name":name,"department":dept}
        return jsonify({
            "message":"Employee created sucessfully",
            "name":name,
            "department":dept
        }),201
@app.route("/employee/<int:id>", methods=["PUT"])
def employees(id):
    data=request.get_json()
    if id not in employees_data:
        return jsonify({"error":"Employees not found"}),404
    if "name" not in data:
        return jsonify({"error":"Name not found"})
    if "department" not in data:
        return jsonify({"error":"department not found"})
    else:
        name=data["name"]
        dept=data["deptarment"]
        employees_data[id]={"name":name,"department":dept}
        return jsonify({"message":"Sucessfully changed"}),201
    
        
@app.route("/employee/<int:id>",methods=["DELETE"])
def employees(id):
    data=request.get_json()
    if id not in employees_data:
        return jsonify({"error":"ID not available"}),204
    else:
        del employees_data[id]
        return jsonify({"message": "Employee deleted successfully"})

if __name__=="__main__":
    app.run(debug=True)
