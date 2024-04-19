import math
def score(x, y):
    scores = ((10.01,0),(5.01,1),(1.01,5),(0,10)) #(distance, score)
    dart_distance = math.sqrt(x**2 + y**2)
    return next(final_score for distance, final_score in scores if dart_distance >= distance)
