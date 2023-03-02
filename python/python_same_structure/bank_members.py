class Account:
    def __init__(self, a_num: str, a_user: str, a_balance: int, a_bank: str, a_pw: str):
        self.account_num: str = a_num
        self.account_user: str = a_user
        self.account_balance: int = a_balance
        self.account_bank: str = a_bank
        self.account_password: str = a_pw
        self.account_transaction: str = ""
        self.account_transaction_kor: str = ""
    
    def account_Num(self):
        return self.account_num

    def account_User(self):
        return self.account_user

    def account_Balance(self):
        return self.account_balance
    
    def account_Bank(self):
        return self.account_bank

    def account_Password(self):
        return self.account_password
    
    def account_Deposit(self, d: int):
        self.account_balance += d

    def account_Withdrawal(self, w: int):
        self.account_balance -= w

    def transaction_Add(self, eng: str, kor: str):
        self.account_transaction += eng
        self.account_transaction_kor += kor

    def ret_transac_history(self, is_eng: bool):
        if(is_eng == True):
            return self.account_transaction
        else:
            return self.account_transaction_kor
    

class Card:
    def __init__(self, a_num: str, b_name: str, is_Admin: bool):
        self.account_num: str = a_num
        self.bank_name: str = b_name
        self.is_admin: bool = is_Admin
    
    def is_Admin(self):
        return self.is_admin

    def account_Num(self):
        return self.account_num
    
    def bank_Name(self):
        return self.bank_name


class Bank:
    max_bank_accounts = 10
    max_another_banks = 10
    zeroAccount = Account("zero", "zero", 0, "zero", 0)
    
    def __init__(self, b_name: str):
        self.bank_name: str = b_name
        self.bank_accounts: Account = []
        self.another_banks: Bank = []
    
    def bank_Name(self)-> str:
        return self.bank_name

    def ret_zeroAccount()-> Account:
        return Bank.zeroAccount
    
    def create_Account(self, a_num: str, a_user: str, a_balance: int, a_pw: str)-> Card:
        temp_account = Account(a_num, a_user, a_balance, self.bank_Name(), a_pw)
        self.bank_accounts.append(temp_account)
        return_card = Card(temp_account.account_Num(), temp_account.account_Bank(), False)
        return return_card
    
    def create_Admin(self)-> Card:
        ret_card = Card("admin", self.bank_Name(), True)
        return ret_card

    def add_Bank(self, b):
        self.another_banks.append(b)
    
    def search_myAccount(self, a_num: str)-> Account:
        for i in self.bank_accounts:
            if i.account_Num() == a_num:
                return i
        
        return Bank.zeroAccount

    def search_anotherAccount(self, a_num: str)-> Account:
        for i in self.another_banks:
            temp_account = i.search_myAccount(a_num)
            if temp_account.account_Num() == a_num:
                return temp_account
        
        return Bank.zeroAccount

    def user_Authorize(self, a: Account, pw: str)-> bool:
        if(a.account_Password() == pw):
            return True
        else:
            return False

    def print_account_RemainBalance(self):
        print("[" + self.bank_name + "Account Balance]")
        for i in self.bank_accounts:
            print(i.account_User() + "'s Account ", i.account_Num(), " Balance : " ,i.account_Balance())
    