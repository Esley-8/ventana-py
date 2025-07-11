
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter, DateEntry

# Crear ventana principal
root = tk.Tk()
root.title("ttkbootstrap widget demo")
root.geometry("750x650")

# Aplicar estilo oscuro por defecto
style = Style(theme="darkly")

# === Función para cambiar tema ===
def cambiar_tema(event):
    nuevo_tema = theme_combo.get()
    style.theme_use(nuevo_tema)
    bg = style.colors.bg
    fg = style.colors.fg
    text_box.config(bg=bg, fg=fg, insertbackground=fg)

# === Encabezado y selección de tema ===
header = ttk.Frame(root)
header.pack(fill="x", pady=(10, 0), padx=10)

ttk.Label(header, text="darkly", font=("Helvetica", 20)).pack(side="left")

ttk.Label(header, text="Select a theme:").pack(side="right")
theme_combo = ttk.Combobox(header, values=style.theme_names(), state="readonly")
theme_combo.set("darkly")
theme_combo.pack(side="right", padx=5)
theme_combo.bind("<<ComboboxSelected>>", cambiar_tema)

# === Colores de tema ===
color_frame = ttk.Frame(root)
color_frame.pack(pady=10, padx=10, fill="x")

for color in ['primary', 'secondary', 'success', 'info', 'warning', 'danger', 'light', 'dark']:
    ttk.Button(color_frame, text=color, bootstyle=color).pack(side="left", padx=3)

# === Checkbuttons & radiobuttons ===
check_radio_frame = ttk.LabelFrame(root, text="Checkbuttons & radiobuttons")
check_radio_frame.pack(padx=10, pady=5, fill="x")

ttk.Checkbutton(check_radio_frame, text="selected").pack(side="left", padx=5)
ttk.Checkbutton(check_radio_frame, text="deselected").pack(side="left", padx=5)
ttk.Checkbutton(check_radio_frame, text="disabled", state="disabled").pack(side="left", padx=5)

ttk.Radiobutton(check_radio_frame, text="selected", value=1).pack(side="left", padx=5)
ttk.Radiobutton(check_radio_frame, text="deselected", value=2).pack(side="left", padx=5)
ttk.Radiobutton(check_radio_frame, text="disabled", value=3, state="disabled").pack(side="left", padx=5)

# === Tabla (Treeview) ===
tree = ttk.Treeview(root, columns=("City", "Rank"), show="headings", height=5, bootstyle="dark")
tree.heading("City", text="City")
tree.heading("Rank", text="Rank")

for city in [
    ("South Island, New Zealand", 1),
    ("Paris", 2),
    ("Bora Bora", 3),
    ("Maui", 4),
    ("Tahiti", 5),
]:
    tree.insert("", "end", values=city)

tree.pack(padx=10, pady=5)

# === Notebook con pestañas ===
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=5, fill="x")

for i in range(1, 6):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=f"Tab {i}")
    if i == 1:
        ttk.Label(tab, text="This is a notebook tab.\nYou can put any widget you want here.").pack(padx=10, pady=10)

# === Panel inferior con texto, sliders, medidor, y más ===
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Zen de Python
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

text_box = tk.Text(bottom_frame, height=12, wrap="word", bg=style.colors.bg, fg=style.colors.fg, insertbackground=style.colors.fg)
text_box.insert("1.0", zen)
text_box.config(state="disabled")
text_box.pack(side="left", fill="both", expand=True)

# === Medidor circular con texto "45" ===
meter_frame = ttk.Frame(bottom_frame)
meter_frame.pack(side="left", fill="y", padx=(10, 0))

meter = Meter(
    meter_frame,
    metersize=180,
    amountused=45,
    amounttotal=100,
    metertype="full",
    subtext="meter widget",
    bootstyle="info",
    interactive=False,
)
meter.pack(pady=(10, 0))

label_metro = ttk.Label(
    meter_frame,
    text="45",
    font=("Helvetica", 24, "bold"),
    background=style.colors.bg,
    foreground=style.colors.fg
)
label_metro.place(relx=0.5, rely=0.5, anchor="center")

# === Controles a la derecha ===
right_controls = ttk.Frame(bottom_frame)
right_controls.pack(side="right", fill="y", padx=10)

ttk.Button(right_controls, text="solid button", bootstyle="danger").pack(fill="x", pady=2)
ttk.Menubutton(right_controls, text="solid menubutton", bootstyle="dark").pack(fill="x", pady=2)
ttk.Button(right_controls, text="solid toolbutton", bootstyle="success").pack(fill="x", pady=2)
ttk.Button(right_controls, text="outline button", bootstyle="outline").pack(fill="x", pady=2)
ttk.Menubutton(right_controls, text="outline menubutton", bootstyle="outline-warning").pack(fill="x", pady=2)
ttk.Button(right_controls, text="outline toolbutton", bootstyle="outline-success").pack(fill="x", pady=2)
ttk.Button(right_controls, text="link button", bootstyle="link").pack(fill="x", pady=2)

ttk.Checkbutton(right_controls, text="rounded toggle").pack(fill="x", pady=2)
ttk.Checkbutton(right_controls, text="squared toggle").pack(fill="x", pady=2)

ttk.Label(right_controls, text="Other input widgets").pack(pady=(10, 0))

# Campos con valores por defecto
entry1 = ttk.Entry(right_controls)
entry1.insert(0, "entry widget")
entry1.pack(fill="x", pady=2)

entry2 = ttk.Entry(right_controls, show="*")
entry2.insert(0, "secret")
entry2.pack(fill="x", pady=2)

spin = ttk.Spinbox(right_controls, from_=0, to=100)
spin.set(45)
spin.pack(fill="x", pady=2)

combo = ttk.Combobox(right_controls, values=["simplex", "darkly", "flatly", "cosmo"])
combo.set("cosmo")
combo.pack(fill="x", pady=2)

date = DateEntry(right_controls)

date.pack(fill="x", pady=2)

# Ejecutar ventana
root.mainloop()