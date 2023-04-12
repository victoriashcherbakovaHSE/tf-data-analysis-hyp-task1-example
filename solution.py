import pandas as pd
import numpy as np


chat_id = 871302863

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    n1 = x_cnt
    n2 = y_cnt
    z = (p1 - p2) / (p * (1 - p) * (1/n1 + 1/n2)) ** 0.5
    return abs(z) > 1.96
