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


contractAddress = '0xc18a1a71f1620a2b7cbcfde9adabfa3b83957348' #"0xf0977763f405d5a0344be01391a31fe7481d86e0"
peer_ip = 'http://192.168.1.104'
peer_rpcport = '9000'

web3 = Web3(Web3.HTTPProvider(peer_ip + ':' + peer_rpcport))
print('HTTP Provider is connected: ' + str(web3.isConnected()))
contractAddr = web3.toChecksumAddress(contractAddress)

# Contract Info
abi = "[{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"localModelloss\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"localModelCount\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"globalModel\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getGlobalModel\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"getModelList\",\"outputs\":[{\"name\":\"\",\"type\":\"bytes32[]\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getLocalUpdates\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"},{\"name\":\"\",\"type\":\"string\"},{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"learningRate\",\"outputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getBatchSize\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"modelNameList\",\"outputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"neuralNetworkCode\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"modelDescriptionList\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"batchSize\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"},{\"name\":\"model\",\"type\":\"string\"}],\"name\":\"updateGlobalModel\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getNeuralNetworkCode\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"localIter\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"deleteModel\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"localModels\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getModelDescription\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getLocalIter\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"},{\"name\":\"modelupdates\",\"type\":\"string\"},{\"name\":\"countUpdates\",\"type\":\"string\"},{\"name\":\"loss\",\"type\":\"string\"}],\"name\":\"uploadLocalUpdates\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"},{\"name\":\"modelDescription\",\"type\":\"string\"},{\"name\":\"initialModel\",\"type\":\"string\"},{\"name\":\"nnCode\",\"type\":\"string\"},{\"name\":\"lr\",\"type\":\"bytes32\"},{\"name\":\"bs\",\"type\":\"uint8\"},{\"name\":\"iter\",\"type\":\"uint8\"}],\"name\":\"addModel\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"modelName\",\"type\":\"bytes32\"}],\"name\":\"getLearningRate\",\"outputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]"
abi = json.loads(abi)

contractInstance = web3.eth.contract(address=contractAddr, abi=abi)
localAccount = web3.eth.coinbase

global_var._init()
global_var.set_value('contractInstance', contractInstance)
global_var.set_value('localAccount', localAccount)

from blockchain.worker import getModelList, getModelDescription, getGlobalModel, getLocalIter, getNeuralNetworkCode, getLearningRate, getBatchSize, uploadLocalUpdates
from blockchain.requester import addModel, deleteModel, updateGlobalModel, getLocalUpdates


while True:
    print('\nGet Model List:')
    print('Model List: {}'.format(getModelList()))
    wait(2)

'''
deleteModel('Alice')
deleteModel('Bob')
wait(waitTime)

print('\nGet Model List:')
print('Model List: {}'.format(getModelList()))

modelName = 'Alice'
print('\nADD MODEL: {}'.format(modelName))
description = 'This is Alice.'
initialModel = 'This is Alice\'s initial model.'
neuralNetworkCode = 'This is Alice\'s neural network code.'
lr = 0.001
bs = 10
iter = 6
print(addModel(modelName, description, initialModel, neuralNetworkCode, lr=lr, bs=bs, iter=iter))

modelName = 'Bob'
print('\nADD MODEL: {}'.format(modelName))
description = 'This is Bob.'
initialModel = 'This is Bob\'s initial model.'
neuralNetworkCode = 'This is Bob\'s neural network code.'
lr = 0.005
bs = 5
iter = 3
print(addModel(modelName, description, initialModel, neuralNetworkCode, lr, bs, iter))
wait(waitTime)

print('\nGet Model List:')
print('Model List: {}'.format(getModelList()))


# get model information
for modelName in ['Alice', 'Bob', 'Carry']:
    print('\nGet {}:'.format(modelName))
    print('Description: {}'.format(getModelDescription(modelName)))
    print('Global Model: {}'.format(getGlobalModel(modelName)))
    print('Neural Network Code: {}'.format(getNeuralNetworkCode(modelName)))
    print('Learning Rate: {}'.format(getLearningRate(modelName)))
    print('Batch Size: {}'.format(getBatchSize(modelName)))
    print('Local Iter: {}'.format(getLocalIter(modelName)))


for modelName in ['Alice', 'Carry']:
    # upload and get local models
    print('\nGet and update {}\'s local model:'.format(modelName))
    localupdates, count, loss = getLocalUpdates(modelName)
    print('Local updates before update: Updates: {}, Count: {}, Loss: {}'.format(localupdates, count, loss))
    localUpdates1 = 'local updates 1'
    count1 = 8
    loss1 = 0.11
    uploadLocalUpdates(modelName, localUpdates1, count1, loss1)
    localUpdates2 = 'local updates 2'
    count2 = 5
    loss2 = 0.12
    uploadLocalUpdates(modelName, localUpdates2, count2, loss2)
    wait(waitTime)

    localupdates, count, loss = getLocalUpdates(modelName)
    print('Local updates after update: Updates: {}, Count: {}, Loss: {}'.format(localupdates, count, loss))

    # update global model
    print('\nGet and update {}\'s global model:'.format(modelName))
    print('Global model before update: {}'.format(getGlobalModel(modelName)))
    updatedModel = 'This is {}\'s new global model.'.format(modelName)
    updateGlobalModel(modelName, updatedModel)
    wait(waitTime)

    print('Global model after update: {}'.format(getGlobalModel(modelName)))

    # delete model
    print('\nDelete {}:'.format(modelName))
    print('Model list before update: {}'.format(getModelList()))
    deleteModel(modelName)
    wait(waitTime)

    print('Model list after update: {}'.format(getModelList()))
'''