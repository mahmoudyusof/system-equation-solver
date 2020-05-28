import numpy as np

def state_space_representaion (coeffs):
     coeffs[:] = [x / coeffs[n] for x in coeffs]

     # state derivatives matrix 

     derivatives_state_variables = []
     for i in range(n):

         derivatives_state_variables.append( "X'")
         derivatives_state_variables[i] = derivatives_state_variables[i] + str(i+1)

        # matrix A

     coeff_array = np.reshape(np.zeros(n*n),(n,n))
     k = 0

     for i in range(n):
         for j in range (n):
             if j == n-1:
                 coeff_array[i,j] = (-1) * coeffs[k]
                 k -= 1
                 if k == n-1 :
                     break
     for i in range(n):
         for j in range(n):
             if i-j == 1 :
                 coeff_array[i,j] = 1
    
        # state variables matrix  

     state_variables = []
     for i in range(n):
         state_variables.append( "X")
         state_variables[i] = state_variables[i] + str(i+1)

        # C matrix 
     c = []
     c = np.reshape(np.zeros(1*n),(1,n))
     c[(0,n-1)] = 1
     
      # B matrix 
     k = np.reshape(np.zeros(n*1),(n,1))
     a = coeffs[0:n+1]
     b = coeffs [n+1:]
     x = 0

     for i in range (len(a)-len(b)):
         b.append(0)

     for i in range(n) :
         k[i] = b[x] - a[x]*b[m]
         x+=1

     """ D matrix"""
     d = b[m]

     return  {'A':coeff_array , 'B':k , 'C':c , 'D':d ,
     'Derivatives_of_sates':np.reshape(derivatives_state_variables,(n,1)) ,
     'states':np.reshape(state_variables,(n,1))}


m = int(input("Enter value of m:\n"))
n = int(input("Enter value of n:\n"))
coeffs = []

if m <= n:
    print("Enter a's and b's respectively")
    for index in range(m+n+2):
        coeffs.append(float(input("")))

    matrices = state_space_representaion(coeffs)
    np.set_printoptions(precision=3, floatmode='fixed')
    # Just for Testing 
    print(matrices['A']) 
    print(matrices['B'])
    print(matrices['C'])
    print(matrices['D'])