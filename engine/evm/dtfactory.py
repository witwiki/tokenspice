from web3tools import web3util
from web3tools.wallet import Wallet

class DTFactory:
    def __init__(self):
        name = self.__class__.__name__
        abi = web3util.abi(name)
        web3 = web3util.get_web3()
        contract_address = web3util.contractAddress(name)
        self.contract = web3.eth.contract(contract_address, abi=abi)
        
    @property
    def address(self):
        return self.contract.address
        
    #============================================================
    #reflect DTFactory Solidity methods
    def createToken(self, blob: str, from_wallet: Wallet) -> str:
        f = self.contract.functions.createToken(blob)
        (tx_hash, tx_receipt) = util.buildAndSendTx(f, from_wallet)

        warnings.filterwarnings("ignore") #ignore unwarranted warning up next
        rich_logs = getattr(self.contract.events, 'TokenCreated')().processReceipt(tx_receipt)
        token_address = rich_logs[0]['args']['newTokenAddress'] 
        warnings.resetwarnings()

        return token_address
