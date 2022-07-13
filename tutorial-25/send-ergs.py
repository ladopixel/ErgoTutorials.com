from ergpy import helper_functions, appkit

node_url: str = 'http://159.65.11.55:9053/'
ergo = appkit.ErgoAppKit(node_url=node_url)

wallet_mnemonic = 'your'
receiver_addresses = ['9g3icrZWNuMCEDZKTkzDh79zhtFr3AbBrKXHAVfC5Kdxx6sjPQh']
amount = [0.1]

print(helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic, receiver_addresses=receiver_addresses))