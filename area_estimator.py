#build a function that estimates the area above y=x2 over the area the under y=x2

import random

def est_run(n):
    num_point_under=0
    num_point_over=0
    for _ in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        calc = x**2-y
        if calc <=0:
            num_point_under +=1
        if calc > 0:
            num_point_over +=1
    return num_point_under/num_point_over
