import tkinter
from tkinter import ttk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import Entry
from tkinter import Button
import numpy as np


class Sys(tkinter.Frame):


    def error_in_coeff(self):
        if(self.m.get()=='1'):
            if(self.in1.get()!='' and self.in2.get()!=''):
                1
            else:
                return False
        elif(self.m.get()=='2'):
            if(self.in1.get()!='' and self.in2.get()!='' and self.in3.get()!=''):
                1
            else:
                return False
        elif(self.m.get()=='3'):
            if(self.in1.get()!='' and self.in2.get()!='' and self.in3.get()!='' and self.in4.get()!=''):
                1
            else:
                return False
        elif(self.m.get()=='4'):
            if(self.in1.get()!='' and self.in2.get()!='' and self.in3.get()!='' and self.in4.get()!='' and self.in5.get()!=''):
                1
            else:
                return False
        if(self.n.get()=='1'):
            if(self.in6.get()!='' and self.in7.get()!=''):
                1
            else:
                return False
        elif(self.n.get()=='2'):
            if(self.in6.get()!='' and self.in7.get()!='' and self.in8.get()!=''):
                1
            else:
                return False
        elif(self.n.get()=='3'):
            if(self.in6.get()!='' and self.in7.get()!='' and self.in8.get()!='' and self.in9.get()!=''):
                1
            else:
                return False
        elif(self.n.get()=='4'):
            if(self.in6.get()!='' and self.in7.get()!='' and self.in8.get()!='' and self.in9.get()!='' and self.in10.get()!=''):
                1
            else:
                return False
            

    def createNewWindow3(self):
        cond=self.error_in_coeff()
        if(cond==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        else:
            newWindow3 = tkinter.Toplevel(self.parent)
            newWindow3.title("State-Space Represtentaion")
            newWindow3.geometry('800x400')

            cond=self.error_in_coeff()
            if(cond==False):
                newWindow3.destroy()


            label_1 = tkinter.Label(newWindow3, text = "State-Space Represtentaion", font=("Times New Roman Bold", 30))
            label_1.place(relx=0.22,rely=0.01)
            scroll = tkinter.Scrollbar(newWindow3)
            scroll.pack(side="right", fill="y")
            txt1 = tkinter.Text(newWindow3, height=5, width=30, wrap="none", yscrollcommand=scroll.set)
            matrices=self.state_space_representaion(int(self.n.get()), int(self.m.get()))
            first = matrices['A']
            second = matrices['B']
            third = matrices['C']
            fourth = matrices['D']
            np.set_printoptions(precision=3, floatmode='fixed')
            txt1.insert('end','A:')
            txt1.insert('end',first)
            txt1.insert('end','\n')
            txt1.insert('end','B:')
            txt1.insert('end',second)
            txt1.insert('end','\n')
            txt1.insert('end','C:')
            txt1.insert('end',third)
            txt1.insert('end','\n')
            txt1.insert('end','D:')
            txt1.insert('end',fourth)
            scroll.config(command=txt1.yview)
            txt1.config(font=("Times New Roman Bold", 30), state="disabled")
            txt1.place(relx=0.01,rely=0.15)


    def coeff_to_array(self):
        coeffs = []
        if(self.in1.get()!=''):
            float(self.in1.get())
            coeffs.append(float(self.in1.get()))
        if(self.in2.get()!=''):
            float(self.in2.get())
            coeffs.append(float(self.in2.get()))
        if(self.in3.get()!=''):
            float(self.in3.get())
            coeffs.append(float(self.in3.get()))
        if(self.in4.get()!=''):
            float(self.in4.get())
            coeffs.append(float(self.in4.get()))
        if(self.in5.get()!=''):
            float(self.in5.get())
            coeffs.append(float(self.in5.get()))
        if(self.in6.get()!=''):
            float(self.in6.get())
            coeffs.append(float(self.in6.get()))
        if(self.in7.get()!=''):
            float(self.in7.get())
            coeffs.append(float(self.in7.get()))
        if(self.in8.get()!=''):
            float(self.in8.get())
            coeffs.append(float(self.in8.get()))
        if(self.in9.get()!=''):
            float(self.in9.get())
            coeffs.append(float(self.in9.get()))
        if(self.in10.get()!=''):
            float(self.in10.get())
            coeffs.append(float(self.in10.get()))
        return coeffs


    def state_space_representaion (self,n,m):
        """ state derivatives matrix """
        coeffs=self.coeff_to_array()
        coeffs[:] = [x / coeffs[n] for x in coeffs]
        derivatives_state_variables = []
        for i in range(n):

            derivatives_state_variables.append( "X'")
            derivatives_state_variables[i] = derivatives_state_variables[i] + str(i+1)

        """ matrix A """

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
    
        """ state variables matrix """  
        state_variables = []
        for i in range(n):
            state_variables.append( "X")
            state_variables[i] = state_variables[i] + str(i+1)

        """ C matrix """
        c = []
        c = np.reshape(np.zeros(1*n),(1,n))
        c[(0,n-1)] = 1
     
        """ B matrix """
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


#Function for checking the Comboboxes m and n


    def check(self,event):
        if(not self.m.get().isdigit()):
            messagebox.showerror('Error','m must be a number')
            self.m.set(1)
        if(not self.n.get().isdigit()):
            messagebox.showerror('Error','n must be a number')
            self.n.set(1)
        if(self.m.get()>'4'):
            messagebox.showerror('Error','m is out of range')
            self.m.set(1)
        if(self.n.get()>'4'):
            messagebox.showerror('Error','n is out of range')
            self.n.set(1)
        if(self.m.get()>self.n.get()):
            messagebox.showerror('Error','m must be a number less than or equal n')
            self.m.set(1)

#Function for checking coefficients of a


    def coeff_of_a(self,event):
        if(self.n.get()>='2'):
            self.a2.config(state='normal')
        else:
            self.a2.delete(0,last='end')
            self.a2.config(state='readonly')
        if(self.n.get()>='3'):
            self.a3.config(state='normal')
        else:
            self.a3.delete(0,last='end')
            self.a3.config(state='readonly')
        if(self.n.get()>='4'):
            self.a4.config(state='normal')
        else:
            self.a4.delete(0,last='end')
            self.a4.config(state='readonly')

#Function for checking coefficients of b

    def coeff_of_b(self,event):
        if(self.m.get()>='2'):
            self.b2.config(state='normal')
        else:
            self.b2.delete(0,last='end')
            self.b2.config(state='readonly')
        if(self.m.get()>='3'):
            self.b3.config(state='normal')
        else:
            self.b3.delete(0,last='end')
            self.b3.config(state='readonly')
        if(self.m.get()>='4'):
            self.b4.config(state='normal')
        else:
            self.b4.delete(0,last='end')
            self.b4.config(state='readonly')

#Combining Function for bind function

    def combine(self,event):
        self.coeff_of_a(event)
        self.coeff_of_b(event)


#Function for checking entry input

    def testVal(self,inStr,acttyp):
        if(acttyp=='1'):
            try:
                if (inStr=='-' or isinstance(float(inStr), float)):
                    1
            except:
                return False
        return True
    
    
    
    
    
    def __init__(self, parent):
        
        
        tkinter.Frame.__init__(self, parent)
        
        
        
        self.parent = parent
        self.in1=StringVar()
        self.in2=StringVar()
        self.in3=StringVar()
        self.in4=StringVar()
        self.in5=StringVar()
        self.in6=StringVar()
        self.in7=StringVar()
        self.in8=StringVar()
        self.in9=StringVar()
        self.in10=StringVar()




#titles and equations

        self.l1 = tkinter.Label(self.parent, text = "Group 48 System Simulator", font=("Times New Roman Bold", 30)).grid(column=3, row=0)
        self.l2 = tkinter.Label(self.parent, text = "tzbtt Equation", font=("Times New Roman", 26)).grid(pady=20, column=3, row=1)

#n Combobox

        self.l3 = tkinter.Label(self.parent, text = "n=", font=("Times New Roman", 16)).grid(padx=(6,0), column=0, row=3)
        self.n= ttk.Combobox(self.parent, values=[1,2,3,4])
        self.n.grid(column=1, row=3)
        self.n.current(0)

#m Combobox

        self.l4 = tkinter.Label(self.parent, text = "m=", font=("Times New Roman", 16)).grid(column=4, row=3)
        self.m= ttk.Combobox(self.parent, values=[1,2,3,4])
        self.m.grid(column=5, row=3)
        self.m.current(0)

#bind fuction waiting for those events (check Function which checks m's and n's  comboboxes)

        self.parent.bind('<ButtonRelease-1>', self.check) and self.parent.bind('<Return>', self.check)

#a0 label

        self.l5 = tkinter.Label(self.parent, text = "a\u2092=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=4)
#a0 entry with calling validation function

        self.a0=Entry(self.parent, textvariable=self.in1, width=23, validate="key")
        self.a0['validatecommand'] = (self.a0.register(self.testVal),'%P','%d')
        self.a0.grid(column=1, row=4)

#a1 label

        self.l6= tkinter.Label(self.parent, text = "a\u2081=", font=("Times New Roman", 16), ).grid(padx=(3,0), column=0, row=5)
#a1 entry with calling validation function

        self.a1=Entry(self.parent, textvariable=self.in2, width=23, validate="key")
        self.a1['validatecommand'] = (self.a1.register(self.testVal),'%P','%d')
        self.a1.grid(column=1, row=5)

#a2 label

        self.l7= tkinter.Label(self.parent, text = "a\u2082=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=6)
#a2 entry with calling validation function

        self.a2=Entry(self.parent, textvariable=self.in3, width=23, validate="key", state="readonly")
        self.a2['validatecommand'] = (self.a2.register(self.testVal),'%P','%d')
        self.a2.grid(column=1, row=6)

#a3 label

        self.l8= tkinter.Label(self.parent, text = "a\u2083=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=7)
#a3 entry with calling validation function

        self.a3=Entry(self.parent, textvariable=self.in4, width=23, validate="key", state="readonly")
        self.a3['validatecommand'] = (self.a3.register(self.testVal),'%P','%d')
        self.a3.grid(column=1, row=7)
#a4 label

        self.l9 = tkinter.Label(self.parent, text = "a\u2084=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=8)
#a4 entry with calling validation function

        self.a4=Entry(self.parent, textvariable=self.in5, width=23, validate="key", state="readonly")
        self.a4['validatecommand'] = (self.a4.register(self.testVal),'%P','%d')
        self.a4.grid(column=1, row=8)
#b0 label

        self.l10 = tkinter.Label(self.parent, text = "b\u2092=", font=("Times New Roman", 16)).grid(column=4, row=4)
#b0 entry with calling validation function

        self.b0=Entry(self.parent, textvariable=self.in6, width=23, validate="key")
        self.b0['validatecommand'] = (self.b0.register(self.testVal),'%P','%d')
        self.b0.grid(column=5, row=4)

#b1 label

        self.l11= tkinter.Label(self.parent, text = "b\u2081=", font=("Times New Roman", 16)).grid(column=4, row=5)
#b1 entry with calling validation function

        self.b1=Entry(self.parent, textvariable=self.in7, width=23, validate="key")
        self.b1['validatecommand'] = (self.b1.register(self.testVal),'%P','%d')
        self.b1.grid(column=5, row=5)

#b2 label

        self.l12= tkinter.Label(self.parent, text = "b\u2082=", font=("Times New Roman", 16)).grid(column=4, row=6)
#b2 entry with calling validation function

        self.b2=Entry(self.parent, textvariable=self.in8, width=23, validate="key", state="readonly")
        self.b2['validatecommand'] = (self.b2.register(self.testVal),'%P','%d')
        self.b2.grid(column=5, row=6)

#b3 label

        self.l13= tkinter.Label(self.parent, text = "b\u2083=", font=("Times New Roman", 16)).grid(column=4, row=7)
#b3 entry with calling validation function

        self.b3=Entry(self.parent, textvariable=self.in9, width=23, validate="key", state="readonly")
        self.b3['validatecommand'] = (self.b3.register(self.testVal),'%P','%d')
        self.b3.grid(column=5, row=7)
#b4 label

        self.l14= tkinter.Label(self.parent, text = "b\u2084=", font=("Times New Roman", 16)).grid(column=4, row=8)
#b4 entry with calling validation function

        self.b4=Entry(self.parent, textvariable=self.in10, width=23, validate="key", state="readonly")
        self.b4['validatecommand'] = (self.b4.register(self.testVal),'%P','%d')
        self.b4.grid(column=5, row=8)
#bind fuction waiting for those events (combine Function which checks a's and b's  coefficients)

        self.parent.bind('<Motion>', self.combine) and self.parent.bind('<FocusOut>', self.combine)

#Type input label

        self.l15 = tkinter.Label(self.parent, text = "Input Type", font=("Times New Roman", 16)).grid(pady=(20,0), column=3, row=9)
#Type input Combobox

        self.input_type= ttk.Combobox(self.parent, values=["Type Impulse", "Type Step"])
        self.input_type.grid(column=3, row=10)
        self.input_type.current(0)
#Simulation time label

        self.l16 = tkinter.Label(self.parent, text = "Simulation time", font=("Times New Roman", 16)).grid(pady=(20,0), column=3, row=11)
#Simulation time Scale

        self.time_meter = tkinter.Scale(self.parent, from_=1, to=30, orient="horizontal")
        self.time_meter.grid(column=3, row=12)
#Plotting input button


        self.bt1=Button(self.parent, text="Plotting Input", font=("Times New Roman", 16), bg="lightblue").grid(pady=20, column=0, columnspan=2, row=13)  #add command attribute with the function after font as: , command=fuction()
#Plotting output button

        self.bt2=Button(self.parent, text="Plotting Output", font=("Times New Roman", 16), bg="lightblue").grid(pady=20, column=4, columnspan=2, row=13)  #add command attribute with the function after font as: , command=fuction()
#State-Space Representention button

        self.bt3=Button(self.parent, text="State-Space Represtentaion", font=("Times New Roman", 16), bg="lightblue", command=self.createNewWindow3).grid(column=3, row=14)  #add command attribute with the function after font as: , command=fuction()
#Visualizing System States button

        self.bt4=Button(self.parent, text="Visualizing System States", font=("Times New Roman", 16), bg="lightblue").grid(pady=20, column=3, row=15)  #add command attribute with the function after font as: , command=fuction()


        
if __name__ == "__main__":
    window = tkinter.Tk()
    Sys(window).place(relx=1, rely=1)
    window.mainloop()