# Electrum2Koinly
Problem:
- Koinly marks lightning channel opens/closes as sends/receives (you are being TRIPLE-TAXED on these!)
- Koinly ignores all lightning transactions when importing Electrum data from CSV since they have "zero" BTC balance change. This means these are not reported as they should be
- If you use auto-sync/import, Koinly only sees on-chain transactions

Solution (short-term):
- This script takes your original CSV export and makes a new one without the lightning channel opens/closes. It marks lightning transactions as on-chain transactions so they are included as normal.
- 100% open source, lightweight and fast, look at the code yourself it's very small!
- 100% local only & private, your data is never sent anywhere

🚨 Note: The IRS has not issued guidance (as of Jan 1, 2026) as to how lightning channels are taxes for the purposes of gains/losses. This script is assuming that channel opens/closes are equivalent to transfers between your own wallets and that LN transactions are equivalent to normal on-chain sends/receives. Please consult a tax professional for advice.

Solution (long-term):

😤 Tired of discriminatory tax treatment of BTC? You don't have to do this gains tracking nonsense with other international currencies. [Satoshi Action](https://www.satoshiaction.io/) makes it easy to contact your legislators to lobby for pro-BTC legislation. Consider donating 10% of your tax prep costs to them. Let's put an END to this gains-tracking nonsense!

This python script will help you convert your exported transactions from Zeus (CSV) into the format Koinly needs. Python 3 is required to run this. It will run on Windows, Linux, and OS X. 

# How to use:
1. Delete any existing electrum imports in Koinly
2. In your electrum wallet, go to History -> Configure icon -> Export, save your CSV file
3. Place your CSV file in the same directory as this python script (or exe file)
4. Run the python script
5. Your new CSV is created, import it to Koinly
7. Make a donation if this script has been useful (see below for more information)


<h3>Windows</h3>

EXE file (easiest)
- Download [electrum_to_koinly.exe](electrum_to_koinly.exe)

Run as Python:
 - Download the latest version of python from python.org. Enable the "install to system path" option while installing.
 - Double-click main.py or in powershell, run `python C:\users\username\Downloads\electrum_to_koinly\main.py` or wherever you saved the tool. Powershell method is best as it will display any errors.

<h3>Linux</h3>

 - In terminal go to the folder you downloaded this tool into using `cd '/home/user/Downloads/electrum_to_koinly'` or wherever you put it
 - Run `python3 main.py` in the terminal

<h3>OS X</h3>

 - In terminal go to the folder you downloaded this tool into using `cd '/home/user/Downloads/electrum_to_koinly'` or wherever you put it
 - Run `python3 main.py`

# How to import Electrum wallet to Koinly with Bitcoin lightning support

To import your Electrum wallet data to Koinly with Bitcoin lightning support, this script will work!

# Donation
![btcbalance badge](https://img.shields.io/badge/dynamic/json?url=https://explorer.viawallet.com/res/btc/addresses/bc1qunr36gpgkhlpezry88qjwl7p5jzljp23thety3&query=$.data.balance&suffix=BTC&logo=bitcoin&label=Donated)

Did this software save you an hour or more of your time? Consider a BTC donation Thank you :).

⛓️ On-chain: bc1qunr36gpgkhlpezry88qjwl7p5jzljp23thety3

⚡ Lightning: cascadiarecovery@strike.me


# Contribute

Feel free to open PRs if you have any fixes or enhancements to add

# Warranty

This software is produced AS IS without ANY WARRANTY. This may produce wrong numbers, double-check everything carefully. This software is released into the public domain. 
