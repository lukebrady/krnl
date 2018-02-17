from flask import Flask


class KernelServer:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            index = open('web/html/index.html', 'r').read(None)
            return index
