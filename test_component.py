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



# import tkinter as tk
# from tkinter import Checkbutton, LabelFrame, IntVar, Label
#
# root = tk.Tk()
# root.geometry('800x600')
#
# def toggle():
#     # 모든 체크박스의 상태를 master 체크박스와 동일하게 설정
#     for var in vars:
#         var.set(master_var.get())
#
# def toggle_frame(event):
#     # 라벨 선택 시 숨겨진 항목 표시
#     frame = event.widget.master
#     if frame.winfo_height() == 20:
#         frame.configure(height=100)
#     else:
#         frame.configure(height=20)
#
# # 오른쪽 창
# right_frame = tk.Frame(root)
# right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
#
# # 체크박스가 있는 Labelframe 네 개
# master_var = IntVar()
# master_cb = Checkbutton(right_frame, text="모두 선택", variable=master_var, command=toggle)
# master_cb.pack()
#
# vars = []
# for _ in range(4):
#     frame = LabelFrame(right_frame, height=20)
#     frame.pack(fill=tk.X, padx=5, pady=5)
#     label = Label(frame, text="클릭하여 펼치기")
#     label.pack()
#     label.bind("<Button-1>", toggle_frame)
#     var = IntVar()
#     vars.append(var)
#     checkbox = Checkbutton(frame, variable=var)
#     checkbox.pack(side=tk.LEFT)
#
# root.mainloop()









# import tkinter as tk
#
# def toggle_frame(frame_content):
#     if frame_content.winfo_ismapped():
#         frame_content.pack_forget()
#     else:
#         frame_content.pack(expand=True, fill='both')
#
# root = tk.Tk()
# root.title("Accordion Example")
#
# def create_accordion_item(parent, text):
#     accordion_frame = tk.LabelFrame(parent, text=text, padx=10, pady=10)
#     accordion_frame.pack(expand=True, fill='both')
#
#     frame_content = tk.Frame(accordion_frame)  # 별도의 프레임을 생성
#     frame_content.pack(expand=True, fill='both')
#
#     tk.Label(frame_content, text=f"This is the {text.lower()} item's accordion body.").pack()
#
#     toggle_button = tk.Button(accordion_frame, text="Toggle", command=lambda: toggle_frame(frame_content))
#     toggle_button.pack()
#
# create_accordion_item(root, "Item #1")
# create_accordion_item(root, "Item #2")
# create_accordion_item(root, "Item #3")
#
# root.mainloop()







import tkinter as tk

def toggle_frame(frame_content, checkbox_var):
    if frame_content.winfo_ismapped():
        frame_content.pack_forget()
    else:
        frame_content.pack(expand=True, fill='both')

root = tk.Tk()
root.title("Accordion Example")

# 체크박스 상태를 저장하는 변수들을 담을 리스트
checkbox_vars = {"video": [], "image": [], "audio": []}
checkbox_labels = {"video": ["mp4", "mkv", "avi", "mov"], "image": ["png", "jpg", "gif"], "audio": ["mp3", "wav"]}

def create_accordion_item(parent, text):
    accordion_frame = tk.LabelFrame(parent, text=text, padx=10, pady=10)
    accordion_frame.pack(expand=True, fill='both')

    toggle_button = tk.Button(accordion_frame, text="Toggle", command=lambda: toggle_frame(frame_content, checkbox_vars))
    toggle_button.pack()
    frame_content = tk.Frame(accordion_frame)
    frame_content.pack(expand=True, fill='both')

    # 체크박스 상태를 저장하는 IntVar 생성
    checkbox_vars[text] = [tk.IntVar() for _ in checkbox_labels[text]]

    # 체크박스를 생성하고 frame_content에 배치
    for i, label in enumerate(checkbox_labels[text]):
        checkbox = tk.Checkbutton(frame_content, text=label, variable=checkbox_vars[text][i])
        checkbox.pack()
    # checkbox = tk.Checkbutton(frame_content, text=f"Include {text.lower()} item", variable=checkbox_var)
    # checkbox.pack()


# 3개의 아코디언 아이템 생성
# create_accordion_item(root, "Item #1")
# create_accordion_item(root, "Item #2")
# create_accordion_item(root, "Item #3")

for key, val in checkbox_labels.items():
    create_accordion_item(root, key)

# 체크박스 상태를 확인하는 버튼 생성
def check_checkbox_state():
    for i, checkbox_var in enumerate(checkbox_vars):
        print(f"Checkbox {i+1}: {checkbox_var.get()}")

check_button = tk.Button(root, text="Check Checkbox State", command=check_checkbox_state)
check_button.pack()

root.mainloop()
