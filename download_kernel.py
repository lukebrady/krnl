# DownloadKernel is used to download the kernel that is
# requested to be installed. This is downloaded by default from kernel.org.
# A separate blob storage can be configured in ./storage_config.json.

import json, os, redis, logging, hashlib, sys

from subprocess import run as run


def check_filesystem_for_kernel(version):
    if os.path.exists('./kernels/linux-' + version + '.tar.xz'):
        return True
    else:
        return False


def make_immutable(version):
    run(['chattr', '+i', './kernels/linux-' + version + 'tar.xz'])


def get_kernel_hash(version):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    kernel = './kernels/linux-' + version + '.tar.xz'
    sha256 = hashlib.sha256()
    if os.path.exists(kernel):
        with open(kernel, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    else:
        print('Kernel cannot be hashed.')


def download_kernel(version):
    config_file = open('./config/storage_config.json', 'r+').read()
    json_config = json.loads(config_file)
    kernel_hash = ''
    cache_client = redis.StrictRedis(host=json_config.get('redis_server').get('host'),
                                     port=json_config.get('redis_server').get('port'),
                                     db=json_config.get('redis_server').get('database'),
                                     decode_responses=True,
                                     encoding='UTF-8')
    kernel_url = json_config.get('kernel_storage') + 'linux-{}.tar.xz'.format(version)
    if not check_filesystem_for_kernel(version):
        download = run(['curl', '-XGET', kernel_url, '-o', './kernels/linux-' + version + '.tar.xz'])
        kernel_hash = get_kernel_hash(version)
        if download.returncode != 0:
            logging.error('There was an error downloading the kernel.')
            exit(code=1)
            # else:
            #      # References the make_immutable function defined above. This makes the kernel that was downloaded immutable
            #       # on the filesystem. The only way to gracefully remove a kernel is to use ./krnl rm VERSION.
            #       make_immutable(version)
    else:
        print('Kernel version has already been downloaded.')
    if cache_client.get('current_kernel') != version:
        cache_client.set('current_kernel', version)
    else:
        print(cache_client.get('current_kernel'))
        print(kernel_hash)

    kernel_obj = {'version': version, 'hash': kernel_hash}
    # Add the new kernel to Redis so that you can query this later.
    cache_client.lrange('_all', 0, -1)
    cache_client.lpush('_all', kernel_obj)
    exit(code=0)


def decompress_kernel(version):
    run(['tar', 'xf', './kernels/linux-' + version + '.tar.xz'])


if __name__ == '__main__':
    # download_kernel('4.9.68')
    download_kernel('4.9.68')
