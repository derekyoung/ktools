
from glob import glob
import os
import datetime
import zipfile

cdg_files = glob('*.cdg')

for file in cdg_files:
    date = datetime.datetime.fromtimestamp(os.path.getctime(file))
    fn = str(file).replace('.cdg','')

    if not(os.path.isfile(fn + '.zip')):
        print('creating archive')
        with zipfile.ZipFile(fn + '.zip', mode='w') as zf:
            if os.path.isfile(fn + '.mp3'):
                zf.write(fn + '.mp3',compress_type=zipfile.ZIP_DEFLATED)
                zf.write(fn + '.cdg',compress_type=zipfile.ZIP_DEFLATED)
# we only like mp3s
#            elif os.path.isfile(fn + '.mp2'):
#                zf.write(fn + '.mp2',compress_type=zipfile.ZIP_DEFLATED)
        print(fn)

    # reset creation and modification time
    os.system('SetFile -d "{}" "{}"'.format(date.strftime('%m/%d/%Y %H:%M:%S'), fn + '.zip'))
    os.system('SetFile -m "{}" "{}"'.format(date.strftime('%m/%d/%Y %H:%M:%S'), fn + '.zip'))


