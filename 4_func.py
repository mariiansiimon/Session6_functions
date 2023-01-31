import math

def edu_distance( a1, b1, a2, b2 ):
    d = ( a2 - a1 ) ** 2 - ( b2 - b1 ) ** 2 
    final_d = math.sqrt(d)
    
    return print(final_d)

edu_distance(30, 12 , 6, 2)



# teacher's answer



import math

def cal_dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])
