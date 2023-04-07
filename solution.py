import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import dlaplace

chat_id = 1017890038 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = np.median(x)
    temp = []
    for i in len(x):
        temp[i] = x[i] - loc
    D = 2*(np.sum(temp))**2
    D = D/len(x)
    D = D/len(x)
    scale = np.sqrt(D) / np.sqrt(len(x))
    return loc - scale * dlaplace.ppf(1 - alpha / 2), \
           loc - scale * dlaplace.ppf(alpha / 2)
