import tkinter



class Objects():
    def __init__(self,a):
        

        self.a = str(a)



    def __str__(self):
        print(self.a)






o = Objects('500')

print(o.a)
alist = [1,2,3,4,5,6,7,8,9]
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_button()
        #w = Canvas(master,width=1000,height=1000) 

        
    #def canvas(self):
         
        

    def create_button(self):
        self.B = tk.Button(self)#board
        self.B["text"] = " Press here to display Board\n(click me)"
        self.B["command"] = self.Board
        self.B.pack()#side = 'top'


        
        
        self.A = tk.Button(self)
        self.A["text"] = "Enter Number:    "
        self.A["command"] = self.playerchoice1
        self.A.pack()

        #self.playerhoice = tk.Button(self)

        self.quit = tk.Button(self, text="QUIT", fg="red",#quit
                              command=root.destroy)
        self.quit.pack()
        

    def Board(self):
        #alist = [1,2,3,4,5,6,7,8,9]
        print ("   ",(alist[0]), '|', alist[1],'|', alist[2])

        print ("   ","-"*10)

        print ("   ",(alist[3]), '|', alist[4],'|', alist[5])

        print ("   ","-"*10)

        print ("   ",(alist[6]), '|', alist[7],'|', alist[8])

    def playerchoice1(self):

        #print("enter number")
        player1 = input("dave:   ")
        
        if player1 == '1':
            if alist[0] == 'x' or alist[0]=='o':
                print("cunt")

                #print("taken")

                #taken = True

                #return taken

                #player()

            else:
                
                alist[0] = 'x'
                print(alist)

        if player1 == '2':
            if alist[1] == 'x' or alist[1]=='o':
                print ("cunt")

                #print("taken")

               # taken = True

                #return taken

                #player()

            else:
                
                alist[1] = 'x'
                print(alist)


        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
