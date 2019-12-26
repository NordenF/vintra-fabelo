# Copyright 2004-2012 Tom Rothamel <pytom@bishoujo.us>
# See LICENSE.txt for license details.
#
# The Ren'Py launcher for Macintosh.

import sys
import os

# Fix platform on older macs.
import platform

def mac_ver(*args, **kwargs):
    return ('10', ('', '', ''), 'RenPy')

platform.mac_ver = mac_ver

def mac_imports():
    """
    This function imports the libraries that are needed by Ren'Py. This is
    so that py2app will pull them in, but they won't pollute this namespace.
    """

    import renpy.bootstrap
    import renpy
    import ast
    import pygame
    import _renpy
    import pysdlsound
    import cPickle
    import pickle
    import EasyDialogs

def mac_find_game():
    """
    Returns a path to the .py or .pyw file that should be run in order to
    play the game.
    """

    # See if we were given a file through drag-and-drop or on the
    # command line.  If so, we can run it.
    if len(sys.argv) > 1:
        rv = sys.argv[1]
        if os.path.exists(rv):
            return rv	

    launcher = os.path.abspath(__file__)
    parts = launcher.split("/")
    
    # Appname is the name of the app, without the .py suffix.
    appname = parts[-4][:-4]
    
    # Look for the directory containing the game.
    basedir = "/".join(parts[:-1] + [ "autorun" ])
    
    if not os.path.isdir(basedir):
        basedir = "/".join(parts[:-4])
        
    # Find all of the python files in that directory.
    pyfiles = [ i for i in os.listdir(basedir) if i.endswith(".py") ]
    
    if len(pyfiles) == 1:
        rv = pyfiles[0]
    elif (appname + ".py") in pyfiles:
        rv = appname + ".py"
    else:
        raise Exception("Could not find a .py file to launch in %r (%r)" % (basedir, pyfiles))
    
    return os.path.join(basedir, rv)


def mac_main():
    global __file__

    launcher = os.path.abspath(__file__)
    contents = "/".join(launcher.split("/")[:-2])
    sys.executable = os.path.join(contents, "MacOS", "python")

    fn = mac_find_game()
    fn = os.path.abspath(fn)

    # Find the directory containing a game.
    dirname = os.path.dirname(fn)

    # Setup the path that files are imported from.
    sys.path.insert(0, dirname)

    # Set sys.argv to the name of the file we will run, followed by 
    # the directory, followed by additional arguments
    sys.argv = [ fn ] + sys.argv[2:]

    # Set up __file__.
    __file__ = fn

    # Init the Mac OS X side of things... probably not necessary,
    # but can't hurt. 
    try:
        import pygame.macosx
        pygame.macosx.init()
    except:
        pass

    try:
        import pygame.macosx
        pygame.macosx.Video_AutoInit()
    except:
        pass

    # __file__ is now set to the main script. When we return, it gets 
    # excecfiled.
    
if __name__ == "__main__":
    mac_main()
    execfile(__file__, globals(), globals())
