import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import RtfFormatter

def get_vb_files(directory):
    """
    Recursively locate all VB.NET files in the directory that are not
    designer files or specific system files.
    """
    vb_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if (file.endswith(".vb") and 
                not file.endswith(".Designer.vb") and 
                file not in ["AssemblyInfo.vb", ".NETFramework,Version=v4.7.2.AssemblyAttributes.vb"]):
                vb_files.append(os.path.join(root, file))
    return vb_files

def main():
    # Create the Tkinter root window and immediately withdraw it to avoid showing a white box.
    root = tk.Tk()
    root.withdraw()
    
    # Step 1: Instruct the user to select the module/global variables file.
    messagebox.showinfo("Step 1", "Please select your module/global variables file.")
    global_file_path = filedialog.askopenfilename(
        title="Select your module/global variables file",
        filetypes=[("VB.NET Files", "*.vb"), ("All Files", "*.*")]
    )
    if not global_file_path:
        messagebox.showinfo("Operation Cancelled", "No global variables file selected.")
        return
    
    # Step 2: Instruct the user to select the folder containing the VB.NET code files.
    messagebox.showinfo("Step 2", "Now please select the folder containing your VB.NET code files.")
    code_folder = filedialog.askdirectory(title="Select the folder containing your VB.NET code files")
    if not code_folder:
        messagebox.showinfo("Operation Cancelled", "No folder selected for code files.")
        return

    # Set up the VB.NET lexer and RTF formatter.
    lexer = get_lexer_by_name("vb.net")
    formatter = RtfFormatter(style="vs", full=False, fontface="Aptos (Body)")

    # RTF header and footer.
    rtf_header = r"{\rtf1\ansi{\fonttbl{\f0\fnil Aptos (Body);}}" + "\n"
    rtf_footer = "}"
    content = ""

    # Process the global variables file first.
    global_filename = os.path.basename(global_file_path)
    try:
        with open(global_file_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        messagebox.showerror("Error", f"Error reading global variables file:\n{e}")
        return

    content += r"{\f0\b\fs28 " + global_filename + "}" + r"\par" + "\n"
    highlighted = highlight(code, lexer, formatter)
    content += highlighted + r"\par" + "\n"

    # Retrieve and process other VB.NET files from the selected folder.
    vb_files = get_vb_files(code_folder)
    # Exclude the global variables file if it is found in the selected folder.
    global_abs = os.path.abspath(global_file_path)
    vb_files = [f for f in vb_files if os.path.abspath(f) != global_abs]

    if not vb_files:
        messagebox.showinfo("Information", "No additional VB.NET files found in the selected folder.")
    else:
        vb_files.sort()  # Sorting for a consistent order.
        for file in vb_files:
            file_name = os.path.basename(file)
            content += r"{\f0\b\fs28 " + file_name + "}" + r"\par" + "\n"
            try:
                with open(file, "r", encoding="utf-8") as f:
                    code = f.read()
            except Exception as e:
                print(f"Error reading {file}: {e}")
                continue
            highlighted = highlight(code, lexer, formatter)
            content += highlighted + r"\par" + "\n"

    # Save the final combined RTF document to the current working directory.
    current_directory = os.getcwd()
    base_filename = "combined_output"
    output_path = os.path.join(current_directory, base_filename + ".rtf")

    # If file already exists, append a number to avoid overwrite
    counter = 1
    while os.path.exists(output_path):
        output_path = os.path.join(current_directory, f"{base_filename}_{counter}.rtf")
        counter += 1

    try:
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write(rtf_header + content + rtf_footer)
    except Exception as e:
        messagebox.showerror("Error", f"Error writing output file:\n{e}")
        return
    # Display a success message.
    messagebox.showinfo("Success", f"Combined RTF document created successfully:\n{output_path}")

if __name__ == '__main__':
    main()
