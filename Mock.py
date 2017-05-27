from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'titulo': u'Buy groceries',
        'descricao': u'Leite, Queijo, Pizza, Fruta, Tylenol',
        'feito': False
    },
    {
        'id': 2,
        'titulo': u'Learn python',
        'descricao': u'Need to find a good Python tutorial on the web',
        'feito': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if (not request.json) or (not 'titulo') in request.json:
        print(request)
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'titulo': request.json['titulo'],
        'descricao': request.json.get('descricao', ""),
        'feito': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'titulo' in request.json and type(request.json['titulo']) != str:
            abort(400)
    if 'descricao' in request.json and type(request.json['descricao']) is not str:
        abort(400)
    if 'feito' in request.json and type(request.json['feito']) is not bool:
        abort(400)

    task[0]['titulo'] = request.json.get('titulo', task[0]['titulo'])
    task[0]['descricao'] = request.json.get('descricao', task[0]['descricao'])
    task[0]['titulo'] = request.json.get('titulo', task[0]['feito'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
