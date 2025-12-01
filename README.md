# File-Handling


# Python File Handling — Examples (README)

This README contains 8 independent and simple examples for learning file handling in Python. Each example is fully self-contained: it creates its own files/folders and removes them at the end (so the working directory stays clean). Each section includes a short explanation and ready-to-run code — suitable for a tutorial video or publishing on GitHub.

---

## Examples index
1. Write Files — create and write text and binary files
2. Read Files — create and read a file
3. Rename & Delete — rename and delete a file
4. Directories — create and remove directories
5. File Methods — use `tell()`, `seek()`, `truncate()`
6. OS File Methods — `os.stat`, `os.access`, `mkdir`, `rmdir`
7. Pathlib Methods — using `pathlib.Path`
8. Merge Files — merge two text files

---

## Quick run guide
You can copy each section separately and run it in a Python file, or import and call the example functions from `file.py` (if the examples are placed there). Every example is standalone and does not depend on the files from the other examples.

Examples follow below — each example includes a brief explanation and a code block.

---

### 1) Write Files — create and write text and binary files
**Description:** This example shows how to create a text file and write some text into it, then create a small binary file.

```python
def example_write_files():
    """Create a text file and a binary file, then remove them."""
    text_path = "ex_write.txt"
    with open(text_path, "w", encoding="utf-8") as f:
        f.write("Hello from example_write_files()\n")

    binary_path = "ex_write.bin"
    with open(binary_path, "wb") as f:
        f.write(bytes(range(8)))

    # cleanup
    for p in (text_path, binary_path):
        if os.path.exists(p):
            os.remove(p)
```

**Note:** Use `with open(..., 'w')` to write files so they are automatically closed without calling `close()`.

---

### 2) Read Files — create and read a file
**Description:** This example first creates a file so that reading always succeeds, then reads the entire content with `read()` and removes the file afterwards.

```python
def example_read_files():
    fname = "ex_read.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("This file is created for reading example.\nLine 2\n")

    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    print(content)

    os.remove(fname)
```

**Note:** For line-by-line reading use `for line in f:` or `readline()`.

---

### 3) Rename & Delete — rename and delete a file
**Description:** Demonstrates how to create a file, rename it with `os.rename()`, and then delete it with `os.remove()`.

```python
def example_rename_delete():
    src = "ex_rename_src.txt"
    dst = "ex_rename_dst.txt"
    with open(src, "w", encoding="utf-8") as f:
        f.write("temporary file\n")

    os.rename(src, dst)
    print("Renamed to", dst)
    os.remove(dst)
```

**Note:** In some cases `os.replace()` is safer because it will replace the destination if it already exists.

---

### 4) Directories — create and remove directories
**Description:** How to create nested directories, list directory contents, and remove the whole directory tree with `shutil.rmtree()`.

```python
def example_directories():
    dirname = "ex_dir_folder"
    os.makedirs(os.path.join(dirname, "sub"), exist_ok=True)
    print(os.listdir("."))
    shutil.rmtree(dirname)
```

**Note:** `os.makedirs(..., exist_ok=True)` prevents an error if the directory already exists.

---

### 5) File Methods — tell(), seek(), truncate()
**Description:** Show the file cursor position, move it, and shorten a file using `truncate()`.

```python
def example_file_methods():
    fname = "ex_methods.txt"
    with open(fname, "w+", encoding="utf-8") as f:
        f.write("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")
        f.flush()
        print("tell:", f.tell())
        f.seek(0)
        print("first10:", f.read(10))
        f.seek(0)
        f.truncate(5)
        f.seek(0)
        print("after truncate:", f.read())
    os.remove(fname)
```

**Note:** `tell()` returns the current byte position; use `seek()` to move it.

---

### 6) OS File Methods — os.stat, os.access, mkdir, rmdir
**Description:** Retrieve file metadata (size, timestamps), check permissions, and create/remove a simple directory.

```python
def example_os_file_directory_methods():
    fname = "ex_osfile.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("os methods\n")
    st = os.stat(fname)
    print("size:", st.st_size, "mtime:", st.st_mtime)
    print("readable:", os.access(fname, os.R_OK))
    dname = "ex_os_dir"
    os.mkdir(dname)
    os.rmdir(dname)
    os.remove(fname)
```

**Note:** `os.stat()` returns metadata that is useful for logging or change detection.

---

### 7) Pathlib Methods — Path.exists(), resolve(), unlink()
**Description:** Using `pathlib` which provides a modern and convenient API compared to `os.path`.

```python
from pathlib import Path

def example_os_path_methods():
    sample = Path("ex_path_sample.txt")
    sample.write_text("pathlib sample\n", encoding="utf-8")
    print("exists?", sample.exists())
    print("absolute:", sample.resolve())
    sample.unlink()
```

**Note:** `pathlib` is more readable and is recommended for new code.

---

### 8) Merge Files — merge two text files
**Description:** Create two text files and write the contents of both into a single output file.

```python
def example_merge_text_files():
    a = "ex_merge_a.txt"
    b = "ex_merge_b.txt"
    out = "ex_merged.txt"
    with open(a, "w", encoding="utf-8") as f:
        f.write("Content A\n")
    with open(b, "w", encoding="utf-8") as f:
        f.write("Content B\n")
    with open(out, "w", encoding="utf-8") as m:
        for p in (a, b):
            with open(p, "r", encoding="utf-8") as src:
                m.write(src.read())
    # cleanup
    for p in (a, b, out):
        os.remove(p)
```

**Note:** For large files, read and write line-by-line to reduce memory usage.

---

## Tips for a tutorial video
- Show and run each example separately.
- Explain the working directory before running (`os.getcwd()`) and emphasize that files are created there.
- For Persian-speaking audiences, keep short English comments in the code and explain verbally in Persian.
- For a follow-up video, add examples for CSV and JSON (using the `csv` and `json` modules).

---


