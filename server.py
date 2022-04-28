from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/calc', methods=['POST'])
def hello_world():
    data = request.get_json()
    dict = {}
    for student_data in data:
        dict[student_data["first name"] + " " + student_data["last name"]] =  sum(student_data["scores"])
    
    return jsonify(dict)



if __name__ == '__main__':
   app.run()