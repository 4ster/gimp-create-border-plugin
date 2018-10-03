#!/usr/bin/env python

from gimpfu import *

# # GimpChannelOps
# CHANNEL_OP_ADD = 0
# CHANNEL_OP_SUBTRACT = 1
# CHANNEL_OP_REPLACE = 2
# CHANNEL_OP_INTERSECT = 3

# # Fill types
# FG_IMAGE_FILL = 0
# BG_IMAGE_FILL = 1
# WHITE_IMAGE_FILL = 2
# TRANS_IMAGE_FILL = 3
# NO_IMAGE_FILL = 4

# # Merge types
# EXPAND_AS_NECESSARY = 0
# CLIP_TO_IMAGE = 1
# CLIP_TO_BOTTOM_LAYER = 2
# FLATTEN_IMAGE = 3


def create_border(img, drawable, thickness=10, layer=None, BORDER_COLOR=(255, 255, 255), MERGE_LAYERS=False):
    # check if thikness not too big
    if 2*thickness>min(drawable.width, drawable.height):
        pdb.gimp_message("Thikness is too big for this image: {0}px".format(str(thickness)))
        return

    # start undo transaction
    pdb.gimp_image_undo_group_start(img)

    # crop layer
    pdb.plug_in_autocrop_layer(img, drawable)
    
    # get active layer
    layer = pdb.gimp_image_get_active_layer(img)

    # add alpha channel for layer
    if not layer.has_alpha:
        pdb.gimp_layer_add_alpha(layer)

    # duplicate layer
    box = pdb.gimp_layer_new(
        img, 1, 1, 1, pdb.gimp_item_get_name(layer) + "_bordered", 100, 0)
    pdb.gimp_image_insert_layer(img, box, None, -1)

    # resize copied layer to original image size
    pdb.gimp_layer_resize_to_image_size(box)

    # transform original image to selection and extend it
    pdb.gimp_image_select_item(img, CHANNEL_OP_REPLACE, layer)
    pdb.gimp_selection_grow(img, thickness)
    pdb.gimp_selection_sharpen(img)

    # activate copied layer
    pdb.gimp_image_set_active_layer(img, box)
    
    # save current background value
    prev_background = gimp.get_background()

    # set bacground to border color and fill selection
    gimp.set_background(BORDER_COLOR)
    pdb.gimp_edit_fill(
        pdb.gimp_image_get_active_drawable(img),  BACKGROUND_FILL)

    # restore prev background
    gimp.set_background(prev_background)

    # move box laer under the original image layer
    pdb.gimp_image_lower_item(img, box)

    # merge layer if user select this option
    if MERGE_LAYERS:
        pdb.gimp_image_merge_visible_layers(img, EXPAND_AS_NECESSARY)

    # clear selection
    pdb.gimp_selection_clear(img)

    # end undo transaction
    pdb.gimp_image_undo_group_end(img)

# register plugin params
register(
    "python_fu_create_border",
    "Create Border",
    "Create a border around active layer",
    "4ster",
    "4ster",
    "2018",
    "Create Border...",
    "RGB, RGB*",
    [
        (PF_IMAGE, "img", "Image:", None),
        (PF_DRAWABLE, "drawable", "Drawable:", None),
        (PF_INT, "thickness", "Box Thickness:", 10),
        (PF_LAYER, "layer", "Layer:", None),
        (PF_COLOR,  "BORDER_COLOR", "Border color:", (255, 255, 255)),
        (PF_BOOL, "MERGE_LAYERS", "Merge all layers:", False),
    ],
    [],
    create_border, menu="<Image>/Filters/Decor")

main()
