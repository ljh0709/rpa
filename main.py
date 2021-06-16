import pywinmacro as pw
import time


location1 = (191, 59)
location2 = (537, 315)
location3 = (339, 306)
location4 = (264, 303)

def newspaper():
    pw.click(location1)
    time.sleep(1)
    pw.type_in("https://www.naver.com")
    time.sleep(1)
    # 엔터키 입력
    pw.key_press_once("enter")
    time.sleep(1)
    pw.click(location2)
    time.sleep(3)
    pw.click(location3)
    time.sleep(3)
    pw.click(location4)


newspaper()

