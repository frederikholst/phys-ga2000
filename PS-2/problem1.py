import numpy as np

"""Code is copied from the Jupyter notebook from lecture"""
def get_bits(number):
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    bytes = number.tobytes()
    bits = []
    for byte in bytes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))


value=np.float32(100.98763)
bitlist=get_bits(np.float32(value))
sign = bitlist[0]
exponent = bitlist[1:9]
mantissa = bitlist[9:32]
template = """{value} decimal ->
sign = {sign} 
exponent = {exponent} 
mantissa = {mantissa}"""

Ex=0

for i in np.arange(len(exponent)):
    Ex=Ex+exponent[i]*2**(len(exponent) - 1 - i)

Ex=Ex-127

mant=1

for i in np.arange(len(mantissa)):
    mant=mant+mantissa[i]*2.0**-(i+1)

IEEEvalue=2**Ex*mant

print("Value represented in IEEEE =",IEEEvalue)
print("Difference between actual value and IEEE value =" ,IEEEvalue-100.98763)
