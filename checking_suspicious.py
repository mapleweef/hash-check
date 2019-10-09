import sqlite3, os, hashlib, sys

DB_FILENAME = os.path.join('goodbadfiles.db')

if os.path.exists(DB_FILENAME) != True:
    print '[-] Cannot find DB file %s' % DB_FILENAME
    sys.exit(-1)

conn = sqlite3.connect(DB_FILENAME)
c = conn.cursor()

suspiciousfolder = os.path.join('Files', 'suspicious files')


for filename in os.listdir(suspiciousfolder):
    # read each file from the folder

    f = open(os.path.join(suspiciousfolder, filename)).read()

    #compute their sha256

    sus_sha256 = hashlib.sha256(f).hexdigest()

    #search in the database if such hash value exists
    #if it exists, select the status of that hash value

    c.execute("SELECT status FROM files WHERE sha256='%s'" % sus_sha256)

    status = c.fetchone()
    try:
        status = ''.join(status)
    except Exception:
        status = "unknown"   
    

    #update the status varialbe based on what you got from DB
    #If the hash didn't exist in DB, the status should be "unknown"            


    print  filename + " is recognized as " + status

    status = None
