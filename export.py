import os
from zipfile import ZipFile

file_spec = (
    ('akarigar', 'Includes/akarigar'),
    ('locations', 'Includes/SPS/img/akarigar'),
    ('AllInOne.simba', 'Scripts/'),
)

out_zip = ZipFile('engine.zip', 'w')


def write_file(file, arcdir):
    out_zip.write(file, os.path.join(arcdir, os.path.basename(file)))


def write_dir(dir, arcdir):
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            write_file(os.path.join(dir, file), arcdir)
        else:
            write_dir(os.path.join(dir, file), os.path.join(arcdir, file))

for name, arcdir in file_spec:
    if os.path.isfile(name):
        write_file(name, arcdir)
    else:
        write_dir(name, arcdir)

out_zip.close()
