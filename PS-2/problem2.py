import numpy as np
value32=np.float32(1e-40)
one32=np.float32(1.)
while one32+value32==one32:
    value32=value32*1.0001

print("Minimum value added to one that gives a different value than one with 32 bit precision: ",value32)

value64=np.float64(1e-40)
one64=np.float64(1.)
while one64+value64==one64:
    value64=value64*1.0001

print("Minimum value added to one that gives a different value than one with 64 bit precision: ",value64)
maximum32=np.float32(1.)


while True:
    maximum32updated=maximum32*1.0001
    if maximum32updated==float("inf"):
        print("Maximum value before overflow with 32 bit precision:",maximum32)
        break
    maximum32=maximum32updated

maximum64=np.float64(1e40)


while True:
    maximum64updated=maximum64*1.0001
    if maximum64updated==float("inf"):
        print("Maximum value before overflow with 64 bit precision:", maximum64)
        break
    maximum64=maximum64updated
min32=np.float32(1e-40)


while True:
    min32updated=min32*0.2
    if min32updated==0.0:
        print("Minimum value before underflow with 32 bit precision:",min32)
        break
    min32=min32updated

min64=np.float64(1e-40)


while True:
    min64updated=min64*0.2
    if min64updated==0.0:
        print("Minimum value before overflow with 64 bit precision:",min64)
        break
    min64=min64updated