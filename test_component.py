import json

with open('extension.json', 'r') as f:
    checkbox_labels = json.load(f)
checkbox_vars = {}
# 체크박스 상태를 저장하는 변수들을 담을 리스트
for key in checkbox_labels.keys():
    checkbox_vars[key] = []
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







# import tkinter as tk
#
# def toggle_frame(frame_content):
#     if frame_content.winfo_ismapped():
#         frame_content.pack_forget()
#     else:
#         frame_content.pack(expand=True, fill='both')
# def update_group_checkboxes(group_var, checkboxes):
#     group_state = group_var.get()
#     for checkbox in checkboxes:
#         checkbox.set(group_state)
# root = tk.Tk()
# root.title("Accordion Example")
#
# # 체크박스 상태를 저장하는 변수들을 담을 리스트
# checkbox_vars = {"video": [], "image": [], "audio": []}
# checkbox_labels = {"video": ["mp4", "mkv", "avi", "mov"], "image": ["png", "jpg", "gif"], "audio": ["mp3", "wav"]}
#
# def create_accordion(parent, text):
#     window = tk.Frame(parent)
#     window.pack(expand=True, fill='both', padx=10, pady=10)
#     header_frame = tk.Frame(window, borderwidth=1, relief="solid")
#     header_frame.pack(expand=True, fill='both')
#
#     toggle_button = tk.Button(header_frame, text="Toggle", command=lambda: toggle_frame(frame_content))
#     toggle_button.pack()
#
#     frame_content = tk.Frame(window, borderwidth=1, relief="solid")
#     frame_content.pack(expand=True, fill='both')
#
#     # 체크박스 상태를 저장하는 IntVar 생성
#     group_var = tk.IntVar()
#     checkbox_vars[text] = [tk.IntVar() for _ in checkbox_labels[text]]
#
#     checkbox_vars[text] = [tk.IntVar() for _ in checkbox_labels[text]]
#
#     header_checkbox = tk.Checkbutton(header_frame, text=text, variable=group_var,
#                                      command=lambda: update_group_checkboxes(group_var, checkbox_vars[text]))
#     header_checkbox.pack()
#     # 체크박스를 생성하고 frame_content에 배치
#     for i, label in enumerate(checkbox_labels[text]):
#         checkbox = tk.Checkbutton(frame_content, text=label, variable=checkbox_vars[text][i])
#         checkbox.pack()
#
#
# for key, val in checkbox_labels.items():
#     create_accordion(root, key)
#
# # 체크박스 상태를 확인하는 버튼 생성
# def check_checkbox_state():
#     for key, var_list in checkbox_vars.items():
#         print(f"{key.capitalize()} checkboxes:")
#         for i, checkbox_var in enumerate(var_list):
#             print(f"  {checkbox_labels[key][i]}: {checkbox_var.get()}")
#
# check_button = tk.Button(root, text="Check Checkbox State", command=check_checkbox_state)
# check_button.pack()
#
# root.mainloop()




# import tkinter as tk
# from tkinter import ttk
#
# def on_mousewheel(event):
#     # 마우스 휠 이벤트 처리
#     if canvas.winfo_height() < inner_frame.winfo_reqheight():
#         canvas.yview_scroll(int(-1*(event.delta/120)), "units")
#
# def on_configure(event):
#     # 내부 Frame의 크기가 변경될 때 스크롤 영역 조정
#     canvas.configure(scrollregion=canvas.bbox("all"))
#
# window = tk.Tk()
# window.title("Scrollable Frame Example")
# window.geometry("800x600")
#
# # 수직 스크롤바 생성
# vsb = tk.Scrollbar(window, orient="vertical")
# vsb.pack(side="right", fill="y")
#
# # 수평 스크롤바 생성
# hsb = tk.Scrollbar(window, orient="horizontal")
# hsb.pack(side="bottom", fill="x")
#
# # Canvas 생성
# canvas = tk.Canvas(window, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
# canvas.pack(side="left", fill="both", expand=True)
#
# # 수직 스크롤바와 Canvas 연결
# vsb.config(command=canvas.yview)
#
# # 수평 스크롤바와 Canvas 연결
# hsb.config(command=canvas.xview)
#
# # 마우스 휠 이벤트 바인딩
# canvas.bind_all("<MouseWheel>", on_mousewheel)
#
# # Frame 생성 (Canvas의 내용을 담는 역할)
# inner_frame = ttk.Frame(canvas)
# canvas.create_window((0, 0), window=inner_frame, anchor="nw")
#
# # 내부 Frame에 위젯들 추가
# for i in range(30):
#     label = ttk.Label(inner_frame, text=f"Label {i}")
#     label.pack()
#
# # 내부 Frame의 크기가 변경될 때 스크롤 영역 조정
# inner_frame.bind("<Configure>", on_configure)
#
# # Canvas의 스크롤 영역 설정
# canvas.configure(scrollregion=canvas.bbox("all"))
#
# window.mainloop()




# import tkinter as tk
# from tkinter import ttk
#
# width = 800
# height = 600
#
# window = tk.Tk()
# window.geometry(f'{width}x{height}')
#
# # 왼쪽 창
# left_frame = tk.Frame(window, width=width // 2, height=height)
# left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
#
# # 수직 선
# separator_frame = ttk.Frame(window, width=2, relief="groove")
# separator_frame.pack(side=tk.LEFT, fill="y")
#
# # 오른쪽 창
# right_frame = tk.Frame(window, width=width // 2, height=height)
# right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
#
# window.mainloop()




# import tkinter as tk
# from tkinter import ttk
#
# def create_loading_bar_frame(parent):
#     frame = tk.Frame(parent)
#     loading_bar = ttk.Progressbar(frame, mode='indeterminate')
#     loading_bar.pack(side=tk.LEFT, padx=5, pady=5)
#     return frame
#
# width = 1000
# height = 600
#
# window = tk.Tk()
# window.geometry(f'{width}x{height}')
#
# # 좌측 상단
# top_left_frame = tk.Frame(window, width=width // 2, height=height // 2)
# top_left_frame.pack(side=tk.LEFT, anchor=tk.NW)
#
# # '?' 텍스트 표시
# question_label = tk.Label(top_left_frame, text="?/?")
# question_label.pack(side=tk.LEFT, padx=5, pady=5)
#
# # 우측 상단
# top_right_frame = tk.Frame(window, width=width // 2, height=height // 2)
# top_right_frame.pack(side=tk.RIGHT, anchor=tk.NE)
#
# # 버튼 추가
# button_top_right = tk.Button(top_right_frame, text="Button")
# button_top_right.pack(side=tk.RIGHT, padx=5, pady=5)
#
# # 좌측 하단
# bottom_left_frame = tk.Frame(window, width=width // 2, height=height // 2)
# bottom_left_frame.pack(side=tk.LEFT, anchor=tk.SW)
#
# # 로딩바 추가
# loading_bar_frame_bottom_left = create_loading_bar_frame(bottom_left_frame)
#
# # 우측 하단
# bottom_right_frame = tk.Frame(window, width=width // 2, height=height // 2)
# bottom_right_frame.pack(side=tk.RIGHT, anchor=tk.SE)
#
# # 로딩바 추가
# loading_bar_frame_bottom_right = create_loading_bar_frame(bottom_right_frame)
#
# # 버튼 추가
# button_bottom_right = tk.Button(bottom_right_frame, text="Button")
# button_bottom_right.pack(side=tk.RIGHT, padx=5, pady=5)
#
# window.mainloop()
