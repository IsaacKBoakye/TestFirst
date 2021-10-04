#This is  file to create GUI  to report  data for navigation

#This is  file to create GUI  to report  data for navigation

# 1-Import
import PySimpleGUI as sg

# 2- Layout

layout = [[sg.Text('Enter something: '), sg.Input(key='-IN-')],
         [sg.Text('Our output will go here', size=(30,1),key='-OUT-')],
         [sg.Button('OK'), sg.Button('Exit')]]

# 3- Window
window = sg.Window('Dash Board', layout)


# 4- Event
while True:
    event, values =window.read()
    if event=='Exit' or event==sg.WIN_CLOSED:
        break
window['-OUT-'].update(values['-IN-'])

#5-
window.close()

