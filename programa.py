import tkinter as tk
from tkinter import ttk

def parse_float(value: str) -> float:
    try:
        # Permitir coma o punto decimal
        return float(value.replace(',', '.').strip())
    except:
        return 0.0

def calcular_total(*_):
    minutos = parse_float(entry_minutos.get())
    precio_min = parse_float(entry_precio_minuto.get())
    gramos = parse_float(entry_gramos.get())
    precio_gramo = parse_float(entry_precio_gramo.get())
    total = minutos * precio_min + gramos * precio_gramo
    label_total_valor.config(text=f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

root = tk.Tk()
root.title("Cálculo de Coste")
root.resizable(False, False)

main = ttk.Frame(root, padding=16)
main.grid()

ttk.Label(main, text="Minutos procesados:").grid(row=0, column=0, sticky="w", padx=(0,8), pady=6)
entry_minutos = ttk.Entry(main, width=12)
entry_minutos.grid(row=0, column=1, pady=6)

ttk.Label(main, text="Precio por minuto (€):").grid(row=1, column=0, sticky="w", padx=(0,8), pady=6)
entry_precio_minuto = ttk.Entry(main, width=12)
entry_precio_minuto.insert(0, "0.15")
entry_precio_minuto.grid(row=1, column=1, pady=6)

ttk.Label(main, text="Gramos utilizados:").grid(row=2, column=0, sticky="w", padx=(0,8), pady=6)
entry_gramos = ttk.Entry(main, width=12)
entry_gramos.grid(row=2, column=1, pady=6)

ttk.Label(main, text="Precio por gramo (€):").grid(row=3, column=0, sticky="w", padx=(0,8), pady=6)
entry_precio_gramo = ttk.Entry(main, width=12)
entry_precio_gramo.insert(0, "0.20")
entry_precio_gramo.grid(row=3, column=1, pady=6)

ttk.Separator(main, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=8)

ttk.Label(main, text="Total:").grid(row=5, column=0, sticky="w", padx=(0,8), pady=6)
label_total_valor = ttk.Label(main, text="0,00 €", font=("Helvetica", 14, "bold"))
label_total_valor.grid(row=5, column=1, sticky="e", pady=6)

def on_change(var, index, mode):
    calcular_total()

for e in (entry_minutos, entry_precio_minuto, entry_gramos, entry_precio_gramo):
    e.bind("<KeyRelease>", calcular_total)
    e.bind("<FocusOut>", calcular_total)

btn = ttk.Button(main, text="Calcular", command=calcular_total)
btn.grid(row=6, column=0, columnspan=2, pady=(8,0), sticky="ew")

entry_minutos.focus()
calcular_total()
root.mainloop()