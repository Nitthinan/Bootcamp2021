# GUITranslator.py

from tkinter import *
# จาก library ชื่อ tkinter, * คือ ให้ดึงความสามารถหลักมาทั้งหมด, GUI Package ใช้สำหรับการออกแบบ UI
from tkinter import ttk # ttk is theme of tk

# ---Google Translate---
from googletrans import Translator
translator = Translator() # ประกาศตัวแปรเพื่อสร้าง function สำหรับแปลภาษา

# ค่ำสั่งสร้างหน้าต่างหลัก
GUI = Tk()  
GUI.geometry('300x400') # กว้าง x สูง
GUI.title('Translator')

#---Config---
FONT = ('Angsana New', 15)
FONT2 = ('Angsana New',24)

#---Label---
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปลภาษา',font = FONT)
L.pack()

# ---Entry---(ช่องกรอกภาษา)---
v_vocab = StringVar() # กล่องสำหรับเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)

# B1=Button(GUI, text='Translate') # สร้างปุ่มธรรมดาสำหรับกด---Button---

# ---Button--- (ปุ่มแปลภาษา) ---
def Translate():
       vocab = v_vocab.get() # .get คือให้แสดงผลออกมา
       meaning = translator.translate(vocab,dest='th')
       print(vocab +' : '+meaning.text)
       v_result.set(vocab +' : '+meaning.text) # สั่งแสดงผลลัพธ์ (Show) ใน GUI
       
B1 = ttk.Button(GUI, text='Translate',command=Translate)
             # สร้างปุ่มสำหรับกดโดยใช้ theme จาก ttk
             # command=Translate (โปรแกรมปกติจะต้องพิมพ์คำสั่งต่อด้านบน) แต่ python พิมพ์ command.ใส่ชื่อฟังก์ชั่นเลย
B1.pack(ipadx=20,ipady=10,pady=20) # show ปุ่มขึ้นมาวางจากบนลงล่าง

#---Label---
L = ttk.Label(GUI,text='คำแปล',font = FONT)
L.pack()

#---Result---
v_result = StringVar()  # กล่องสำหรับบันทึกคำแปล
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2, foreground='green')
R1.pack()

GUI.mainloop () # ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด
