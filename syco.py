import matplotlib.pyplot as plt
'''
coeffs_a = [0, 0, 0, 0, 0]
coeffs_b = [0, 0, 0, 0, 0]
all_coeffs = coeff_to_array()
for i in range(n+1) {
    coeffs_a[i] = all_coeffs[i]
}
for i in range(m+1) {
    coeffs_b[i] = all_coeffs[n+1]
}
'''
def main():
    h = 0.4
    Time = 11
    Fx = [0, 0, 0, 0]
    a4 = 0
    a3 = 0
    a2 = 1
    a1 = 0
    a0 = 0
    x = [] 
    i = 0
    for k in range(4, int(Time*1/h)):
        #y0 = ( 1 - (-a1/h - 2*a2 / (h**2))*Fx[-1] - a2/(h**2) * Fx[-2] ) / ( a2/(h**2) + a1/h + a0)
        y0 = ( (1) - (-a1/h - 2*a2 / (h**2) - 3*a3 / (h**3) - 4*a4 / (h**4) )*Fx[-1] - ( a2/(h**2) + 3*a3 / (h**3) + 6*a4 / (h**4) ) * Fx[-2] -( - a3 / (h**3) - 4*a4 / (h**4) ) * Fx[-3] -( a4 / (h**4)) * Fx[-4] )/ ( a4 / (h**4) + a3 / (h**3) + a2 / (h**2) + a1 / h + a0 )
        Fx.append(y0)
    for k in range(0, int(Time*1/h)):
        x.append(i)
        i += h
    plt.figure('Output')
    plt.plot(x, Fx)
    plt.xlabel('Time (sec)') 
    plt.ylabel('y(t)')
    plt.show()
if __name__== "__main__" :
    main()