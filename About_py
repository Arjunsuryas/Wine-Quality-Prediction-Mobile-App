import tkinter as tk
from tkinter import ttk

# Define the factors
factors = [
    {
        "title": "Alcohol Content",
        "description": "Higher alcohol levels generally improve wine quality up to an optimal point",
    },
    {
        "title": "Acidity Balance",
        "description": "Proper pH and acidity levels are crucial for wine stability and taste",
    },
    {
        "title": "Awards",
        "description": "Recognition and awards can indicate wine quality",
    },
    {
        "title": "Aroma & Flavor",
        "description": "Complex aromas and balanced flavors contribute to wine excellence",
    },
]

# Initialize main window
root = tk.Tk()
root.title("About Wine Factors")
root.geometry("500x400")

# Create a scrollable frame
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add factor content to scrollable frame
for factor in factors:
    title_label = tk.Label(scrollable_frame, text=factor["title"], font=("Helvetica", 14, "bold"), anchor="w")
    title_label.pack(fill="x", padx=10, pady=(10, 0))

    desc_label = tk.Label(scrollable_frame, text=factor["description"], font=("Helvetica", 12), wraplength=460, justify="left", anchor="w")
    desc_label.pack(fill="x", padx=10, pady=(2, 10))

root.mainloop()
