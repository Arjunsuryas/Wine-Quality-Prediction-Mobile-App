import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass, field
from typing import List

# Dataclass for WinePrediction
@dataclass
class WinePrediction:
    date: str
    score: float
    notes: str

# Mock storage functions
history_storage: List[WinePrediction] = [
    WinePrediction(date="2025-10-26", score=7.2, notes="Fruity aroma, balanced acidity"),
    WinePrediction(date="2025-10-25", score=8.5, notes="Rich body, excellent finish"),
]

def get_wine_prediction_history() -> List[WinePrediction]:
    return history_storage.copy()

def clear_wine_prediction_history():
    history_storage.clear()

# Helper functions
def get_quality_color(score: float) -> str:
    if score >= 8: return "#16A34A"
    if score >= 6: return "#65A30D"
    if score >= 4: return "#D97706"
    return "#DC2626"

def get_quality_label(score: float) -> str:
    if score >= 8: return "Excellent"
    if score >= 6: return "Good"
    if score >= 4: return "Fair"
    return "Poor"

# Load history into the treeview
def load_history():
    for i in tree.get_children():
        tree.delete(i)
    for pred in get_wine_prediction_history():
        tree.insert("", "end", values=(
            pred.date,
            f"{pred.score} ({get_quality_label(pred.score)})",
            pred.notes
        ))

def clear_history():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear history?"):
        clear_wine_prediction_history()
        load_history()

# Initialize Tkinter window
root = tk.Tk()
root.title("Wine Prediction History")
root.geometry("600x400")

# Header
header_frame = ttk.Frame(root, padding=10)
header_frame.pack(fill="x")

title_label = ttk.Label(header_frame, text="Wine Prediction History", font=("Helvetica", 16, "bold"))
title_label.pack(side="left")

clear_btn = ttk.Button(header_frame, text="Clear History", command=clear_history)
clear_btn.pack(side="right")

# Treeview for history
columns = ("Date", "Score", "Notes")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180 if col != "Notes" else 250)

tree.pack(fill="both", expand=True, padx=10, pady=10)

# Load initial history
load_history()

root.mainloop()
