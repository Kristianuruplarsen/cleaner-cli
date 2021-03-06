import glob
import os
import sys
import optparse
from os.path import join, basename, exists, splitext

# def list_files(filetype):
#     """ List files of a particular type in the specified folder.
#     folder - a folder path to work in
#     filetype - extension of the filetype you want to glob
#     """
#     return glob.glob('*.{t}'.format(t = filetype))

def clean():
    """ move all files with filetype ft to a subfolder named as ft
    """
    folder = os.getcwd()
    required = ['filetypes']
    # parser for cli options
    p = optparse.OptionParser()
    p.add_option('--filetypes', '-f',
    help = 'File extentions to clean')
    p.add_option('--exemptions', '-x',
    help = 'File names exempt from cleaning')
    options, arguments = p.parse_args()

    for r in required:
        if options.__dict__[r] is None:
            p.print_help()
            sys.exit()
    #    if not os.path.exists(folder):
    #        raise ValueError('Folder does not exist.')
    filetypes = options.filetypes.split(',')

    continue_answer = input('Continue cleaning files {ft} in folder {f} (Y)'.format(ft = filetypes, f = pwd() ))
    if continue_anwer == 'Y':
        for ft in filetypes:
            files = glob.glob('*.{t}'.format(t = ft))
            if len(files)>0:
                # if there isn't already a folder named `ft`, make one
                if not exists(join(folder, ft)):
                    os.mkdir(join(folder, ft))
                # move each file from folder to folder/`ft`
                for f in files:
                    filename = basename(f)
                    # if the file is not exempt
                    if splitext(basename(filename))[0] not in options.exemptions.split(','):
                        if not exists(join(folder, ft, filename)):
                            os.rename(f, join(folder, ft, filename))
                        else:
                            # if a file already existed, should it be replaced?
                            user_response = input('File {f} already exists in folder. Overwrite? [Y/n]'.format(f = filename))
                            if user_response == 'Y':
                                os.remove(join(folder, ft, filename))
                                os.rename(f, join(folder, ft, filename))
                            else:
                                pass
                    else:
                        pass
        print("Files of types {fts} have been organized in folders.".format(fts = options.filetypes))
    else:
        print("Clean aborted")
