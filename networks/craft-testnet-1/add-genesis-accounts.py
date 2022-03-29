from operator import ge
import os
import json
from pathlib import Path

# cd networks/craft-testnet-1/

LAUNCH_TIME = "2022-03-30T17:00:00Z"
CHAIN_ID = "craft-testv3"
EXP_SEND = [{"denom": "uexp","enabled": True}]

GENESIS_FILE=f"{Path.home()}/.craftd/config/genesis.json"
FOLDER = "gentx-v3"

def main():
    # outputDetails()
    resetGenesisFile()
    # createGenesisAccountsCommands()

def resetGenesisFile():
    # load genesis.json & remove all values for accounts & supply
    with open(GENESIS_FILE) as f:
        genesis = json.load(f)
        genesis["genesis_time"] = LAUNCH_TIME
        genesis["chain_id"] = str(CHAIN_ID)

        genesis["app_state"]['auth']["accounts"] = []
        genesis["app_state"]['bank']["balances"] = []
        genesis["app_state"]['bank']["supply"] = []
        genesis["app_state"]['bank']["params"]["send_enabled"] = EXP_SEND

        genesis["app_state"]['genutil']["gen_txs"] = []

    # save genesis.json
    with open(GENESIS_FILE, 'w') as f:
        json.dump(genesis, f, indent=4)


def outputDetails() -> str:
    # get the seconds until LAUNCH_TIME
    launch_time = int(os.popen("date -d '" + LAUNCH_TIME + "' +%s").read())
    now = int(os.popen("date +%s").read())
    seconds_until_launch = launch_time - now

    # convert seconds_until_launch to hours, minutes, and seconds
    hours = seconds_until_launch // 3600
    minutes = (seconds_until_launch % 3600) // 60

    print(f"# {LAUNCH_TIME} ({hours}h {minutes}m) from now\n# {CHAIN_ID}\n")

def createGenesisAccountsCommands():
    gentx_files = os.listdir(FOLDER)
    for file in gentx_files:
        f = open(FOLDER + "/" + file, 'r')
        data = json.load(f)

        validatorData = data['body']['messages'][0]
        moniker = validatorData['description']['moniker']
        delegator = validatorData['delegator_address']
        amt = validatorData['value']['amount']

        if delegator == "craft13vhr3gkme8hqvfyxd4zkmf5gaus840j5hwuqkh":
            print(f"craftd add-genesis-account {delegator} 100000000000000ucraft,30000000000uexp #pbcups")
        else:
            print(f"craftd add-genesis-account {delegator} 10000000000ucraft,{amt}uexp #{moniker}")


if __name__ == "__main__":
    main()