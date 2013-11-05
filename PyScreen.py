import os
from Tkinter import *
import tkMessageBox
import tkFileDialog
import Tkconstants


class PyScreen:
	def __init__(self, parent):

		#attributes
		self.dirname = ""

		#packing the container
		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()			

		#packing text field
		self.text2 = text = Text(self.myContainer1)
		self.text2.insert(INSERT, "Caminho Destino...:")
		self.text2.configure(width=80,height=3)
		self.text2.pack()

		#packing dir open button 
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Selecionar Destino")
		self.button2.configure(width="20")   
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Button-1>", self.file_open) ### (2)

		#packing print screen button
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Print Screen")
		self.button2.configure(width="20")   
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Button-1>", self.print_screen) ### (2)	

		#packing exit button
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Sair")
		self.button2.configure(width="20")   
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Button-1>", self.sair) ### (2)	

	def formatImage(self):
		#aqui vem o PIL
		pass

	def file_open(self,event):
		root = self.myParent
		self.dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Pick a directory')
		self.text2.insert(END, self.dirname)
		print self.dirname


	def print_screen(self,event):
		print self.dirname
		os.system('screencapture ' + self.dirname + '/Print_Screen.jpg' + ' -S')

	def sair(self, event):
		self.myParent.destroy()

if __name__ == '__main__':
	root = Tk()
	root.title("PyScreen")
	myapp = PyScreen(root)
	root.mainloop()
