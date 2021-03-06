# Copyright 2004-2012 Tom Rothamel <pytom@bishoujo.us>
# See LICENSE.txt for license details.

# This file defines variables and functions that are obsolete in modern version 
# of Ren'Py. (But there are other functions that are also obsolete.)

init -1900 python:
    # The minimum version of the module we work with. Don't change
    # this unless you know what you're doing.
    config.module_version = 6007001

    # Should we warn the user if the module is missing or has a bad
    # version?
    config.module_warning = False

init -1900 python:
    
    # basics: A map from a string that's displayed by the interface to
    # a translated value of that string.
    config.translations = { }

    # Used internally to maintain compatiblity with old
    # translations of strings.
    config.old_names = { }


    # This function is actually used, but since config.translations and config.old_names
    # are both empty, this should usually just return s.
    def _(s):
        """
        Translates s into another language or something.
        """

        if not config.translations:
            return s

        if s in config.translations:
            return config.translations[s]

        if s in config.old_names and config.old_names[s] in config.translations:
            return config.translations[config.old_names[s]]

        return s

init -1900 python:

    # Should we automatically define images?
    config.automatic_images = None

    # Prefixes to strip from automatic images.
    config.automatic_images_strip = [ ]
    

init 1900 python hide:
    
    def create_automatic_images():
    
        seps = config.automatic_images

        if seps is True:
            seps = [ ' ', '/', '_' ]
            
        for dir, fn in renpy.loader.listdirfiles():

            if fn.startswith("_"):
                continue

            # Only .png and .jpg
            if not fn.lower().endswith(".png") and not fn.lower().endswith(".jpg"):
                continue

            # Strip the extension, replace slashes.
            shortfn = fn[:-4].replace("\\", "/")
            
            # Determine the name.
            name = ( shortfn, )
            for sep in seps:
                name = tuple(j for i in name for j in i.split(sep))

            # Strip name components.
            while name:
                for i in config.automatic_images_strip:
                    if name[0] == i:
                        name = name[1:]
                        break
                else:
                    break
                
            # Only names of 2 components or more.
            if len(name) < 2:
                continue
            
            # Reject if it already exists.
            if name in renpy.display.image.images:
                continue

            renpy.image(name, fn)

    if config.automatic_images:
        create_automatic_images()

init -1900 python:

    # Should the window be shown during transitions?
    _window_during_transitions = False

    def _default_with_callback(trans, paired=None):
        if (_window_during_transitions and not
            renpy.context_nesting_level() and
            not renpy.count_displayables_in_layer('transient')):

            # narrator("", interact=False)
            ui.window(style=style.say_window["empty"])
            ui.null()
            
        return trans

    config.with_callback = _default_with_callback
