import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompt user to select a file using a dialog box
file_path = filedialog.askopenfilename(title="Select Names File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

if file_path:
    # Read the names from the selected file
    names_array = []
    with open(file_path, "r") as file:
        names_array = [name.strip() for name in file]
    
    # Convert names array to a formatted string
    names_formatted = "[" + ", ".join('"' + name + '"' for name in names_array) + "]"
    print("Names formatted as Python array:")
    print(names_formatted)
    
    # Prompt user to select a save location using a dialog box
    save_path = filedialog.asksaveasfilename(title="Select Save Location", defaultextension=".py", filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    
    if save_path:
        # Save the formatted names as a Python file
        with open(save_path, "w") as file:
            file.write("Cities = " + names_formatted)
        print("Python file saved successfully.")
    else:
        print("Save location not selected.")
else:
    print("File not selected.")
