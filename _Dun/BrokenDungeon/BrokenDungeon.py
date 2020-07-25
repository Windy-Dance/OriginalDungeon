#             Coding : Utf-8              #
#         Created By : Parallel           #
#         Created On : 2020/7/19 11:43    #
#           Language : Python             #
#       Last Updated : 2020/7/19 11:43    #
#       Last Viewer  : Windy(Admin)       #

# ======================================= #

# ____            _              ____
# | __ ) _ __ ___ | | _____ _ __ |  _ \ _   _ _ __   __ _  ___  ___  _ __
# |  _ \| '__/ _ \| |/ / _ \ '_ \| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \
# | |_) | | | (_) |   <  __/ | | | |_| | |_| | | | | (_| |  __/ (_) | | | |
# |____/|_|  \___/|_|\_\___|_| |_|____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
#                                                   |___/

import sys
import wears

open()
class Docker:
    """
    /*
    The docstring for Docker object.
    The Docker object is for ONE OF PLAYER'S SAVE
    Docker is a player wears saver, it supports read player data from Data/*.json
    It save player's helmet, armor, pants, shoes and attacker in this version.
    Docker should be a arg, before use it, you should CAREFUL.
    Pay attention : don't use it to save player's healthy and other thing, it only do save armors this thing.
    This object use __slots__ to save RAM space.
    */
    """
    __slots__ = ["helmet", "armor", "pants", "shoes", "attacker"]

    def __init__(self):
        self.helmet: object = object
        self.armor: object = object
        self.pants: object = object
        self.shoes: object = object
        self.attacker: object = object


class Person:
    """
    The docstring for Person object.
    The Person object is for all the players!
    """

    def __init__(self, docker: object):
        self.NAME: str = 'PersonFather'
        self.LEVEL: int = 1
        self.EXP: int = 0
        self.UP_EXE: int = 5
        self.HELMET: object = docker.helmet()
        self.ARMOR: object = docker.armor()
        self.PANTS: object = docker.pants()
        self.SHOES: object = docker.shoes()
        self.ATTACKER: object = docker.attacker()



