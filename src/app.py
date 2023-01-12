##siguientes 2 lineas de código permiten crear una nueva app Flask (publica URLs en internet como una api o sitio web):
    ##agregar import request para aplicar método POST.
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

##hacer que servidor retorne string con el 1er endpoint:

@app.route('/todos', methods=['GET'])
def hello_world():
    some_data = todos
    json_text = jsonify(some_data)
    return json_text

##Agregar endpoint con método POST:

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print ("incoming request with the following body", request_body)
    

    ##agregar nueva tarea a la lista:
    todos.append(request_body)

    return jsonify(todos)

##Creación de una variable global (todos):
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": False },
    { "label": "My fourth task", "done": False },
    { "label": "My fifth task", "done": False }
]

##Eliminar de todolist según posición con método DELETE:
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    del todos[position]
    
    ##retornar el jsonify de la lista de todos actualizado:
    return jsonify(todos)

##siguientes 2 líneas siempre deben estar al final del archivo app.py:

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)