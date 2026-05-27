from tkinter import *

class Counter:
   

    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1
        
        
    def decrement(self):
        self.value -= 1
       
        
    def reset(self):
        self.value = 0


pasta_counter = Counter()      # !
oat_counter = Counter()
banana_counter = Counter()
isp_counter = Counter()


def update_label():
    carb = pasta_counter.value * 7.5 + oat_counter.value * 3.3 + banana_counter.value * 23.0 + isp_counter.value * 1.0
    protein = pasta_counter.value * 1.2 + oat_counter.value * 0.7 + banana_counter.value * 1.0 + isp_counter.value * 17.0
    fat = pasta_counter.value * 0.15 + oat_counter.value * 0.3 + banana_counter.value * 0.3 + isp_counter.value * 1.0
    
    label.config(text=f'탄수:{carb}g, 단백질:{protein}g, 지방:{fat}g / 파스타:{pasta_counter.value * 10}g, 오트:{oat_counter.value * 5}g, 바나나:{banana_counter.value}개, 보충제:{isp_counter.value}스쿱')
    
def on_plus_pasta():
    pasta_counter.increment()
    update_label()

def on_minus_pasta():
    pasta_counter.decrement()
    update_label()

def on_plus_oat():
    oat_counter.increment()
    update_label()

def on_minus_oat():
    oat_counter.decrement()
    update_label()

def on_plus_banana():
    banana_counter.increment()
    update_label()

def on_minus_banana():
    banana_counter.decrement()
    update_label()

def on_plus_isp():
    isp_counter.increment()
    update_label()

def on_minus_isp():
    isp_counter.decrement()
    update_label()

def on_reset():
    pasta_counter.reset()
    oat_counter.reset()
    banana_counter.reset()
    isp_counter.reset()
    update_label()
    
window = Tk()
window.title("식단 탄단지 계산")
window.geometry("1000x400")

label = Label(window, text="", font=("맑은 고딕", 14))
label.pack(pady=10)

btn_plus_pasta = Button(window, text="파스타 +10g", width=12, command=on_plus_pasta)
btn_minus_pasta = Button(window, text="파스타 -10g", width=12, command=on_minus_pasta)

btn_plus_oat = Button(window, text="오트 +5g", width=12, command=on_plus_oat)
btn_minus_oat = Button(window, text="오트 -5g", width=12, command=on_minus_oat)

btn_plus_banana = Button(window, text="바나나 +1개", width=12, command=on_plus_banana)
btn_minus_banana = Button(window, text="바나나 -1개", width=12, command=on_minus_banana)

btn_plus_ISP = Button(window, text="보충제 +1스쿱", width=12, command=on_plus_isp)
btn_minus_ISP = Button(window, text="보충제 -1스쿱", width=12, command=on_minus_isp)

btn_reset = Button(window, text="Reset", width=12, command=on_reset)





btn_plus_pasta.pack(side=LEFT, padx=10, pady=10)
btn_minus_pasta.pack(side=LEFT, padx=10, pady=10)

btn_plus_oat.pack(side=LEFT, padx=10, pady=10)
btn_minus_oat.pack(side=LEFT, padx=10, pady=10)

btn_plus_banana.pack(side=LEFT, padx=10, pady=10)
btn_minus_banana.pack(side=LEFT, padx=10, pady=10)

btn_plus_ISP.pack(side=LEFT, padx=10, pady=10)
btn_minus_ISP.pack(side=LEFT, padx=10, pady=10)

btn_reset.pack(side=LEFT, padx=10, pady=10)




window.mainloop()
