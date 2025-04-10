# VB.NET RTF Combiner – User Guide

## What This Script Does

This Python script combines your VB.NET code files into a single `.rtf` document with Visual Studio-style syntax highlighting.

It begins with your **global variables/module** file, followed by all `.vb` code files in a selected folder—automatically skipping system-generated or duplicate files such as:

- `*.Designer.vb`
- `AssemblyInfo.vb`
- `.NETFramework,Version=*.AssemblyAttributes.vb`

---

## Step 1: Install Python

1. Go to the official Python download page:  
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest version of Python (3.10+ recommended).
3. **Important**: During installation, **tick the box** that says **“Add Python to PATH”**.
4. Click **Install Now** and follow the on-screen instructions.

---

## Step 2: Install Required Packages

Open **Command Prompt (Windows)** or **Terminal (Mac/Linux)** and run:

```bash
pip install pygments
```

This installs the syntax highlighter needed to generate the coloured output.

---

## Step 3: Download the Script

Download the script from GitHub above or from the releases section

---

## Step 4: Run the Script

### Using Command Line:

1. Open **Command Prompt** or **Terminal**.
2. Navigate to the folder where the script is saved:

```bash
cd path\to\your\script
```

3. Run the script:

```bash
python "code format - Public.py"
```

---

## Step 5: Follow the On-Screen Prompts

The script will display two message boxes:

1. **Step 1** – Select your global variables/module `.vb` file.
2. **Step 2** – Select the folder containing your other `.vb` code files.

⚠️ Note: The script **automatically excludes**:
- `.Designer.vb` files
- `AssemblyInfo.vb`
- System framework-generated files

---

## Step 6: Check the Output

The script will generate a file like:

```
combined_output.rtf
```

If a file with that name already exists, the script will automatically create:

```
combined_output_1.rtf
combined_output_2.rtf
...
```

📂 It will be saved in the **same directory** where the script is run.

📝 You can open it with **Microsoft Word**, **WordPad**, or any RTF-compatible editor to view the **colour-coded VB.NET source code**. Then, press **Ctrl + A** to select all, followed by **Ctrl + C** to copy it. You can then paste it into your main file or document.

---

## Done!

You now have a clean, colour-coded VB.NET project in RTF format—great for documentation, printing, or submission!
