import random
import copy

class Block:
    def __init__(self, data, previous_hash=0):
        self.data = data 
        self.hash = 0                      # dependent on data
        self.previous_hash = previous_hash # hash of previous block in the chain
        self.compute_hash()

    def compute_hash(self):
        self.hash = hash(self.data)
        

class Blockchain: 
    def __init__(self, name):
        self.chain = [Block("genesis", "null")]
        self.name = name

    def create_block(self, data):
        if len(self.chain) > 0:
            b1 = Block(data, self.chain[-1].hash)
        else:
            b1 = Block(data, "null")
        #self.chain.append(b1)
        return b1

    def show_chain(self):
        print("\tBlockchain: " + str(self.name) + "")
        print("------------------------------------------")
        for i, block in enumerate(self.chain):
            print("Block: " + str(block.hash) +"| Data: "+ str(block.data) + "| Prev: " + str(block.previous_hash))
            print("------------------------------------------")

    def distribute_ledger(self, computers):
        print("Distributing ledger to all nodes in network...")
        for computer in computers:
            computer.ledger = copy.deepcopy(self)

class Computer:
    def __init__(self, primary_key=0):
        self.primary_key = primary_key
        self.ledger = None
    
    def show(self):
        print("Computer: " + str(self.primary_key) + "| Ledger: " + str(self.ledger.name))

    def validate_block(self, new_block):
        if new_block.previous_hash == self.ledger.chain[-1].hash == False:
            return False
        return True
        
class Network:
    def __init__(self, computers):
        self.computers = computers

    def show_status(self):
        for computer in self.computers:
            computer.show()
        print("------------------------------------------")

    def braodcast_block_validation(self, block):
        for computer in self.computers:
            if computer.validate_block(block) == False:
                print("Adding block....Validation Failed!")
                return False
            
        print("Adding block....Validation Passed!")
        return True
    
    def propagate_valid_block(self, new_block):
        for computer in self.computers:
            computer.ledger.chain.append(new_block)

    

def main():
    computers = []
    for i in range(2):
        computers.append(Computer(i+1))
    network = Network(computers=computers)

    block_chain = Blockchain("Chain#1")
    block_chain.show_chain()
    block_chain.distribute_ledger(computers)
    network.show_status()

    run = True
    while run:
        new_block_data = input("Enter data of new block: ")
        if new_block_data == "q":
            run = False
            break
        new_block_prev_hash = int(input("Enter previous hash of new block: "))
        print(("------------------------------------------"))
        #new_block = block_chain.create_block(new_block_data)
        new_block = Block(new_block_data, new_block_prev_hash)
        if network.braodcast_block_validation(new_block) == True:
            block_chain.chain.append(new_block)
            network.propagate_valid_block(new_block)
        block_chain.show_chain()
        
        # Confirm changes to ledger is migrated throughout all nodes in network
        # network.computers[0].ledger.show_chain()
    

main()