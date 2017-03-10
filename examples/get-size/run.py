from os.path import getsize
from sys import argv


image_path = argv[1]
print('file_size = %s' % getsize(image_path))
