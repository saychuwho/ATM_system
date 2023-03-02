from bank_members import *

'''
# testing bank_members
# testing Account
testacc = Account("000-000-000000", "test", 10000, "test", "0000")
print(testacc.account_Balance())
print(testacc.account_Bank())
print(testacc.account_Password())
print(testacc.account_Num())
testacc.account_Deposit(1000)
print(testacc.account_Balance())
testacc.account_Withdrawal(1000)
print(testacc.account_Balance())
print("\n")

# testing Card
testCard = Card("000-000-000000", "test", False)
print(testCard.account_Num())
print(testCard.bank_Name())
print(testCard.is_Admin())
print("\n")

# testing Bank
testBank = Bank("Test")
testBank2 = Bank("Test2")
testBank.add_Bank(testBank2)
testBank2.add_Bank(testBank)
print(testBank.bank_Name())
testCard2 = testBank.create_Account("111-111-111111", "test2", 20000, "0000")
testCard3 = testBank.create_Account("222-222-222222", "test3", 30000, "0000")
print(testCard2.account_Num())
print(testCard2.bank_Name())
print(testCard2.is_Admin())
testAdmin = testBank.create_Admin()
print(testAdmin.account_Num())
print(testAdmin.bank_Name())
print(testAdmin.is_Admin())
print(testBank.user_Authorize(testacc, "0000"))
print(testBank.user_Authorize(testacc, "1000"))
searched_acc = testBank.search_myAccount("111-111-111111")
searched_acc2 = testBank.search_myAccount("000-000-000000")
searched_acc3 = testBank.search_anotherAccount("222-222-222222")
searched_acc.account_Balance()
searched_acc2.account_Num()
searched_acc3.account_Num()
testBank.print_account_RemainBalance()
'''

