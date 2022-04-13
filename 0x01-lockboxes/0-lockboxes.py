#!/usr/bin/python3

def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened"""

    if not isinstance(boxes, list):
        return False
    elif boxes == 0:
        return False
    elif len(boxes) == 0:
        return False
    checker = [0]
    list_ing = [i for i in range(len(boxes))]

    for in_check in checker:
        for in_boxes in boxes[in_check]:
            if in_boxes not in checker and in_boxes in list_ing:
                if in_boxes >= len(boxes):
                    return False
                checker.append(in_boxes)

    if len(checker) == len(boxes):
        return True
    else:
        return False
