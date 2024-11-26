import numpy as np

def calculate(list):
    n=len(list)
    if n<9:
        raise ValueError("List must contain nine numbers.")

    orig=np.array(list)
    reorg=orig.reshape(3,3)
    mean=[np.mean(reorg,axis=0).tolist(),np.mean(reorg,axis=1).tolist(),np.mean(reorg)]
    variance=[np.var(reorg,axis=0).tolist(),np.var(reorg,axis=1).tolist(),np.var(reorg)]
    std=[np.std(reorg,axis=0).tolist(),np.std(reorg,axis=1).tolist(),np.std(reorg)]
    maxv=[np.max(reorg,axis=0).tolist(),np.max(reorg,axis=1).tolist(),np.max(reorg)]
    minv=[np.min(reorg,axis=0).tolist(),np.min(reorg,axis=1).tolist(),np.min(reorg)]
    sumv=[np.sum(reorg,axis=0).tolist(),np.sum(reorg,axis=1).tolist(),np.sum(reorg)]

    calculations={
        'mean':mean,
        'variance':variance,
        'standard deviation':std,
        'max':maxv,
        'min':minv,
        'sum':sumv
    }

    return calculations