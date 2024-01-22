import tkinter as tk
from tkinter import scrolledtext, LabelFrame, ttk, filedialog


def get_directory_path(entry_var):
    path = filedialog.askdirectory()
    entry_var.set(path)

window = tk.Tk()
window.geometry('800x600')

# 왼쪽 창
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

separator = ttk.Separator(window, orient="vertical")
separator.pack(side=tk.LEFT, fill="y", padx=10)

# Entry와 Button이 있는 Labelframe 두 개

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
log_text = scrolledtext.ScrolledText(left_frame)
log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Text, Button, Loading Bar, Button
text = tk.Entry(left_frame)
text.pack(fill=tk.X, padx=5, pady=5)
button1 = tk.Button(left_frame, text="Button")
button1.pack(fill=tk.X, padx=5, pady=5)
loading_bar = ttk.Progressbar(left_frame, mode='indeterminate')
loading_bar.pack(fill=tk.X, padx=5, pady=5)
button2 = tk.Button(left_frame, text="Button")
button2.pack(fill=tk.X, padx=5, pady=5)

# 오른쪽 창
right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# 체크박스가 있는 Labelframe 네 개
check_title_frame = tk.Frame(window)
check_title_frame.pack()





window.mainloop()
