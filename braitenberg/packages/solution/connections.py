from typing import Tuple
import numpy as np

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    rows, cols = shape
    res[:, :320] = 1  # Rouge
    return res

def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    rows, cols = shape
    res[:, 320:] = -1  # Bleu
    return res
