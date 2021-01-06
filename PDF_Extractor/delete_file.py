import os
path = "/mnt/d/OneDrive - Boustead Heavy Industries Corporation Berhad/LCS1 Unlock"
os.chdir(path)
flist = open('/mnt/d/delete_list.txt')
for f in flist:
    fname = f.rstrip() # or depending on situation: f.rstrip('\n')
    # or, if you get rid of os.chdir(path) above,
    # fname = os.path.join(path, f.rstrip())
    if os.path.isfile(fname): # this makes the code more robust
        os.remove(fname)

# also, don't forget to close the text file:
flist.close()