import pyautogui
import pyperclip
import webbrowser
from win10toast_click import ToastNotifier 
#position of buttons on the screen
smsButtonPositionX = 528#245
smsButtonPositionY = 515#372
btnnewMessageX =677
btnnewMessageY =831
#phone numbers field 
txtPhoneNumbersX =941
txtPhoneNumbersY =250
#send button position
btnSendX =1369
btnSendY =827
#message box field
msgFieldX =1055
msgFieldY =787


print("\033[92m WELCOME TO SMS AUTOMATISATION WITH AIRDROID .\033[0m")
print("\033[93m REMEMBER TO CHANGE POSITIONS ON THE SCRIPT IT DEPEND TO SCREEN THAT YOU ARE DISPLAYING FOR.\033[0m")
res=pyautogui.confirm(text='Steps to do befor execution the script \n -CHANGE POSITIONS VARIABLES ON THE SCRIPT IT DEPEND TO SCREEN THAT YOU ARE DISPLAYING FOR\n-OPEN AIRDOID APP \n-Please dont touch the mouse and the keyboard during automatisation excexution',
                     title='SMS AUTOMATISATION AIRDROID', buttons=['Execute','Cancel'])
toaster = ToastNotifier()
if(res=='Cancel'):
    print("\033[91m exit.\033[0m")

    exit()

toaster.show_toast(
"SMS AUTOMATISATION AIRDROID", 
"starting program", 
icon_path=None,
duration=5, #
threaded=True, 
callback_on_click='' 
)
print("\033[92mExecution.\033[0m")
#message to send
message ="hello from pyautogui"
#open airDroid app
pyautogui.press('win')
pyautogui.write('airdroid')
pyautogui.press('enter')
pyautogui.moveTo(smsButtonPositionX, smsButtonPositionY, duration=1)
pyautogui.click(
    button="left")

#get count of numbers
nbLines = len(open('data.txt', 'r').readlines())
#read
file = open('data.txt', 'r')
#iterat1,2,3,4,5,6,7
for indexLine in range(0, nbLines):
    #read line by line
    content = file.__next__()
    pyperclip.copy(content)
    #move to new message button
    pyautogui.moveTo(btnnewMessageX, btnnewMessageY, duration=0.5)
    pyautogui.click()
    #move to phone numbers field
    pyautogui.click(txtPhoneNumbersX, txtPhoneNumbersY,duration=0.2)
    pyautogui.press('backspace',presses=10,interval=0.2)
    pyperclip.copy(content)
    pyautogui.click(duration=0.2)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    #move to message field
    pyautogui.moveTo(msgFieldX, msgFieldY, duration=1)
    pyautogui.click(duration=0.2)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    #past message to send
    pyperclip.copy(message)
    pyautogui.click(duration=0.2)
    pyautogui.hotkey('ctrl','v')
    #click on send button
    pyautogui.moveTo(btnSendX, btnSendY, duration=0.5)
    pyautogui.click()

print("\033[92mFinish .\033[0m")
toaster.show_toast(
"SMS AUTOMATISATION AIRDROID", 
"end executing script", 
icon_path=None,
duration=5, #
threaded=True, 
callback_on_click='' 
)