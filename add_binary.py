# # Given two binary strings a and b, return their sum as a binary string.
# class Solution:
#     def addBinary( a: str, b: str) -> str:
#         aDecimal =0 
#         bDecimal  = 0 
#         sum = []
#         expo =0 
#         for digit in range(len(a)-1,-1,-1):
#             aDecimal += int(a[digit])*(2**expo)
#             expo+=1
#         expo=0
#         for digit in range(len(b)-1,-1,-1):
#             bDecimal += int(b[digit])*(2**expo)
#             expo+=1
#         sumDecimal= aDecimal+bDecimal
#         if(sumDecimal==0):
#             return '0'
#         while sumDecimal>0 :
#             sum.insert(0,str(sumDecimal%2))
#             sumDecimal = sumDecimal>>1 
#         return "".join(sum)

class Solution:
    def getSum(a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        while b_int != 0:
            carry = a_int & b_int
            a_int = a_int ^ b_int
            b_int = carry << 1
        return bin(a_int)[2:]

        


print(Solution.getSum('0','0'))


