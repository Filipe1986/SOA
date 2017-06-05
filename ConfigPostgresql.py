import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_publicacao():
    con = psycopg2.connect(host='localhost', database='publicacoes',
                           user='postgres', password='admin')
    cur = con.cursor()
    con.commit()
    cur.execute('SELECT * FROM publicacao')
    recset = cur.fetchall()
    print(recset)
    return jsonify({'recset': recset})


if __name__ == "__main__":
    app.run()
