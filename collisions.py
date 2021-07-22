def collide(object_1, object_2) -> bool:

    offset_x = object_2.position[0] - object_1.position[0]
    offset_y = object_2.position[1] - object_1.position[1]

    if object_1.mask.overlap(object_2.mask, (int(offset_x), int(offset_y))):
        return True

    return False

