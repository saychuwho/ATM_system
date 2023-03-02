from bank_members import *

# MultiBank, English 만을 지원하는 ATM을 상속 없이 만들어둠.
# 어차피 아두이노에 물려서 사용할거니까 영어만 출력해도 됨.

class Atm:
    getable_cash_num = 50
    getable_check_num = 30
    withdrawal_ammount = 500000
    called_session_num = 0
    max_withdrawal = 3
    # 수수료
    fee_deposit_non_primary = 1000
    fee_deposit_primary = 0
    fee_withdrawal_primary = 1000
    fee_withdrawal_non_primary = 2000
    fee_transfer_primary_primary = 2000
    fee_transfer_primary_non_primary = 3000
    fee_tranfer_non_primary_non_primary = 4000


    def __init__(self, a_serial: str, p_bank: Bank, lf_cash : int):
        self.atm_serial = a_serial
        self.primary_bank = p_bank
        self.left_cash = lf_cash
        self.transac_history = ""
        

    def Deposit(a: Account):
        pass


    def Withdrawal(a: Account):
        pass


    def Transfer(a1: Account, a2: Account):
        pass


    def user_Authorize(a: Account):
        pass