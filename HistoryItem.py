import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass

@dataclass
class WinePrediction:
    date: str
    score: float
    notes: str

# Example prediction
prediction = WinePrediction(date="2025-10-26", score=7.2, notes="Fruity aroma, balanced acidity")

# Helper functions
def get_quality_color(score: float) -> str:
    if score >= 8:
        return "#16A34A"  # Green
    if score >= 6:
        return "#65A30D"  # Yellow-green
    if score >= 4:
        return "#D97706"  # Orange
    return "#DC2626"      # Red

def get_quality_label(score: float) -> str:
    if score >= 8:
        return "Excellent"
    if score >= 6:
        return "Good"
    if score >= 4:
        return "Fair"
    return "Poor"

# Initialize Tkinter window
root = tk.Tk()
root.title("Wine Prediction History")
root.geometry("400x150")

frame = ttk.Frame(root, padding=16)
frame.pack(fill="both", expand=True)

# Date label
date_label = ttk.Label(frame, text=f"Date: {prediction.date}", font=("Helvetica", 12))
date_label.pack(anchor="w")

# Score label with color
score_label = tk.Label(
    frame,
    text=f"Score: {prediction.score} ({get_quality_label(prediction.score)})",
    fg=get_quality_color(prediction.score),
    font=("Helvetica", 12, "bold")
)
score_label.pack(anchor="w", pady=(4, 0))

# Notes label
notes_label = ttk.Label(frame, text=f"Notes: {prediction.notes}", font=("Helvetica", 12))
notes_label.pack(anchor="w", pady=(4, 0))

root.mainloop()
