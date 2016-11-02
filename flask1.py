from flask import Flask
from flask.templating import render_template

from db import session
from config import config
from models.figure import Figure
from models.board import Board

app = Flask(__name__)
app.config['DEBUG'] = config['application'].getboolean("debug", False)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/board/<int:id>')
def board(id):
    board = session.query(Board).filter(Board.id == id).one()
    figures = board.figures
    #figures = session.query(Figure).filter(Figure.board_id == id).all()

    def find_figure(i, j):
        try:
            return [f for f in figures if f.row == i and f.col == j][0]
        except IndexError:
            return ""

    board = [[find_figure(i, j) for j in range(8)] for i in range(8)]
    return render_template("board.html", rows=range(8), cols=range(8), board=board)

if __name__ == '__main__':
    app.run()
