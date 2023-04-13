
#normal_function

def find_fact(x):
    result=1
    while x>=1:
        result=result*x
        x=x-1
    return result


'''def recursive_function(x):

    if x == 1:
        return x
    else:
        return x*recursive_function(x-1)

    #return x if x==1 else(x*recursive_function(x-1))
'''
print(find_fact(5))
#print(recursive_function(5))
