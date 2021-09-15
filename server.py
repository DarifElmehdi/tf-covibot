
from flask import Flask, jsonify , request
from flask_cors import CORS
from chatbot import get_response

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/chat/<string:user_input>',methods=['GET'])                                                                                                    
def chat(user_input):                                                                                                                            
    response = get_response(user_input)
    return {'msg' : response} , 200

app.run()