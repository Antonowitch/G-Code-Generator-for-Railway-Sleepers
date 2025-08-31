import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser

# Konfiguration
FONT = ("Arial", 16)
PADY = 6
PADX_LABEL = (10, 5)
PADX_ENTRY = (5, 10)
ENTRY_WIDTH = 10  # halbierte Breite

def generate_gcode(length, spacing, overhang, track_width, axis, depth, retract, plunge_feed, cut_feed, spindle_speed):
    gcode = [
        "G21 (Set units to millimeters)",
        "G90 (Absolute positioning)",
        f"M3 S{spindle_speed} (Start spindle clockwise at {spindle_speed} RPM)",
        f"G0 Z10 (Move to safe height)"
    ]

    if axis == "Y":
        gcode += [
            "(Mill left rail side)",
            f"G0 X0 Y0",
            f"G1 Z-{depth} F{plunge_feed}",
            f"G1 Y{length} F{cut_feed}",
            f"G0 Z{retract}",
            "(Mill right rail side)",
            f"G0 X{track_width} Y0",
            f"G1 Z-{depth} F{plunge_feed}",
            f"G1 Y{length} F{cut_feed}",
            f"G0 Z{retract}",
            "(Mill sleepers)"
        ]
        for i in range(int(length // spacing)):
            y = i * spacing
            gcode += [
                f"G0 X{-overhang} Y{y}",
                f"G1 Z-{depth} F{plunge_feed}",
                f"G1 X{track_width + overhang} F{cut_feed}",
                f"G0 Z{retract}"
            ]
    else:
        gcode += [
            "(Mill bottom rail side)",
            f"G0 X0 Y0",
            f"G1 Z-{depth} F{plunge_feed}",
            f"G1 X{length} F{cut_feed}",
            f"G0 Z{retract}",
            "(Mill top rail side)",
            f"G0 X0 Y{track_width}",
            f"G1 Z-{depth} F{plunge_feed}",
            f"G1 X{length} F{cut_feed}",
            f"G0 Z{retract}",
            "(Mill sleepers)"
        ]
        for i in range(int(length // spacing)):
            x = i * spacing
            gcode += [
                f"G0 X{x} Y{-overhang}",
                f"G1 Z-{depth} F{plunge_feed}",
                f"G1 Y{track_width + overhang} F{cut_feed}",
                f"G0 Z{retract}"
            ]

    gcode.append("M30 (End of program)")
    return "\n".join(gcode)

def save_gcode():
    try:
        length = float(entry_length.get().replace(",", "."))
        spacing = float(entry_spacing.get().replace(",", "."))
        overhang = float(entry_overhang.get().replace(",", "."))
        track_width = float(entry_track_width.get().replace(",", "."))
        depth = float(entry_depth.get().replace(",", "."))
        retract = float(entry_retract.get().replace(",", "."))
        plunge_feed = float(entry_plunge_feed.get().replace(",", "."))
        cut_feed = float(entry_cut_feed.get().replace(",", "."))
        spindle_speed = int(entry_spindle_speed.get().replace(",", "."))
        axis = axis_var.get()

        gcode = generate_gcode(length, spacing, overhang, track_width, axis, depth, retract, plunge_feed, cut_feed, spindle_speed)

        file_path = filedialog.asksaveasfilename(defaultextension=".nc", filetypes=[("G-Code files", "*.nc"), ("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(gcode)
            messagebox.showinfo("Success", f"G-code saved to:\n{file_path}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("G-Code Generator for Railway Sleepers")

def add_entry(label_text, default_value, row):
    tk.Label(root, text=label_text, font=FONT).grid(row=row, column=0, sticky="e", pady=PADY, padx=PADX_LABEL)
    entry = tk.Entry(root, font=FONT, width=ENTRY_WIDTH)
    entry.grid(row=row, column=1, pady=PADY, padx=PADX_ENTRY)
    entry.insert(0, default_value)
    return entry

# Eingabefelder
entry_length = add_entry("Track length (mm):", "200", 0)
entry_spacing = add_entry("Sleeper spacing (mm):", "7.53", 1)
entry_overhang = add_entry("Sleeper overhang (mm):", "5", 2)
entry_track_width = add_entry("Track width (mm):", "17.5", 3)
entry_depth = add_entry("Cutting depth (mm):", "3", 4)
entry_retract = add_entry("Retract height (mm):", "1", 5)
entry_plunge_feed = add_entry("Plunge feed rate (mm/min):", "600", 6)
entry_cut_feed = add_entry("Cutting feed rate (mm/min):", "600", 7)
entry_spindle_speed = add_entry("Spindle speed (RPM):", "12000", 8)

# Achsenauswahl
tk.Label(root, text="Cutting axis:", font=FONT).grid(row=9, column=0, sticky="e", pady=PADY, padx=PADX_LABEL)
axis_var = tk.StringVar(value="Y")
tk.OptionMenu(root, axis_var, "X", "Y").grid(row=9, column=1, pady=PADY, padx=PADX_ENTRY)

# Button zum Speichern
save_button = tk.Button(root, text="Generate and Save G-Code", command=save_gcode, font=FONT)
save_button.grid(row=10, column=0, columnspan=2, pady=PADY * 2)

# Statusbar mit Link
def open_link(event):
    webbrowser.open_new("https://www.youtube.com/@boessi")

statusbar = tk.Label(
    root,
    text="Anton CNC",
    font=FONT,
    bd=1,
    relief=tk.SUNKEN,
    anchor="center",  # zentriert
    fg="blue",
    bg="#d0d0d0",     # dunkleres Grau
    cursor="hand2"
)
statusbar.grid(row=11, column=0, columnspan=2, sticky="we")
statusbar.bind("<Button-1>", open_link)

# Start GUI
root.mainloop()
