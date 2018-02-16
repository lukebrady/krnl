import os

from krnl_redis import redis_client


def remove_kernel(version):
    # Get a krnl_redis client object
    client = redis_client.KrnlRedisClient().get_client()
    kernel_path = './kernels/linux-' + version + '.tar.xz'

    if os.path.exists(kernel_path):
        os.remove(kernel_path)
        obj = client.lrange('_all', 0, -1)
        for x in obj:
            print(x)
        client.lrem('_all', -1, version)
        exit(code=0)
    else:
        print('ERROR: The kernel does not exist')
        print('INFO: Could not remove kernel version ' + version)
        exit(code=1)
