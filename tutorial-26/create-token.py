from ergpy import helper_functions, appkit

node_url: str = 'http://159.65.11.55:9053/'
ergo = appkit.ErgoAppKit(node_url=node_url)

wallet_mnemonic = 'Your'

token_name = input('Enter name: ')
token_description = input('Enter description: ')
token_amount = int(input('Enter amount: '))
token_decimals = int(input('Enter decimals: '))

print(helper_functions.create_token(ergo=ergo, token_name=token_name, description=token_description, token_amount=token_amount, token_decimals=token_decimals, wallet_mnemonic=wallet_mnemonic))