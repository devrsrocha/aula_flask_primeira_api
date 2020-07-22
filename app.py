from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoas(id):
    return {'id':id, 'nome':'Rodrigo', 'profissao':'vagabundo'}

# @app.route('/soma/<int:n1>/<int:n2>')
# def soma(n1, n2):
#     return {'soma':n1+n2}

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return {'soma':total}

if __name__ == "__main__":
    

    app.run()