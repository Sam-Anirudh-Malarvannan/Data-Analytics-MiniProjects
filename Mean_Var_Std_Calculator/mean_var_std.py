import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must have 9 elements')

    arr = np.array(list).reshape(3,3)

    calculations = {
        'mean' : [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.flatten().mean()],
        'variance' : [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.flatten().var()],
        'standard deviation' : [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.flatten().std()],
        'max' : [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.flatten().max()],
        'min' : [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.flatten().min()],
        'sum' : [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.flatten().sum()]
    }

    return calculations