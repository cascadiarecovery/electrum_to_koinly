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
def calc_time_saved(seconds:int)->str:
    if seconds<60:
        return f"{seconds:.2f} seconds"
    minutes=seconds/60
    hours=minutes/60
    days=hours/24
    if days>=1:
        return f"{days:.2f} days"
    if hours>=1:
        return f"{hours:.2f} hours"
    if minutes>=1:
        return f"{minutes:.2f} minutes"


if __name__=='__main__':
    seconds_saved=0
    seconds_save_increment=20
    total_transactions=0
    modified_transactions=0
    for file in os.listdir():
        if not file.lower().endswith('.csv'):
            continue
        output_list=[]
        input_dict = csv.DictReader(open(file))
        for row in input_dict:
            total_transactions += 1
            # skip opens/closes
            if is_open_or_close(row):
                print('Found LN channel open/close tx, setting to zero BTC impact, keeping fee')
                row['amount_chain_bc']=0
                row['amount_lightning_bc'] = 0
                row['fiat_value'] = 0
                row['label']=row['label']+' modified by electrum2koinly'
                output_list.append(row)
                seconds_saved+=seconds_save_increment
                modified_transactions += 1
                continue
            # don't modify non-LN transactions
            if not is_ln_transaction(row):
                output_list.append(row)
                continue
            else:
                row['amount_chain_bc']=row['amount_lightning_bc']
                row['amount_lightning_bc'] = '0'
                row['label'] = row['label'] + ' modified by electrum2koinly'
                seconds_saved += seconds_save_increment
                output_list.append(row)
                print(f'found ln transaction: {row}')
                modified_transactions += 1
        fieldnames=list(generate_fieldnames(output_list))
        with open(f'{file}_output.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_list)
    print("""
    Did this software save you an hour or more of your time? Consider a BTC donation Thank you :).
    
    ⛓️ On-chain: bc1qunr36gpgkhlpezry88qjwl7p5jzljp23thety3
    
    ⚡ Lightning: cascadiarecovery@strike.me""")
    saved_time=calc_time_saved(seconds_saved)
    print(f"If we assume each transaction would have taken {seconds_save_increment} seconds to manually edit, this tool saved you {saved_time} by processing {total_transactions} transactions, {modified_transactions} of which were modified")


