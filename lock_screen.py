import tkinter as tk
from tkinter import font as tkfont

UNLOCK_CODE = "773"


def build_eye(canvas, width, height):
    canvas.create_oval(10, 10, width - 10, height - 10, fill="white", outline="black", width=2)
    canvas.create_oval(
        width * 0.35,
        height * 0.35,
        width * 0.65,
        height * 0.65,
        fill="black",
        outline="black",
    )


def main():
    root = tk.Tk()
    root.title("Lock Screen")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg="black")

    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.bind_all("<Key>", lambda _event: "break")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    message_frame = tk.Frame(root, bg="black")
    message_frame.pack(expand=True, fill="both")

    message_label = tk.Label(
        message_frame,
        text="вас заметили",
        fg="white",
        bg="black",
        font=("Helvetica", 48, "bold"),
    )
    message_label.pack(pady=(60, 20))

    eye_canvas = tk.Canvas(
        message_frame,
        width=300,
        height=140,
        bg="black",
        highlightthickness=0,
    )
    eye_canvas.pack()
    build_eye(eye_canvas, 300, 140)

    keypad_frame = tk.Frame(root, bg="black")
    keypad_frame.pack(side="bottom", fill="x", pady=40)

    code_var = tk.StringVar(value="")

    entry = tk.Entry(
        keypad_frame,
        textvariable=code_var,
        font=("Helvetica", 28, "bold"),
        justify="center",
        state="readonly",
        readonlybackground="black",
        fg="white",
        bd=2,
        relief="solid",
        width=10,
    )
    entry.grid(row=0, column=0, columnspan=3, pady=(0, 20))

    def append_digit(digit):
        current = code_var.get()
        next_value = f"{current}{digit}"
        code_var.set(next_value)
        if next_value == UNLOCK_CODE:
            unlock()

    def clear_code():
        code_var.set("")

    button_style = {
        "font": ("Helvetica", 22, "bold"),
        "width": 5,
        "height": 2,
        "bg": "#222222",
        "fg": "white",
        "activebackground": "#444444",
        "activeforeground": "white",
        "bd": 0,
    }

    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    row_offset = 1
    for index, digit in enumerate(digits):
        row = index // 3 + row_offset
        column = index % 3
        tk.Button(
            keypad_frame,
            text=digit,
            command=lambda d=digit: append_digit(d),
            **button_style,
        ).grid(row=row, column=column, padx=10, pady=10)

    tk.Button(
        keypad_frame,
        text="Очистить",
        command=clear_code,
        **button_style,
    ).grid(row=4, column=0, padx=10, pady=10)

    tk.Button(
        keypad_frame,
        text="0",
        command=lambda: append_digit("0"),
        **button_style,
    ).grid(row=4, column=1, padx=10, pady=10)

    tk.Button(
        keypad_frame,
        text="←",
        command=lambda: code_var.set(code_var.get()[:-1]),
        **button_style,
    ).grid(row=4, column=2, padx=10, pady=10)

    def unlock():
        root.grab_release()
        root.destroy()
        show_message(screen_width, screen_height)

    root.grab_set()
    root.mainloop()


def show_message(screen_width, screen_height):
    message_window = tk.Tk()
    message_window.title("Message")
    message_window.configure(bg="black")

    width = screen_width
    height = screen_height // 2
    message_window.geometry(f"{width}x{height}+0+0")
    message_window.attributes("-topmost", True)

    bloody_font = tkfont.Font(family="Impact", size=64, weight="bold")

    label = tk.Label(
        message_window,
        text="@servinant",
        fg="#b00000",
        bg="black",
        font=bloody_font,
    )
    label.pack(expand=True, fill="both")

    message_window.after(10_000, message_window.destroy)
    message_window.mainloop()


if __name__ == "__main__":
    main()
