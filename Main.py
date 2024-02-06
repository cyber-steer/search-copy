import json
import tkinter as tk
from tkinter import scrolledtext, LabelFrame, ttk, filedialog

with open('extension.json', 'r') as f:
    checkbox_labels = json.load(f)
checkbox_vars = {}
# 체크박스 상태를 저장하는 변수들을 담을 리스트
for key in checkbox_labels.keys():
    checkbox_vars[key] = []
# checkbox_labels = {"video": ["mp4", "mkv", "avi", "mov"], "image": ["png", "jpg", "gif"], "audio": ["mp3", "wav"]}


def on_mousewheel(event):
    # 마우스 휠 이벤트 처리
    if canvas.winfo_height() < inner_frame.winfo_reqheight():
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def on_configure(event):
    # 내부 Frame의 크기가 변경될 때 스크롤 영역 조정
    canvas.configure(scrollregion=canvas.bbox("all"))


def toggle_frame(frame_content):
    if frame_content.winfo_ismapped():
        frame_content.pack_forget()
    else:
        frame_content.pack(expand=True, fill='both')
        frame_content.pack_propagate(False)
def update_group_checkboxes(group_var, checkboxes):
    group_state = group_var.get()
    for checkbox in checkboxes:
        checkbox.set(group_state)
def create_accordion(parent, text):
    window = tk.Frame(parent, borderwidth=1, relief="solid", width=1000)
    window.pack(expand=True, fill='x', padx=10, pady=10)
    window.bind("<MouseWheel>", on_mousewheel)
    # window.pack_propagate(False)
    header_frame = tk.Frame(window, borderwidth=1, relief="solid")
    header_frame.pack(expand=True, fill='x')
    header_frame.bind("<MouseWheel>", on_mousewheel)


    frame_content = tk.Frame(window, borderwidth=1, relief="solid")
    frame_content.pack(expand=True, fill='both')
    frame_content.pack_propagate(False)  # frame_content의 내용에 따라 크기가 조절되지 않도록 설정
    frame_content.bind("<MouseWheel>", on_mousewheel)

    # 체크박스 상태를 저장하는 IntVar 생성
    group_var = tk.IntVar()
    checkbox_vars[text] = [tk.IntVar() for _ in checkbox_labels[text]]

    header_checkbox = tk.Checkbutton(header_frame, text=text, variable=group_var,
                                     command=lambda: update_group_checkboxes(group_var, checkbox_vars[text]))
    header_checkbox.grid(row=0, column=0)  # 체크박스를 먼저 배치
    header_checkbox.bind("<MouseWheel>", on_mousewheel)
    #
    toggle_button = tk.Button(header_frame, text="Toggle", command=lambda: toggle_frame(frame_content))
    toggle_button.grid(row=0, column=1)  # 토글 버튼을 체크박스 뒤에 배치
    toggle_button.bind("<MouseWheel>", on_mousewheel)


    # # 체크박스를 생성하고 frame_content에 배치
    # for i, label in enumerate(checkbox_labels[text]):
    #     checkbox = tk.Checkbutton(frame_content, text=label, variable=checkbox_vars[text][i], width=5)
    #     checkbox.grid(row=0, column=i)  # 체크박스를 가로로 배치
    #     checkbox.pack_propagate(False)

    num_columns = 6
    for i, label in enumerate(checkbox_labels[text]):
        row = i // num_columns
        col = i % num_columns
        checkbox = tk.Checkbutton(frame_content, text=label, variable=checkbox_vars[text][i], width=5, borderwidth=1, relief="solid")
        checkbox.grid(row=row, column=col, padx=5, pady=5, sticky="w")  # padx, pady 값으로 간격 조절

        # 추가 설정
        checkbox.pack_propagate(False)
        checkbox.bind("<MouseWheel>", on_mousewheel)

        frame_content.pack_forget()


def get_directory_path(entry_var):
    path = filedialog.askdirectory()
    entry_var.set(path)


width = 1000
height = 600
window = tk.Tk()
window.geometry(f'{width}x{height}')

# 왼쪽 창
left_frame = tk.Frame(window, width=width // 2, height=height)
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
left_frame.pack_propagate(0)
# left_frame.grid(row=0, column=0)


search_path_var = tk.StringVar()
copy_path_var = tk.StringVar()
for text, entry_var in [("검색 경로", search_path_var), ("복사 경로", copy_path_var)]:
    labelframe = LabelFrame(left_frame, text=text)
    labelframe.pack(fill=tk.X, padx=20, pady=5, ipadx=10, ipady=10)
    entry = tk.Entry(labelframe, textvariable=entry_var)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
    button = tk.Button(labelframe, text="browse...", command=lambda var=entry_var: get_directory_path(var))
    button.pack(side=tk.LEFT, padx=10)

# Log 창
log_text = scrolledtext.ScrolledText(left_frame, wrap="none", width=1, height=1)
log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

separator_frame = ttk.Frame(window, width=2, relief="groove")
separator_frame.pack(side=tk.LEFT, fill="y")

# separator.grid(row=0, column=1)
# Text, Button, Loading Bar, Button
search_frame = tk.Frame(left_frame)
search_frame.pack(fill=tk.BOTH, expand=True)

text = tk.Entry(left_frame)
text.pack(fill=tk.X, padx=5, pady=5)
button1 = tk.Button(left_frame, text="Button")
button1.pack(fill=tk.X, padx=5, pady=5)
loading_bar = ttk.Progressbar(left_frame, mode='indeterminate')
loading_bar.pack(fill=tk.X, padx=5, pady=5)
button2 = tk.Button(left_frame, text="Button")
button2.pack(fill=tk.X, padx=5, pady=5)

def on_inner_frame_mousewheel(event):
    inner_frame.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")  # canvas에 전달


# 오른쪽 창
right_frame = tk.Frame(window, width=width // 2, height=height)
right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# 수직 스크롤바 생성
scrollbar = tk.Scrollbar(right_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Canvas 생성
canvas = tk.Canvas(right_frame, yscrollcommand=scrollbar.set, width=width / 2)
canvas.pack(side="left", fill="both", expand=True)

# 수직 스크롤바와 Canvas 연결
scrollbar.config(command=canvas.yview)

# Frame 생성 (Canvas의 내용을 담는 역할)
inner_frame = ttk.Frame(canvas, borderwidth=1, relief="solid")

# Place the inner_frame inside the Canvas
canvas.create_window((0, 0), window=inner_frame, anchor="nw", width=width / 2-20)

# inner_frame에서의 마우스 휠 이벤트 바인딩
inner_frame.bind("<MouseWheel>", on_mousewheel)

# Canvas 위에서의 마우스 휠 이벤트 바인딩
canvas.bind("<MouseWheel>", on_mousewheel)

inner_frame.bind("<Configure>", on_configure)

# inner_frame에 내용 추가
for key, val in checkbox_labels.items():
    create_accordion(inner_frame, key)

window.mainloop()
