# 각종 예외처리를 여기서 담당하면 될 듯

class ATM_exception(Exception):
    pass

class Num_exception(ATM_exception):
    pass

class Cin_exception(ATM_exception):
    pass

class Invalid_account(ATM_exception):
    pass

class Invalid_password(ATM_exception):
    pass

class Invalid_account_num(ATM_exception):
    pass

class File_open_fail(ATM_exception):
    pass
