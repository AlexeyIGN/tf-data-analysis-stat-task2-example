import pandas as pd 
import numpy as np 
from scipy.stats import norm 
from scipy.stats import expon

chat_id = 1017890038 

def solution(p: float, x: np.array) -> tuple: 
    E=x.mean() 
    s=0
    for c in x: 
        s+=(c-E)**2 
    s/=len(x) - 1
    s=s**0.5 
    alpha=1-p 
    left = 0.5 + E + expon.ppf(alpha/2)*s/len(x)**0.5 
    right = 0.5 + E - expon.ppf(alpha/2)*s/len(x)**0.5
    left*=2/2**2 
    right*=2/2**2 
    return left, right
