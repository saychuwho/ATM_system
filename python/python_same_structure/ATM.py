from bank_members import *
from ATM_exception import *
import input_output

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
        

    def Deposit(self, a: Account):
        button = 0
        # how many cash get during Deposit. last index is check.
        input_won = [0, 0, 0, 0, 0]
        total_amount = 0
        while(True):
            input_output.output_display("Select type of money\nSelect a number\n1. Cash | 2. Check | 3. Exit")
            button = int(input())
            if(button == 1):
                pass


    def Withdrawal(self, a: Account):
        pass


    def Transfer(self, a1: Account, a2: Account):
        pass


    def user_Authorize(self, a: Account):
        pass


    def Session_start(self):
        pass