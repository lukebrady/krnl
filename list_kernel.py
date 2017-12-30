import redis
from configuration import Configuration


def list_kernel():
    json_config = Configuration('storage').GetConfiguration()
    cache_client = redis.StrictRedis(host=json_config.get('redis_server').get('host'),
                                     port=json_config.get('redis_server').get('port'),
                                     db=json_config.get('redis_server').get('database'),
                                     decode_responses=True,
                                     encoding='UTF-8')
    kernel_array = cache_client.lrange('_all', 0, -1)
    kernel_sorted = sorted(kernel_array)
    print('Installed Kernels')
    print('-----------------')
    for k in kernel_sorted:
        print(k)
    exit(code=0)