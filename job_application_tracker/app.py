import tkinter as tk
from tkinter import ttk, messagebox
from db import init_db, add_application, get_all

init_db()

class AppTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job Application Tracker")
        self.geometry("600x400")
        ttk.Label(self, text="Company:").pack()
        self.company = tk.StringVar()
        ttk.Entry(self, textvariable=self.company).pack()
        ttk.Button(self, text="Add", command=self.add_app).pack()
        self.tree = ttk.Treeview(self, columns=("id","company"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("company", text="Company")
        self.tree.pack(expand=True, fill="both")
        self.load_table()

    def add_app(self):
        if not self.company.get().strip():
            messagebox.showwarning("Validation", "Company is required")
            return
        add_application(self.company.get().strip())
        self.company.set("")
        self.load_table()

    def load_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for r in get_all():
            self.tree.insert("", "end", values=(r["id"], r["company"]))

if __name__ == "__main__":
    app = AppTracker()
    app.mainloop()
