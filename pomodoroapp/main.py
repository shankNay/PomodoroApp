from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0  # to record work and break cycles
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

# resets every element in the GUI
def timer_reset():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_box.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 30), fg=PINK, bg=YELLOW)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 30), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)   # 1000ms = 1 second delay
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(REPS / 2)):
            mark += "✅"  # after a successful rep this gets displayed in the checkbox
        check_box.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # creating the background tomato canvas
tomato_img = PhotoImage(file="tomato.png")  # to read the png photo
canvas.create_image(100, 112, image=tomato_img)  # half of the image canvas size
timer_text = canvas.create_text(100, 117, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

check_box = Checkbutton(fg=GREEN, bg=YELLOW)
check_box.grid(column=2, row=4)

reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(column=3, row=3)

window.mainloop()
