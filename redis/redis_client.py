import json, redis

# The KrnlRedisClient will be used to load the Redis client from the storage config file.
class KrnlRedisClient:
    def __init__(self):
        config_file = open('./config/storage_config.json', 'r+').read()
        json_config = json.loads(config_file)
        self.cache_client = redis.StrictRedis(host=json_config.get('redis_server').get('host'),
                                              port=json_config.get('redis_server').get('port'),
                                              db=json_config.get('redis_server').get('database'),
                                              decode_responses=True,
                                              encoding='UTF-8')
    # get_client will return an active client object that can be used to get and put data
    # into the redis cache container.
    def get_client(self):
        return self.cache_client
