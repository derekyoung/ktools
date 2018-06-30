
from glob import glob
import os
import datetime
import zipfile

cdg_files = glob('*.cdg')

for file in cdg_files:
    date = datetime.datetime.fromtimestamp(os.path.getctime(file))
    fn = str(file).replace('.cdg','')

    print('creating archive ' + fn)
    with zipfile.ZipFile(fn + '.zip', mode='w') as zf:
        zf.write(fn + '.mp3',compress_type=zipfile.ZIP_DEFLATED)
        zf.write(fn + '.cdg',compress_type=zipfile.ZIP_DEFLATED)

    # reset creation and modification time
    os.system('SetFile -d "{}" "{}"'.format(date.strftime('%m/%d/%Y %H:%M:%S'), fn + '.zip'))
    os.system('SetFile -m "{}" "{}"'.format(date.strftime('%m/%d/%Y %H:%M:%S'), fn + '.zip'))


