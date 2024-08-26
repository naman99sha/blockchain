# Module 1 - Creating a blockchain
import datetime
import hashlib
import json
from flask import Flask, jsonify

#Building blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, prev_hash = '0')
        
    def create_block(self, proof, prev_hash):
        block = {
            'index': len(self.chain)+1, 
            'timestamp': str(datetime.datetime().now()), 
            'proof':proof, 
            'previous_hash':prev_hash
            }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def verify_chain(self, chain):
        prev_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(prev_block):
                return False
            prev_proof = prev_block['proof']
            cur_proof = block['proof']
            hash_operation = hashlib.sha256(str(cur_proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False
            prev_block = block
            block_index += 1
        return True

#Mining Blockchain

# - Create a web app to interact with blockchain
app = Flask(__name__)

# - Create a blockchain
blockchain = Blockchain()

# - Mine a new block
@app.route("/mine-block", methods=['GET'])
def mine_block():
    prev_block = blockchain.get_previous_block()
    prev_proof = prev_block['proof']
    proof = blockchain.proof_of_work(prev_proof)
    prev_hash = blockchain.hash(prev_block)
    block = blockchain.create_block(proof, prev_hash)
    response = {
        'message': "Congrats!! Block Mined successfully!",
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash':block['previous_hash']
    }
    return jsonify(response), 200

# - Return the full chain
@app.route("/get-chain", methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

# Run the app