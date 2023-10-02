import pyautogui


# open airDroid app
# smsButtonPositionX = 245
# smsButtonPositionY = 372

# pyautogui.press('win')
# pyautogui.write('airdroid')
# pyautogui.press('enter')

# pyautogui.moveTo(smsButtonPositionX, smsButtonPositionY, duration=0.5)
# pyautogui.click(
#     button="left")


nbLines = len(open('data.txt', 'r').readlines())
file = open('data.txt', 'r')
for indexLine in range(1, nbLines):
    content = file.__next__()
    print(content)
