from random import choice, randint
from logger import logger


def getList(filename):
    try:
        f = open(filename)
        names = f.read().split("\n")
    except OSError as err:
        logger.error("Error opening file", exc_info=True)
        print("error")
        raise err
    else:
        f.close()
        return names


def getName():
    f_names = getList("assets/first-names.txt")
    m_names = getList("assets/middle-names.txt")
    l_names = getList("assets/last-names.txt")

    #10% chance of full name
    if randint(0,9) == 0:
        name = F"{choice(f_names)} {choice(m_names)} {choice(l_names)}"
    else: 
        name = F"{choice(f_names)} {choice(l_names)}"

    return name