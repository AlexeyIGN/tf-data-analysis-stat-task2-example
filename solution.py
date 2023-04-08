import pandas as pd 
import numpy as np 
from scipy.stats import norm
from scipy.stats import chi2

chat_id = 1017890038 

def solution(p: float, x: np.array) -> tuple: 
    E=x.mean() 
    s=0
    for c in x: 
        s+=(c-E)**2 
    s/=len(x)-1
    s=s**0.5 
    alpha=1-p 
    #left = 0.5 + E + chi2.ppf(alpha/2)*s/len(x)**0.5 
    #right = 0.5 + E - chi2.ppf(alpha/2)*s/len(x)**0.5
    left = 0.5 - E - 2*len(x)*E / chi2.ppf((1+p)/2 , df = 2*len(x))
    right = 0.5 - E - 2*len(x)*E / chi2.ppf((1-p)/2 , df = 2*len(x))
    left*=2/2**2 
    right*=2/2**2 
    return left, right
