import tkinter as tk
import tkinter.messagebox as msg
import math

#팩토리얼 계산함수
def cal():
    try:
        num = int(inputnum.get())
        if num <= -1:
            return positive()

        elif num >= 38:
            return maxnumerror()
            
        else:
            result = math.factorial(num)
            print('{:,}'.format(result))
            Resulttext.configure(text = '{:,}'.format(result))

    except ValueError:
        return error()

#에러
def error():
    msg.showerror("오류","수를 입력해주세요.")

def maxnumerror():
    msg.showwarning("최댓값 초과", "37 이하의 숫자를 입력해주세요.")

def positive():
    msg.showwarning("양수" , "양수를 입력해주세요")

#기본설정
window= tk.Tk()
window.title("팩토리얼 계산기")
window.geometry("400x250")
window.resizable(False,False)

#라벨
title = tk.Label(window, text = "아래에 계산할 수를 넣은후 계산하기 버튼을 눌러주세요.")
title.pack()

#입력창
inputnum = tk.Entry(window, width= 40)
inputnum.pack(pady=20)


Resulttext =tk.Label(window, bg= "white",width=50, height=5, text="결과")
Resulttext.pack()

#팩토리얼 버튼
check = tk.Button(
        window, 
        width=20, 
        height=3, 
        fg= "black", 
        bg="white" , 
        command = cal,
        text="계산하기.")


check.pack(side="bottom")

window.mainloop()