import csv,os
from typing import List,Set,Dict
def is_open_or_close(transaction:Dict[str,str])->bool:
    label=transaction['label']
    if 'Open channel' in label:
        return True
    if 'Close channel' in label:
        return True
    return False
def generate_fieldnames(mydict:Dict[str,str])->Set[str]:
    return_fields=set()
    for row in mydict:
        for key in row.keys():
            return_fields.add(key)
    return return_fields
def is_ln_transaction(transaction:Dict[str,str])->bool:
    if transaction['ln_payment_hash']!='':
        return True
    return False
if __name__=='__main__':
    for file in os.listdir():
        if not file.lower().endswith('.csv'):
            continue
        output_list=[]
        input_dict = csv.DictReader(open(file))
        for row in input_dict:
            # skip opens/closes
            if is_open_or_close(row):
                print('Found LN channel open/close tx, skipping')
                continue
            # don't modify non-LN transactions
            if not is_ln_transaction(row):
                output_list.append(row)
                continue
            else:
                row['amount_chain_bc']=row['amount_lightning_bc']
                output_list.append(row)
                print(f'found ln transaction: {row}')
        fieldnames=list(generate_fieldnames(output_list))
        with open(f'{file}_output.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_list)
    print("""
    Did this software save you an hour or more of your time? Consider a BTC donation Thank you :).
    
    ⛓️ On-chain: bc1qunr36gpgkhlpezry88qjwl7p5jzljp23thety3
    
    ⚡ Lightning: cascadiarecovery@strike.me""")


