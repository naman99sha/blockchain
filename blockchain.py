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

#Mining Blockchain