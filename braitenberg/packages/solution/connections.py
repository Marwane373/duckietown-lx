from typing import Tuple
import numpy as np
hauteur = 350
speed_esquive = 1
speed_loin = 0.3
def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    rows, cols = shape
    res[0:500, :320] = -speed_loin  # Rouge uniquement entre les lignes 400 et 500
    res[0:500, 320:] = speed_loin  # Rouge uniquement entre les lignes 400 et 500

    res[hauteur:500, 320:] = -speed_esquive  # Rouge uniquement entre les lignes 400 et 500
    res[hauteur:500, :320] = speed_esquive # Bleu uniquement entre les lignes 400 et 500

    return res

def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    rows, cols = shape

    res[0:500, :320] = speed_loin  # Rouge uniquement entre les lignes 400 et 500
    res[0:500, 320:] = -speed_loin  # Rouge uniquement entre les lignes 400 et 500

    res[hauteur:500, :320] = -speed_esquive # Bleu uniquement entre les lignes 400 et 500
    res[hauteur:500, 320:] = speed_esquive  # Rouge uniquement entre les lignes 400 et 500
    return res

