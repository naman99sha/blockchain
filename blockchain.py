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

#Mining Blockchain