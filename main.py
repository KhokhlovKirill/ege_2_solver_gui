from tkinter import *
from tkinter import ttk

from TruthTable import TruthTable

truth_table = None

def render_table(table):
    tree.delete(*tree.get_children())
    for row in table:
        tree.insert('', END, values=row)


def solve():
    truth_table = TruthTable(logical_exp_inp.get())
    render_table(truth_table.get_results(truth_table.least_common))

root = Tk()
root.title('Решатель задания №2 ЕГЭ по информатике')
root.geometry('500x500')
root.minsize(500, 500)
root.maxsize(500, 500)

heading = ttk.Label(text='Введите логическое выражение:')
heading.pack()

logical_exp_inp = ttk.Entry()
logical_exp_inp.pack(pady=10, padx=25, fill=X)

solve_btn = ttk.Button(text='Решить', command=solve)
solve_btn.pack()

tree = ttk.Treeview(columns=('w', 'x', 'y', 'z', 'result'), show='headings', height=100)
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

root.mainloop()