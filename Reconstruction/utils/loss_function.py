import torch
import torch.nn as nn

def select_loss_function(loss_function):
    if loss_function == 'CELoss':
        return nn.BCELoss(size_average=False)
    elif loss_function == 'MSELoss':
        return nn.MSELoss()
    else:
        return ''
