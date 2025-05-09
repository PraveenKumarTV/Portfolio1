import tkinter as tk
from tkinter import filedialog, messagebox
import git
import os

def clone_repo():
    url = repo_url_entry.get()
    folder = filedialog.askdirectory(title="Select folder to clone into")
    if url and folder:
        try:
            git.Repo.clone_from(url, folder)
            messagebox.showinfo("Success", f"Cloned into {folder}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def push_repo():
    folder = filedialog.askdirectory(title="Select local repo folder")
    branch = branch_entry.get()
    commit_msg = commit_msg_entry.get()
    if folder and branch and commit_msg:
        try:
            repo = git.Repo(folder)
            repo.git.add(all=True)
            repo.index.commit(commit_msg)
            origin = repo.remote(name='origin')
            origin.push(refspec=f"{branch}:{branch}")
            messagebox.showinfo("Success", "Pushed to remote!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# UI Setup
root = tk.Tk()
root.title("Git GUI")

tk.Label(root, text="Remote Repo URL:").pack()
repo_url_entry = tk.Entry(root, width=50)
repo_url_entry.pack()

tk.Button(root, text="Clone Repository", command=clone_repo).pack(pady=5)

tk.Label(root, text="Branch to Push:").pack()
branch_entry = tk.Entry(root, width=30)
branch_entry.pack()

tk.Label(root, text="Commit Message:").pack()
commit_msg_entry = tk.Entry(root, width=50)
commit_msg_entry.pack()

tk.Button(root, text="Push Files", command=push_repo).pack(pady=10)

root.mainloop()
