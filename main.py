# import fun_dgcm
import sys
from bs4 import BeautifulSoup


def main():

    lenght_of_args = len(sys.argv)
    # print(lenght_of_args)
    try:
        if lenght_of_args == 1:
            fun_dgcm.ALL()

        elif lenght_of_args != 1:
            if sys.argv[1] == '1':
                fun_dgcm.ONE()
            elif sys.argv[1] == '2':
                fun_dgcm.TWO()
            elif sys.argv[1] == '3':
                fun_dgcm.THREE()
            elif sys.argv[1] == '4':
                fun_dgcm.FOUR()
    except:
        print(
            f'Command line argument {sys.argv[1]} is not valid or is incorrectly written.')


if __name__ == "__main__":
    main()
