import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return np.amax(x), (np.amax(x) - 0.071) / (alpha**(1 / len(x))) + 0.071
