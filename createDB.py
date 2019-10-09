import sqlite3, os, hashlib, sys

DB_FILENAME = 'goodbadfiles.db'

# check for db presence
if os.path.exists(DB_FILENAME) != True:
    print '[-] Cannot find DB file %s' % DB_FILENAME
    sys.exit(-1)

conn = sqlite3.connect(DB_FILENAME)

goodfolder = os.path.join('Files', 'Good')
badfolder = os.path.join('Files', 'Bad')

# get good files
for filename in os.listdir(goodfolder):
    f = open(os.path.join(goodfolder, filename)).read()
	# make the hashing method to sha256, md5 is not collision resistant anymore!
    sha256 = hashlib.sha256(f).hexdigest()
    conn.execute('INSERT INTO files VALUES (?, ?, ?);', (filename, 'Good', sha256))
    print filename + " with hash of "+ sha256 + "is inserted as good file"
# get bad files

for filename in os.listdir(badfolder):
    f = open(os.path.join(badfolder, filename)).read()
	# make the hashing method to sha256, md5 is not collision resistant anymore!
    sha256 = hashlib.sha256(f).hexdigest()
    conn.execute('INSERT INTO files VALUES (?, ?, ?);', (filename, 'Bad', sha256))
    print filename + " with hash of "+ sha256 + "is inserted as bad file"

conn.commit()
