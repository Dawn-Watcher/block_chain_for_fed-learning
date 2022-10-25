from utility import global_var
from utility import model_class
contractInstance = global_var.get_value('contractInstance')
localAccount = global_var.get_value('localAccount')


def addModel(modelName, description, initialModel, neuralNetworkCode, lr=0.01, bs=64, iter=5):
    modelName = bytes(modelName, 'utf-8')
    lr = bytes(str(lr), 'utf-8')
    try:
        contractInstance.functions.addModel(modelName, description, initialModel,
                                            neuralNetworkCode, lr, bs, iter).transact({'from': localAccount})
        global_var.add_model(initialModel,model_class())#加接口，add,delete都需要对model的map进行修改
        return 'Model is added successfully!'
    except:
        return 'Model exists. Please choose another name.'


def deleteModel(modelName):
    modelName = bytes(modelName, 'utf-8')
    contractInstance.functions.deleteModel(modelName).transact({'from': localAccount})


def updateGlobalModel(modelName, model):
    modelName = bytes(modelName, 'utf-8')
    try:
        contractInstance.functions.updateGlobalModel(modelName, model).transact({'from': localAccount})
        return 'Global model is updated successfully!'
    except:
        return 'Failed. Please check model name and input type.'


def getLocalUpdates(modelName):
    modelName = bytes(modelName, 'utf-8')
    updates = []
    count = []
    loss = []
    try:
        tmp_updates, tmp_count, tmp_loss = contractInstance.functions.getLocalUpdates(modelName).call()
        if count != '':
            updates = tmp_updates.split("<>")[:-1]
            count = tmp_count.split("<>")[:-1]
            loss = tmp_loss.split("<>")[:-1]
            for ii in range(len(count)):
                count[ii] = int(count[ii])
                loss[ii] = float(loss[ii])
    except:
        updates = 'Model does not exist.'
        count = -1
        loss = -1

    return updates, count, loss


