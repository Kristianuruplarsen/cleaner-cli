import glob
import os
import optparse
from os.path import join, isfile


def list_files(filetype):
    """ List files of a particular type in the specified folder.
    folder - a folder path to work in
    filetype - extension of the filetype you want to glob
    """
    return glob.glob('*.{t}'.format(t = filetype))

# folder, ft = 'pdf,txt'
def clean():
    """ move all files with filetype ft to a subfolder named as ft
    """
    folder = os.getcwd()
    # parser for cli options
    p = optparse.OptionParser()
    p.add_option('--filetypes', '-f', default = 'pdf')
    options, arguments = p.parse_args()

    #    if not os.path.exists(folder):
    #        raise ValueError('Folder does not exist.')
    filetypes = options.filetypes.split(',')

    for ft in filetypes:
        files = list_files(ft)
        if len(files)>0:
            # if there isn't already a folder named `ft`, make one
            if not os.path.exists(join(folder, ft)):
                os.mkdir(join(folder, ft))
            # move each file from folder to folder/`ft`
            for f in files:
                filename = os.path.basename(f)
                if not os.path.exists(join(folder, ft, filename)):
                    os.rename(f, join(folder, ft, filename))
                else:
                    # if a file already existed, should it be replaced?
                    user_response = input('File {f} already exists in folder. Overwrite? [Y/n]'.format(f = filename))
                    if user_response == 'Y':
                        os.remove(join(folder, ft, filename))
                        os.rename(f, join(folder, ft, filename))
                    else:
                        pass
