from web3 import Web3
from utility import global_var
import json
import threading
import time

waitTime = 10
def wait(num):
    print('waiting...')
    for ii in range(num):
        print(str(ii + 1) + '...')
        time.sleep(1)

contractAddress = "0x6a303f9045D4508A6a9aABD8F5921498BbD99b8d" #"0xc18a1a71f1620a2b7cbcfde9adabfa3b83957348" #智能合约部署地址
peer_ip = 'http://127.0.0.1'
peer_rpcport = '7545'       # 端口

web3 = Web3(Web3.HTTPProvider(peer_ip + ':' + peer_rpcport))
print('HTTP Provider is connected: ' + str(web3.isConnected()))
contractAddr = web3.toChecksumAddress(contractAddress)

# Contract Info
abi="""[
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "localModelloss",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "localModelCount",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "globalModel",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getGlobalModel",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "getModelList",
		"outputs": [
			{
				"name": "",
				"type": "bytes32[]"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getLocalUpdates",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "learningRate",
		"outputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getBatchSize",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "modelNameList",
		"outputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "neuralNetworkCode",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "modelDescriptionList",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "batchSize",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			},
			{
				"name": "model",
				"type": "string"
			}
		],
		"name": "updateGlobalModel",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getNeuralNetworkCode",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "localIter",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "deleteModel",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "localModels",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getModelDescription",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getLocalIter",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			},
			{
				"name": "modelupdates",
				"type": "string"
			},
			{
				"name": "countUpdates",
				"type": "string"
			},
			{
				"name": "loss",
				"type": "string"
			}
		],
		"name": "uploadLocalUpdates",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			},
			{
				"name": "modelDescription",
				"type": "string"
			},
			{
				"name": "initialModel",
				"type": "string"
			},
			{
				"name": "nnCode",
				"type": "string"
			},
			{
				"name": "lr",
				"type": "bytes32"
			},
			{
				"name": "bs",
				"type": "uint8"
			},
			{
				"name": "iter",
				"type": "uint8"
			}
		],
		"name": "addModel",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "modelName",
				"type": "bytes32"
			}
		],
		"name": "getLearningRate",
		"outputs": [
			{
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	}
]"""

abi=json.loads(abi)
contractInstance = web3.eth.contract(address=contractAddr, abi=abi)
localAccount = web3.eth.coinbase

global_var._init()
global_var.set_value('contractInstance', contractInstance)
global_var.set_value('localAccount', localAccount)

from blockchain.worker import getModelList, getModelDescription, getGlobalModel, getLocalIter, getNeuralNetworkCode, getLearningRate, getBatchSize, uploadLocalUpdates
from blockchain.requester import addModel, deleteModel, updateGlobalModel, getLocalUpdates

modelName = 'Fed_avg'
description = 'Fed_avg model'
initialModel = 'fed_avg'//哈希值
neuralNetworkCode = 'This is Fed_avg\'s neural network code.'
lr = 0.001
bs = 10
iter = 5
print(addModel(modelName, description, initialModel, neuralNetworkCode, lr=lr, bs=bs, iter=iter))

