class Error:
    @staticmethod
    def is_Error():
        while True:
            x = input()
            if x != "yes" and x != "no":
                print("Need be yes or no ")
            else:
                return x

    @staticmethod
    def Error_bet(have_Chip):
        while True:
            try:
                x = int(input())
            except:
                print("need to be int ")
            else:
                if x > have_Chip:
                    print("Sorry, You do not have enough Chips , you have {} ".
                          format(have_Chip))
                elif x <= 0:
                    print("num need to be > 0")
                else:
                    return x
            finally:
                print("")