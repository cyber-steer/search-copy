# import tkinter as tk
# from tkinter import filedialog
#
# def get_directory_path():
#     path = filedialog.askdirectory()
#     entry_var.set(path)
#
# # Tkinter 윈도우 생성
# root = tk.Tk()
# root.title("윈도우 경로 입력")
#
# # 라벨과 엔트리 위젯 생성
# label = tk.Label(root, text="경로:")
# label.pack(pady=10)
#
# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvariable=entry_var, width=50)
# entry.pack(pady=10)
#
# # 버튼 생성 및 클릭 시 경로 입력 함수 호출
# button = tk.Button(root, text="경로 선택", command=get_directory_path)
# button.pack(pady=10)
#
# # 윈도우 실행
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog
#
# def get_directory_path():
#     path = filedialog.askdirectory()
#     entry_var.set(path)
#
# # Tkinter 윈도우 생성
# root = tk.Tk()
# root.title("좌우로 나눠진 윈도우")
#
# # 좌측 프레임 생성
# left_frame = tk.Frame(root)
# left_frame.pack(side=tk.LEFT, padx=10, pady=10)
#
# # 라벨과 엔트리 위젯을 좌측 프레임에 배치
# label = tk.Label(left_frame, text="경로:")
# label.pack(side=tk.TOP)
#
# entry_var = tk.StringVar()
# entry = tk.Entry(left_frame, textvariable=entry_var, width=30)
# entry.pack(side=tk.TOP)
#
# # 우측에 Separator 추가
# separator = ttk.Separator(root, orient="vertical")
# separator.pack(side=tk.LEFT, fill="y", padx=5)
#
# # 우측 프레임 생성
# right_frame = tk.Frame(root)
# right_frame.pack(side=tk.LEFT, padx=10, pady=10)
#
# # 버튼을 우측 프레임에 배치
# button = tk.Button(right_frame, text="경로 선택", command=get_directory_path)
# button.pack(side=tk.TOP)
#
# # 윈도우 실행
# root.mainloop()


# import tkinter as tk
#
# def toggle_hidden_frame():
#     if hidden_frame.winfo_ismapped():  # 이미 보여지고 있다면 숨김
#         hidden_frame.pack_forget()
#     else:
#         hidden_frame.pack(expand=True, ipadx=10, ipady=10)
#
# window = tk.Tk()
# window.title("숨겨진 요소 보이기")
#
# # 숨겨진 프레임 생성
# hidden_frame = tk.Frame(window, bg="yellow")
# hidden_frame.pack_forget()  # 초기에는 숨겨진 상태로 설정
#
# # 보이기/숨기기 버튼
# toggle_button = tk.Button(window, text="숨겨진 요소 보이기/숨기기", command=toggle_hidden_frame)
# toggle_button.pack(pady=10)
#
# window.mainloop()



import tkinter as tk
from tkinter import Checkbutton, LabelFrame, IntVar, Label

root = tk.Tk()
root.geometry('800x600')

def toggle():
    # 모든 체크박스의 상태를 master 체크박스와 동일하게 설정
    for var in vars:
        var.set(master_var.get())

def toggle_frame(event):
    # 라벨 선택 시 숨겨진 항목 표시
    frame = event.widget.master
    if frame.winfo_height() == 20:
        frame.configure(height=100)
    else:
        frame.configure(height=20)

# 오른쪽 창
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# 체크박스가 있는 Labelframe 네 개
master_var = IntVar()
master_cb = Checkbutton(right_frame, text="모두 선택", variable=master_var, command=toggle)
master_cb.pack()

vars = []
for _ in range(4):
    frame = LabelFrame(right_frame, height=20)
    frame.pack(fill=tk.X, padx=5, pady=5)
    label = Label(frame, text="클릭하여 펼치기")
    label.pack()
    label.bind("<Button-1>", toggle_frame)
    var = IntVar()
    vars.append(var)
    checkbox = Checkbutton(frame, variable=var)
    checkbox.pack(side=tk.LEFT)

root.mainloop()
