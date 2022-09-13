"""
    Tutorial for ErgoTutorials.com | Sending different tokens to various addresses with ergpy

    → pip install ergpy or pip install -U ergpy
    → pip install dotenv

    → Modify the file .env with PASSWORD = 'your wallet_mnemonic'

    → python3 app.py
"""

from ergpy import helper_functions, appkit
from dotenv import dotenv_values

node_url: str = 'http://159.65.11.55:9053/'
ergo = appkit.ErgoAppKit(node_url=node_url)

private = dotenv_values('.env')
wallet_mnemonic = private['PASSWORD']


def send_tokens():
    
    # ↓ ['Wallet 1', 'Wallet 2', 'Wallet 3']
    receiver_addresses = ['9g3icrZWNuMCEDZKTkzDh79zhtFr3AbBrKXHAVfC5Kdxx6sjPQh', '9fiwUpZM5ZVZoj2Xqk54EhNM68N2HUkxvFby8ww17b2fjZ3yLwj', '9hapMiKfiFhDpxBH21rp6GKCAfNwh9BREnn1VMU4P7dAufbaTps']
    

    """ Amount in ERG [
                    0,03 →→→→ wallet 1, 
                    0.04 →→→→ wallet 2, 
                    0.02 →→→→ wallet 3
                        ]
    ↓"""
    amount = [0.03, 0.04, 0.02]


    """ tokens for each wallet = [ 
                            [token_id, token_id, token_id →→→→ wallet1],
                            [token_id →→→→ wallet2],
                            [token_id, token_id, token_id, token_id →→→→ wallet3]
                                ]
    ↓"""
    tokens = [                                                                                                
        ['0cd8c9f416e5b1ca9f986a7f10a84191dfb85941619e49e53c0dc30ebf83324b',    # COMET                     →→→→ wallet1
        '0779ec04f2fae64e87418a1ad917639d4668f78484f45df962b0dec14a2591d2',     # Mi Goreng                 →→→→ wallet1
        '5a34d53ca483924b9a6aa0c771f11888881b516a8d1a9cdc535d063fe26d065e'],    # Lunadog                   →→→→ wallet1

        ['1fbebafa50211eb645410b15565eeecd080ae20ced9e5466e4453f75d9829738'],   # Ergo’s EIP-27 Rollout     →→→→ wallet2

        ['0cd8c9f416e5b1ca9f986a7f10a84191dfb85941619e49e53c0dc30ebf83324b',    # COMET                     →→→→ wallet3 
        '0779ec04f2fae64e87418a1ad917639d4668f78484f45df962b0dec14a2591d2',     # Mi Goreng                 →→→→ wallet3
        '5a34d53ca483924b9a6aa0c771f11888881b516a8d1a9cdc535d063fe26d065e',     # Lunadog                   →→→→ wallet3   
        '1fbebafa50211eb645410b15565eeecd080ae20ced9e5466e4453f75d9829738']     # Ergo’s EIP-27 Rollout     →→→→ wallet3
    ]


    """ Amount for each tokens [
                            100 COMET                                   →→→→ wallet1
                            100 Mi Goreng                               →→→→ wallet1
                            0.000001 Lunadog                            →→→→ wallet1 (The decimals of the token (8 decimals) must be taken into account)

                            100 COErgo’s EIP-27 RolloutET               →→→→ wallet2

                            100 COMET                                   →→→→ wallet3
                            100 Mi Goreng                               →→→→ wallet3
                            0.000001 Lunadog                            →→→→ wallet3 (The decimals of the token (8 decimals) must be taken into account)
                            100 COErgo’s EIP-27 RolloutET               →→→→ wallet3
                        ]
    ↓"""
    amount_tokens = [
                [100, 100, 100],
                [100],
                [100, 100, 100, 100]
            ]

    tx = helper_functions.send_token(ergo=ergo, amount=amount, receiver_addresses=receiver_addresses, amount_tokens=amount_tokens,tokens=tokens, wallet_mnemonic=wallet_mnemonic)
    print(f'→ {tx}')

input('Pulse enter')
send_tokens()
