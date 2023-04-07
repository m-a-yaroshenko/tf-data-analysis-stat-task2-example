import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.max()
    sd = x.std()

    scale = 1 / np.sqrt(len(x)) * sd
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
