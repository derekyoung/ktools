
from glob import glob
import os

coll = 'CB'

zip_files = glob('*.zip')

for idx, f in enumerate(zip_files):
    # nfn = str(f).replace('_',' ').split(' - ')[1:]
    nfn = str(f).replace('_',' ').split(' - ')
#    print(len(nfn))
    if len(nfn) == 2:
#        print(nfn)
        artist0 = str(nfn[0]).split(' ')[1:]
#        print(len(artist0))
        b = ''
        for a in artist0:
            b = b+a
#        print(b)
        artist0 = b
        # artist0 = artist0[0] + artist0[1]
        # print(artist0)
        title0 = str(nfn[1]).replace('.zip','')
        # print(title0)
    else:
        artist0 = nfn[1]
        title0 = str(nfn[2]).replace('.zip','')
    artist = artist0
    title = title0
    fn = artist + ' - ' + title
    # Attempt to detect transposed artist / title
    if ', ' in title and len(title.split()) == 2:
        artist = title0
        title = artist0
    # Attempt to detect lastname, firstname
    if ', ' in artist:
        name = artist.split(', ')
        if len(str(name).split()) == 2: #its a name
           # print(name[1] + ' ' + name[0] + ' - ' + title)
           fn = name[1] + ' ' + name[0] + ' - ' + title
 
    print(fn + ' [' + coll + ' Karaoke].zip')
#    os.rename(f, fn + ' [' + coll + ' Karaoke].zip')


