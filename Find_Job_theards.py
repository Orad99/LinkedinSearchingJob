# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font as tkFont
import Linkedin_bot as lb



def close_app():
    window.destroy()
    
def run_app():
    username_search = str(username_entry.get())
    password_search = str(password_entry.get())
    job_search = str(job_entry.get())
    filename_search = str(filename_entry.get())
    
    lb.Search_job(username_search, password_search, filename_search)
   

    

window = tk.Tk()



window.title("JobFounder")
frame_header = tk.Frame(master = window, borderwidth = 2, pady = 2)
center_frame = tk.Frame(window, borderwidth = 2, pady = 5)
bottom_frame = tk.Frame(window, borderwidth = 2, pady = 5)



frame_header.grid(row = 0, column = 0)
center_frame.grid(row = 1, column = 0)
bottom_frame.grid(row = 2, column = 0)

header = tk.Label(frame_header, text = "Let's find your next job!", bg = '#0ED3FF', fg = '#415559', height = "3", width = "50",font = ('Calibri bold',18))
header.grid(row = 0, column = 0)




frame_main1 = tk.Frame(center_frame, borderwidth = 2,relief = "sunken" )
frame_main2 = tk.Frame(center_frame, borderwidth = 2,relief = "sunken" )
frame_main3 = tk.Frame(center_frame, borderwidth = 2,relief = "sunken" )
frame_main4 = tk.Frame(center_frame, borderwidth = 2,relief = "sunken" )


username = tk.Label(frame_main1, text = "Email:")
password = tk.Label(frame_main2, text = "Password:")
filename = tk.Label(frame_main3, text = "where to save?")
job = tk.Label(frame_main4, text = "specific job?")



username_1 = tk.StringVar()
password_1 = tk.StringVar()
filename_1 = tk.StringVar()
job_1 = tk.StringVar()


username_entry = tk.Entry(frame_main1, textvariable = username_1, width = 29)
password_entry = tk.Entry(frame_main2, textvariable = password_1, width = 26, show = "•")
filename_entry = tk.Entry(frame_main3, textvariable = filename_1, width = 24)
job_entry = tk.Entry(frame_main4, textvariable = job_1, width = 20)



button_run = tk.Button(bottom_frame,text = "Search", command = run_app, bg = "#4BF629", fg = "white", relief = "raised", width = 10, font = ("Helvetica 10 bold"))
button_run.grid(column = 0, row = 0, padx = 100, pady = 2)

button_close = tk.Button(bottom_frame,text = "Exit", command = close_app, bg = "#F62929", fg = "white", relief = "raised", width = 10, font = ("Helvetica 10 bold"))
button_close.grid(column = 1, row = 0, padx = 100, pady = 2)

frame_main1.pack(fill = 'x', pady='2')
frame_main2.pack(fill = 'x', pady='2')
frame_main3.pack(fill = 'x', pady='2')
username.pack(side = "left",padx = 7)
username_entry.pack(side = "left", padx = 27)
password.pack(side = "left",padx = 7)
password_entry.pack(side = "left", padx = 24)
filename.pack(side = "left",padx = 7)
filename_entry.pack(side = "left", padx = 13)
job.pack(side = "left",padx = 7)
job_entry.pack(side = "left", padx = 1)



window.mainloop()

