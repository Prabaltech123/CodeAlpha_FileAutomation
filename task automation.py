
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("JPG File Organizer")
root.geometry("700x550")
root.resizable(False, False)
root.configure(bg="#f1f5f9")

source_folder = tk.StringVar()
destination_folder = tk.StringVar()

# ---------------- HEADER ----------------

header = tk.Frame(root, bg="#17365d", pady=18)
header.pack(fill="x")

tk.Label(
    header,
    text="JPG FILE ORGANIZER",
    font=("Arial", 22, "bold"),
    bg="#17365d",
    fg="white"
).pack()

tk.Label(
    header,
    text="Organize your JPG images automatically",
    font=("Arial", 11),
    bg="#17365d",
    fg="#dbeafe"
).pack(pady=4)

# ---------------- FOLDER SELECTION ----------------

folder_frame = tk.LabelFrame(
    root,
    text=" Select Folders ",
    font=("Arial", 12, "bold"),
    bg="#f1f5f9",
    fg="#17365d",
    padx=15,
    pady=15
)
folder_frame.pack(fill="x", padx=20, pady=15)

tk.Label(
    folder_frame,
    text="Source Folder:",
    font=("Arial", 10, "bold"),
    bg="#f1f5f9"
).grid(row=0, column=0, sticky="w", pady=10)

tk.Entry(
    folder_frame,
    textvariable=source_folder,
    width=48,
    font=("Arial", 10)
).grid(row=0, column=1, padx=8)

def select_source():
    folder = filedialog.askdirectory(title="Select Source Folder")
    if folder:
        source_folder.set(folder)

tk.Button(
    folder_frame,
    text="Browse",
    command=select_source
).grid(row=0, column=2)

tk.Label(
    folder_frame,
    text="Destination:",
    font=("Arial", 10, "bold"),
    bg="#f1f5f9"
).grid(row=1, column=0, sticky="w", pady=10)

tk.Entry(
    folder_frame,
    textvariable=destination_folder,
    width=48,
    font=("Arial", 10)
).grid(row=1, column=1, padx=8)

def select_destination():
    folder = filedialog.askdirectory(
        title="Select Destination Folder"
    )
    if folder:
        destination_folder.set(folder)

tk.Button(
    folder_frame,
    text="Browse",
    command=select_destination
).grid(row=1, column=2)

# ---------------- RESULTS AREA ----------------

results_frame = tk.LabelFrame(
    root,
    text=" Activity Log ",
    font=("Arial", 12, "bold"),
    bg="#f1f5f9",
    fg="#17365d",
    padx=10,
    pady=10
)
results_frame.pack(fill="both", expand=True, padx=20, pady=5)

log = scrolledtext.ScrolledText(
    results_frame,
    height=8,
    font=("Consolas", 10),
    wrap=tk.WORD
)
log.pack(fill="both", expand=True)

def write_log(message):
    log.insert(tk.END, message + "\n")
    log.see(tk.END)

# ---------------- ORGANIZE FILES ----------------

def organize_files():
    source = source_folder.get().strip()
    destination = destination_folder.get().strip()

    if not source or not destination:
        messagebox.showwarning(
            "Missing Folder",
            "Please select both folders."
        )
        return

    if not os.path.isdir(source):
        messagebox.showerror(
            "Invalid Source",
            "The source folder does not exist."
        )
        return

    if os.path.abspath(source) == os.path.abspath(destination):
        messagebox.showerror(
            "Invalid Destination",
            "Choose a different destination folder."
        )
        return

    try:
        os.makedirs(destination, exist_ok=True)

        moved = 0
        skipped = 0

        write_log("\nStarting JPG file organization...")
        write_log("Source: " + source)
        write_log("Destination: " + destination)

        for filename in os.listdir(source):
            source_path = os.path.join(source, filename)

            # Process JPG files only, not subfolders
            if (
                os.path.isfile(source_path)
                and filename.lower().endswith(".jpg")
            ):
                destination_path = os.path.join(
                    destination, filename
                )

                # Never overwrite an existing file
                if os.path.exists(destination_path):
                    write_log("Skipped (already exists): " + filename)
                    skipped += 1
                    continue

                shutil.move(source_path, destination_path)
                write_log("Moved: " + filename)
                moved += 1

        write_log("\nOrganization completed!")
        write_log(f"Files moved: {moved}")
        write_log(f"Files skipped: {skipped}")

        messagebox.showinfo(
            "Completed",
            f"Files moved: {moved}\nFiles skipped: {skipped}"
        )

    except OSError as error:
        messagebox.showerror("File Error", str(error))
        write_log("Error: " + str(error))

# ---------------- BUTTONS ----------------

button_frame = tk.Frame(root, bg="#f1f5f9")
button_frame.pack(pady=12)

tk.Button(
    button_frame,
    text="ORGANIZE JPG FILES",
    command=organize_files,
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    padx=18,
    pady=9
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="CLEAR LOG",
    command=lambda: log.delete("1.0", tk.END),
    font=("Arial", 10, "bold"),
    bg="#64748b",
    fg="white",
    padx=18,
    pady=9
).grid(row=0, column=1, padx=8)

root.mainloop()
