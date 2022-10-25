from utility import global_var

contractInstance = global_var.get_value('contractInstance')
localAccount = global_var.get_value('localAccount')


def getModelList():
    received = contractInstance.functions.getModelList().call()
    result = list()
    for ii in range(len(received)):
        if received[ii].decode().rstrip('\x00') != '':
            result.append(received[ii].decode().rstrip('\x00'))
    return result


def getModelDescription(modelName):
    modelName = bytes(modelName, 'utf-8')
    try:
        return contractInstance.functions.getModelDescription(modelName).call()
    except:
        return 'Model does not exist.'


def getGlobalModel(modelName):
    modelName = bytes(modelName, 'utf-8')
    try:
        return contractInstance.functions.getGlobalModel(modelName).call()
    except:
        return 'Model does not exist.'


def getNeuralNetworkCode(modelName):
    modelName = bytes(modelName, 'utf-8')
    try:
        return contractInstance.functions.getNeuralNetworkCode(modelName).call()
    except:
        return 'Model does not exist.'


def getLearningRate(modelName):
    modelName = bytes(modelName, 'utf-8')
    try:
        lr_byte32 = contractInstance.functions.getLearningRate(modelName).call()
        return float(lr_byte32.decode().rstrip('\x00'))
    except:
        return 'Model does not exist.'


def getBatchSize(modelName):
    modelName = bytes(modelName, 'utf-8')
    try:
        return int(contractInstance.functions.getBatchSize(modelName).call())
    except:
        return 'Model does not exist.'


def getLocalIter(modelName):
    modelName = bytes(modelName, 'utf-8')
    try:
        return int(contractInstance.functions.getLocalIter(modelName).call())
    except:
        return 'Model does not exist.'


def uploadLocalUpdates(modelName, localUpdates, count, loss):
    modelName = bytes(modelName, 'utf-8')
    count = str(count)
    loss = str(loss)
    try:
        contractInstance.functions.uploadLocalUpdates(modelName, localUpdates, count, loss).transact({'from': localAccount})
        return 'Local updates are submitted successfully!'
    except:
        return 'Failed. Please check model name and input type.'
