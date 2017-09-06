from guizero import App, PushButton, TextBox

def do_staff():
    print("Hi")

def do_other_staff():
    print("Hi as well")

app = App("Lots of buttons")

button1 = PushButton(app, text="Button 1", command=do_staff)
button2 = PushButton(app, text="Button 2", command=do_other_staff)

app.display()