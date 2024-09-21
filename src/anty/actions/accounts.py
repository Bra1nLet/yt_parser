from src.models.accounts import Account, get_good_accounts, get_broken_accounts, AccountList


def add_accounts(accounts: list):
    for account in accounts:
        Account.model_validate(account).create_account()

def delete_broken_accounts():
    accounts = get_broken_accounts()
    for account in accounts:
        account.delete()
