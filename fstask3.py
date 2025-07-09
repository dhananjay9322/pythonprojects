from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/data', methods=['POST'])
def data():
    json_data = request.get_json()
    name = json_data.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

if _name_ == "_main_":
    app.run(debug=True)