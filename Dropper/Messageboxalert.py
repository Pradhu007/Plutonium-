import os
import sys
import tkinter as Tk
import tkinter.messagebox

count = 3
i = 0
done = False



def checkforinfection():
    if os.path.exists("date.txt") == True:
        return True# We would not be checking for this...



while done!= True:

    s = tkinter.messagebox.askyesno("Are you sure you want to execute this")

    if s == True:
        i = i +1
    else:
        sys.exit()


    if i == 2:
        s = tkinter.messagebox.askyesno("Plutonium.exe","Choosing  to execute this might make your system unstable")

        if s == False:
            break
        else:
            i = i + 1


    if i == count:


       done = True



if done == True:
    if checkforinfection() == True:
        sys.exit()
        # Why bother when this system has been infected before...
    else:
        print("STARTING INFECTION NOW")
        
        """

        1. Make the batch file  to do the registry changes ,write to and add the  C# payload to startup and winlogin.exe. Restart computer and self destruct 
        batch 
        
        """
        
        






"""
  TODO
  -Check if the user has been infected before by checking registry keys, files which are dropped by the c#/python/asm/batch payload
  -if they have not been infected,  Do registry stuff with batch. eg. write the main payload bytes and add  to startup, disabling UAC, etc...., common stuff
  -delete the python file because it is not needed anymore
"""








