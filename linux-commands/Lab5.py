import shutil, os, zipfile, datetime, time

def backup(source_dir, dest_dir):
    filename_list = os.listdir(source_dir)
    for filename in filename_list:
        curr_dir = "{}/{}".format(source_dir, filename)
        shutil.copy(curr_dir, dest_dir)

# ==============================
# Backup function test
# ==============================
# source_dir = 'source'
# dest_dir = 'dest'
# backup(source_dir, dest_dir)


def archive(source_dir, dest_dir, atype):
    valid_types = ('zip', 'gztar', 'tar', 'bztar', 'xztar')
    if atype in valid_types:
        shutil.make_archive(dest_dir, atype, source_dir)
    else:
        print('Please provide a valid archive type!')

# ==============================
# Archive function test
# ==============================
# source_dir = 'source'
# dest_dir = 'dest'
# atype = 'zip'
# archive(source_dir, dest_dir, atype) 

def display(dirname, threshold):
    myzipfile = zipfile.ZipFile(dirname)
    for file in myzipfile.filelist:
        size = file.file_size // 1024
        if size > threshold:
            print('{}: {}KB'.format(file.filename, size))

# ==============================
# Display function test
# ==============================
# dirname = 'Lab5_zip.zip'
# threshold = 1000
# display(dirname, threshold)

# def recently_modified(dirname):
#     filename_list = os.listdir(dirname)
#     print(datetime.datetime.now())
#     for filename in filename_list:
#         curr_dir = "{}/{}".format(dirname, filename)

#         stamp = time.time() - time.ctime(os.path.getmtime(curr_dir))
#         print('{}: {}'.format(curr_dir, stamp))


# dirname = '.'
# recently_modified(dirname)
