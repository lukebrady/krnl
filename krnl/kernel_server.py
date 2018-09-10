import redis, json
from flask import Flask


class KernelServer:
    def __init__(self):
        self.app = Flask(__name__)
        config_file = open('./config/storage_config.json', 'r+').read()
        json_config = json.loads(config_file)
        self.cache_client = redis.StrictRedis(host=json_config.get('redis_server').get('host'),
                                         port=json_config.get('redis_server').get('port'),
                                         db=json_config.get('redis_server').get('database'),
                                         decode_responses=True,
                                         encoding='UTF-8')


        @self.app.route('/')
        def index():
            all = self.cache_client.lrange('_all', 0, -1)
            sorted_all = sorted(all)
            index = '<h3>Installed Kernels</h3>'
            for kernel in sorted_all:
                index += '<h4>{}</h4>'.format(kernel)
            # index = open('web/html/index.html', 'r').read(None)
            return index

        # This route will be used to perform a system-wide health check and return
        # the status depending on system performance.
        @self.app.route('/health')
        def health():
            status = '<p>Krnl Status</p><p style = "background-color : green; color: white">Kernels: Healthy</p>'
            return status
