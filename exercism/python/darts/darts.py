import math


def score(x: float, y: float) -> int:
    scores = [[10, 0], [5, 1], [1, 5], [0, 10]] #[distance, score]
    dart_distance = math.sqrt(x ** 2 + y ** 2)
    return next((final_score for distance, final_score in scores if dart_distance > distance), 10)