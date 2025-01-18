from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/todos', methods=['GET', 'POST'])
def todos():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = 'Listado de todos los TODOS'
        response_body['results'] = todos
        return jsonify(todos)
    if request.method == 'POST':
        data = request.json
        print('Incom.......', data)
        todos.append(data)
        response_body['message'] = 'Todo agregado con éxito'
        response_body['results'] = todos
        return jsonify(todos)


@app.route('/todos/<int:position>', methods=['GET', 'PUT', 'DELETE'])
def todo(position):
    response_body = {}
    print('La posición es: ', position)
    if request.method == 'GET':
        response_body['message'] = f'Datos del todo: {position}'
        response_body['results'] = todos[position]
        pass
    if request.method == 'PUT':
        data = request.json
        todos[position] = data
        response_body['message'] = f'Todo nro: {position} modificado'
        response_body['results'] = todos[position]
        pass
    if request.method == 'DELETE':
        del todos[position]
        response_body['message'] = f'Todo nro: {position} eliminado'
        response_body['results'] = todos
        return jsonify(todos)



todos = [{"label": "my first task", "done": False}]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)