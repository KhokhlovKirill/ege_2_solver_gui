from tkinter import *
from tkinter import ttk

from Solver import Solver
from TruthTable import TruthTable

truth_table = None

def format_exp(exp):
    exp = exp.replace('∧', ' ∧ ').replace('∨', ' ∨ ').replace('≡', ' ≡ ').replace('→', ' → ').replace('¬', ' ¬ ')
    exp = exp.replace('∧', 'and').replace('∨', 'or').replace('≡', '==').replace('→', '<=').replace('¬', '1-')
    return exp

def render_table(table):
    tree.delete(*tree.get_children())
    for row in table:
        tree.insert('', END, values=row)


def make_table():
    truth_table = TruthTable(format_exp(logical_exp_inp.get()))
    res = None
    if is_false_enabled.get() == 1 and is_true_enabled.get() == 1:
        res = 2
    elif is_false_enabled.get() == 0 and is_true_enabled.get() == 1:
        res = 1
    if is_false_enabled.get() == 1 and is_true_enabled.get() == 0:
        res = 0
    if is_false_enabled.get() == 0 and is_true_enabled.get() == 0:
        render_table(truth_table.get_results(truth_table.least_common))
        return
    render_table(truth_table.get_results(res))

def solve():
    values = []
    for r in range(3):
        row_vals = []
        for c in range(5):
            val = entries[r][c].get()
            row_vals.append(val)
        values.append(row_vals)

    solver = Solver(values, format_exp(logical_exp_inp.get()))
    result['text'] = f'Результат: {''.join(solver.solve())}'

root = Tk()
root.title('Решатель задания №2 ЕГЭ по информатике')
root.geometry('900x500')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

first_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[3, 3], height=70, width=30)
heading = ttk.Label(first_frame, text='Введите логическое выражение:')
heading.pack()

logical_exp_inp = ttk.Entry(first_frame)
logical_exp_inp.pack(pady=10, padx=25, fill=X)

solve_btn = ttk.Button(first_frame, text='Решить', command=make_table)
solve_btn.pack()

is_false_enabled = IntVar()
false_btn = ttk.Checkbutton(first_frame, text="Отображать ложные комбинации", command=make_table, variable=is_false_enabled)
false_btn.pack(padx=6, pady=6)

is_true_enabled = IntVar()
true_btn = ttk.Checkbutton(first_frame, text="Отображать истинные комбинации", command=make_table, variable=is_true_enabled)
true_btn.pack(padx=6, pady=6)


tree = ttk.Treeview(first_frame, columns=('w', 'x', 'y', 'z', 'result'), show='headings', height=60)
tree.column('w', stretch=NO, width=40)
tree.column('x', stretch=NO, width=40)
tree.column('y', stretch=NO, width=40)
tree.column('z', stretch=NO, width=40)
tree.column('result', stretch=NO, width=70)

tree.heading('w', text='w')
tree.heading('x', text='x')
tree.heading('y', text='y')
tree.heading('z', text='z')
tree.heading('result', text='Результат')
tree.pack(fill=Y, padx=100, pady=20)

first_frame.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
solve_btn = ttk.Button(first_frame, text='Решить', command=make_table)
solve_btn.pack()

second_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[3, 3], height=70, width=30)

column_names = ('1', '2', '3', '4', 'F')
for c in range(5):
    lbl = ttk.Label(second_frame, text=column_names[c], anchor='center')
    lbl.grid(row=0, column=c, padx=4, pady=(0,4), sticky='nsew')

entries = []
for r in range(3):
    row_entries = []
    for c in range(5):
        e = ttk.Entry(second_frame, width=10)
        e.grid(row=r+1, column=c, padx=4, pady=4)
        row_entries.append(e)
    entries.append(row_entries)

read_btn = ttk.Button(second_frame, text='Найти ответ', command=solve)
read_btn.grid(row=6, column=0, columnspan=5, pady=(8,0))

result = ttk.Label(second_frame, text="Результат:", font=('Arial', 14))
result.grid(row=7, column=0, columnspan=5)

second_frame.grid(row=0, column=1, sticky='ne', padx=8, pady=8)
root.mainloop()