import json
import tkinter as tk
from tkinter import scrolledtext, LabelFrame, ttk, filedialog, ttk

class GUI_component:
    def __init__(self, extension_path, width=1000, height=600):
        self.width = width
        self.height = height
        self.search_path_var = None
        self.copy_path_var = None
        self.checkbox_labels = self.get_extension(extension_path)
        self.checkbox_vars = self.get_extension_labels(self.checkbox_labels)


        self.window = tk.Tk()
        self.window.title("검색 및 복사")
        self.window.geometry(f'{width}x{height}')

        self.left_component()
        separator_frame = ttk.Frame(self.window, width=2, relief="groove")
        separator_frame.pack(side=tk.LEFT, fill="y")
        self.right_component()

        self.window.mainloop()

    def left_component(self):
        left_frame = tk.Frame(self.window, width=self.width // 2, height=self.height)
        left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        left_frame.pack_propagate(0)

        self.search_path_var = tk.StringVar()
        self.copy_path_var = tk.StringVar()
        for text, entry_var in [("검색 경로", self.search_path_var), ("복사 경로", self.copy_path_var)]:
            labelframe = LabelFrame(left_frame, text=text)
            labelframe.pack(fill=tk.X, padx=20, pady=5, ipadx=10, ipady=10)
            entry = tk.Entry(labelframe, textvariable=entry_var)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
            button = tk.Button(labelframe, text="browse...", command=lambda var=entry_var: self.get_directory_path(var))
            button.pack(side=tk.LEFT, padx=10)

        log_frame = tk.Frame(left_frame, height=self.height-250)
        log_frame.pack_propagate(0)
        log_frame.pack(fill="both")
        log_text = scrolledtext.ScrolledText(log_frame, wrap="none", width=1)
        log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        result_frame = tk.Frame(left_frame)
        result_frame.pack(side="bottom", fill=tk.BOTH, expand=True)
        search_frame = tk.Frame(result_frame)
        search_frame.pack(fill="x")
        copy_frame = tk.Frame(result_frame)
        copy_frame.pack(fill="x", pady=10)

        count_label = tk.Label(search_frame, text=" / ")
        count_label.pack(side="left", fill=tk.BOTH, padx=5, pady=5)
        search_button = tk.Button(search_frame, text="검색")
        search_button.pack(side="right", fill=tk.BOTH, padx=5, pady=5, ipadx=10, ipady=5)

        loading_bar = ttk.Progressbar(copy_frame, mode='indeterminate')
        loading_bar.pack(side="left", fill=tk.X, expand=True, padx=5, pady=5)
        copy_button = tk.Button(copy_frame, text="복사")
        copy_button.pack(side="right", fill=tk.BOTH, padx=5, pady=5, ipadx=10, ipady=5)

    def right_component(self):

        # 오른쪽 창
        right_frame = tk.Frame(self.window, width=self.width // 2, height=self.height)
        right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # 수직 스크롤바 생성
        scrollbar = tk.Scrollbar(right_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        search_extension_frame = tk.Frame(right_frame)
        search_extension_frame.pack(fill="x")
        search_extension_label = tk.Label(search_extension_frame, text="추가 지정( , ):")
        search_extension_label.pack(side="left", fill="both")
        search_extension_entry = tk.Entry(search_extension_frame)
        search_extension_entry.pack(side="left", fill="both", expand=True, padx=(5,10))

        # Canvas 생성
        self.canvas = tk.Canvas(right_frame, yscrollcommand=scrollbar.set, width=self.width / 2)
        self.canvas.pack(side="left", fill="both", expand=True)

        # 수직 스크롤바와 Canvas 연결
        scrollbar.config(command=self.canvas.yview)

        # Frame 생성 (Canvas의 내용을 담는 역할)
        self.inner_frame = ttk.Frame(self.canvas)

        # Place the inner_frame inside the Canvas
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw", width=self.width / 2 - 20)

        # inner_frame에서의 마우스 휠 이벤트 바인딩
        self.inner_frame.bind("<MouseWheel>", self.on_mousewheel)

        # Canvas 위에서의 마우스 휠 이벤트 바인딩
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

        self.inner_frame.bind("<Configure>", self.on_configure)

        # inner_frame에 내용 추가
        for key, val in self.checkbox_labels.items():
            self.create_accordion(self.inner_frame, key)

#========================================================================================
    def get_extension_labels(self, data):
        labels = {}
        for key in data.keys():
            labels[key] = []
        return labels
    def get_extension(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_directory_path(self, entry_var):
        path = filedialog.askdirectory()
        entry_var.set(path)
    def on_mousewheel(self, event):
        # 마우스 휠 이벤트 처리
        if self.canvas.winfo_height() < self.inner_frame.winfo_reqheight():
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_configure(self, event):
        # 내부 Frame의 크기가 변경될 때 스크롤 영역 조정
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def toggle_frame(self, frame_content, toggle_button):
        if frame_content.winfo_ismapped():
            frame_content.pack_forget()
            toggle_button["text"] = "펼침"
        else:
            frame_content.pack(expand=True, fill='both')
            frame_content.pack_propagate(False)
            toggle_button["text"] = "접기"
    def update_group_checkboxes(self, group_var, checkboxes):
        group_state = group_var.get()
        for checkbox in checkboxes:
            checkbox.set(group_state)

    def create_accordion(self, parent, text):
        window = tk.Frame(parent)
        window.pack(expand=True, fill='x', padx=10, pady=10)
        window.bind("<MouseWheel>", self.on_mousewheel)
        # window.pack_propagate(False)
        header_frame = tk.Frame(window, borderwidth=1, relief="solid")
        header_frame.pack(expand=True, fill='x', ipadx=10, ipady=5)
        header_frame.bind("<MouseWheel>", self.on_mousewheel)

        frame_content = tk.Frame(window, borderwidth=1, relief="solid")
        frame_content.pack(expand=True, fill='both')
        frame_content.pack_propagate(False)  # frame_content의 내용에 따라 크기가 조절되지 않도록 설정
        frame_content.bind("<MouseWheel>", self.on_mousewheel)

        # 체크박스 상태를 저장하는 IntVar 생성
        group_var = tk.IntVar()
        self.checkbox_vars[text] = [tk.IntVar() for _ in self.checkbox_labels[text]]

        header_checkbox = tk.Checkbutton(header_frame, text=text, variable=group_var,
                                         command=lambda: self.update_group_checkboxes(group_var, self.checkbox_vars[text]))
        header_checkbox.pack(side="left")  # 체크박스를 먼저 배치
        header_checkbox.bind("<MouseWheel>", self.on_mousewheel)
        #
        toggle_button = tk.Button(header_frame, text="펼침", command=lambda: self.toggle_frame(frame_content, toggle_button))
        toggle_button.pack(side="right", padx=10, ipadx=10, ipady=5)  # 토글 버튼을 체크박스 뒤에 배치
        toggle_button.bind("<MouseWheel>", self.on_mousewheel)

        num_columns = 6
        for i, label in enumerate(self.checkbox_labels[text]):
            row = i // num_columns
            col = i % num_columns
            checkbox = tk.Checkbutton(frame_content, text=label, variable=self.checkbox_vars[text][i], width=5,)
            checkbox.grid(row=row, column=col, padx=5, pady=5, sticky="w")  # padx, pady 값으로 간격 조절

            # 추가 설정
            checkbox.pack_propagate(False)
            checkbox.bind("<MouseWheel>", self.on_mousewheel)

            frame_content.pack_forget()


if __name__ == "__main__":
    app = GUI_component("extension.json", 1000, 800)
