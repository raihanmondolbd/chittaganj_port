import random


class TestData:
    BASE_URL = 'http://123.200.20.20:5302/'
    NID_NUMBER = '8231771135'
    DOB = '08-23-1995'
    FATHER_NAME = "Md Siddique Haque"
    MOTHER_NAME = "Amena Begum"

    def mobile_number(self):
        MOBILE_NUMBER = "017"

        # Generate random digits for the remaining 8 characters
        for _ in range(8):
            MOBILE_NUMBER += str(random.randint(0, 9))

        return MOBILE_NUMBER

    EMAIL = "anis@gmail.com"
