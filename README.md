
Functions:

- CLASS: Block
- this represents a individual block in the chain
- Create a new block.
- Each block stores its hash and hash of previous block. 

- CLASS: Blockchain
- this class represents the ledger or the chain it stores all the blocks on the block chain.
- distribute_ledger()-> this function passes a copy of the ledger (blockchain) to every
node (computer) in the network.

- CLASS: Computer
- this represents a node in the network and each node should have a copy of ledger (blockchain)
- validate_block()-> this function validates a new block by verifying if its previous hash is
equal to the hash of the latest block in the chain. 

- CLASS: Network
- this represents the entity in which the blockchain distributed
- stores all the computer-objects
- braodcast_block_validation()-> this function passes a new block to each node (computer) in the network and calls validate_block() if every node (computer) says the block is valid it adds
it to the actual ledger (blockchain)
- propagate_valid_block()-> this function broadcasts the new block to other nodes as part of their regular communication. It updates the local copies of the ledger of each node with the new block.

- HOW TO USE:
- Syntax is "Block {hash}| Data: 'some text'| Prev: {hash of previous block}
- WHen prompted enter the data for the new block to be updated
- Then you will be prompted to enter the previous hash, look at the current
state of the blockchain and copy and past the hash of the last block. 
- If the credential of the block are valid you will recieve Adding block....Validation Passed!
- If block is invalid you will recieve Adding block....Validation Failed!
- Enter q to quit.