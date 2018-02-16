from flask import Flask


class KernelServer:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return '<h1>This is KRNL</h1>'
