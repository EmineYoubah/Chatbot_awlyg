from flask import Flask, render_template, request, jsonify
import explo_model
from explo_model import chatbot_response
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

i=0
classe=''
@app.route("/get", methods=["GET", "POST"])

def chat():
    global i
    msg = request.form["msg"]
    input , classe  =chatbot_response(msg)
    print(classe)

    return [input , classe]

@app.route("/cla", methods=["GET", "POST"])

def cla( classs):


    return str(classs)





if __name__ == '__main__':
    app.run(debug = True,port=5001)
