# DownloadKernel is used to download the kernel that is
# requested to be installed. This is downloaded by default from kernel.org.
# A separate blob storage can be configured in ./storage_config.json.

import json, os, redis, sys

import logging
from subprocess import run as run


def check_filesystem_for_kernel(version):
    if os.path.exists('./kernels/linux-' + version + '.tar.xz'):
        return True
    else:
        return False


def make_immutable(version):
    run(['chattr', '+i', './kernels/linux-' + version + 'tar.xz'])


def download_kernel(version):
    config_file = open('./config/storage_config.json', 'r+').read()
    json_config = json.loads(config_file)
    cache_client = redis.StrictRedis(host=json_config.get('redis_server').get('host'),
                                     port=json_config.get('redis_server').get('port'),
                                     db=json_config.get('redis_server').get('database'),
                                     decode_responses=True,
                                     encoding='UTF-8')
    kernel_url = json_config.get('kernel_storage') + 'linux-{}.tar.xz'.format(version)
    if not check_filesystem_for_kernel(version):
        download = run(['curl', '-XGET', kernel_url, '-o', './kernels/linux-' + version + '.tar.xz'])
        if download.returncode != 0:
            logging.error('There was an error downloading the kernel.')
            exit(code=1)
        #else:
        #      # References the make_immutable function defined above. This makes the kernel that was downloaded immutable
        #       # on the filesystem. The only way to gracefully remove a kernel is to use ./krnl rm VERSION.
        #       make_immutable(version)
    else:
        print('Kernel version has already been downloaded.')
    if cache_client.get('current_kernel') != version:
        cache_client.set('current_kernel', version)
    else:
        print(cache_client.get('current_kernel'))
    # Add the new kernel to Redis so that you can query this later.
    cache_client.lrange('_all', 0, -1)
    cache_client.lpush('_all', version)
    exit(code=0)


def decompress_kernel(version):
    run(['tar', 'xf', './kernels/linux-' + version + '.tar.xz'])


if __name__ == '__main__':
    # download_kernel('4.9.68')
    download_kernel('4.9.68')
