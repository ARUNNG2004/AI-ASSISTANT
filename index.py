
#you must do this activity of the code
# pip install -r requirements.txt


from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text
import os

def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def ask():
    ask_val = spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n")
    if bot_val:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")

def execute_command(event):
    selected_command = commands_listbox.get(commands_listbox.curselection())
    entry1.delete(0, END)
    entry1.insert(0, selected_command)
    User_send()

root = Tk()
root.geometry("650x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
Text_label = Label(Main_frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), bg="#356696")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
try:
    image_path = os.path.join(os.path.dirname(__file__), "image/assitant.png")
    Display_Image = ImageTk.PhotoImage(Image.open(image_path))
    Image_Label = Label(Main_frame, image=Display_Image)
    Image_Label.grid(row=1, column=0, pady=20)
except FileNotFoundError:
    Image_Label = Label(Main_frame, text="Image not found", font=("comic Sans ms", 14, "bold"), bg="#356696")
    Image_Label.grid(row=1, column=0, pady=20)

# Add a text widget
text = Text(root, font=('Courier 10 bold'), bg="#356696")
text.grid(row=2, column=0, columnspan=2)
text.place(x=100, y=375, width=375, height=100)

# Add an entry widget
entry1 = Entry(root, justify=CENTER)
entry1.place(x=100, y=500, width=350, height=40)

# Add a send button
button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=User_send)
button2.place(x=350, y=575)

# Add a delete button
button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete_text)
button3.place(x=225, y=575)

# Add a listbox for commands
commands_frame = Frame(root, bg="#6F8FAF")
commands_frame.place(x=500, y=50, width=150, height=330)

commands_label = Label(commands_frame, text="Commands", font=("comic Sans ms", 14, "bold"), bg="#356696")
commands_label.pack(pady=10)

commands_listbox = Listbox(commands_frame, font=('Courier 14 bold'), bg="#356696", height=30)
commands_listbox.pack(padx=10, pady=10, fill=BOTH)
commands = [
    "1. YOUTUBE",
    "2. OPEN GOOGLE",
    "3. PLAY MUSIC",
    "4. TIME NOW",
    "5. GM",
    "6. TK",
    "7. HELLO",
    "8. WHAT IS YOUR NAME",
    "9. HOW ARE YOU",
    "10. QUIT"
]
for command in commands:
    commands_listbox.insert(END, command)

commands_listbox.bind('<<ListboxSelect>>', execute_command)

root.mainloop()
