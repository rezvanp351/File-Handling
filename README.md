# Python File Handling — Runnable Examples

This repository contains a single script, `file.py`, with independent, runnable examples that demonstrate common file and directory operations in Python. The examples are designed for learning and for short tutorial videos — each example creates its own temporary files/folders and cleans them up so the working directory stays tidy.

## Contents
- `file.py` — CLI wrapper with example functions (write, read, rename, directories, file methods, os/file/path utilities, and merging files).

## Quick start
Prerequisites: Python 3.7+.

From PowerShell (Windows):

```powershell
# list available examples
python file.py list

# run a single example, e.g. the 'methods' example
python file.py run methods

# run all examples sequentially (if available)
python file.py run all
```

If you use another shell, replace the `powershell` snippet accordingly.

## Examples (short names)
The CLI exposes short names for each example. The typical set included in `file.py` are:

- `write` — write text and binary files (creates `ex_write.txt` and `ex_write.bin`)  
- `read` — create and read a file (creates and reads `ex_read.txt`)  
- `rename` — rename a file then delete it (`ex_rename_src.txt` -> `ex_rename_dst.txt`)  
- `dirs` — create nested directories and remove them (`ex_dir_folder/`)  
- `methods` — demonstrate `tell()`, `seek()`, `truncate()` on a file (`ex_methods.txt`)  
- `os` — show `os.stat`, `os.access`, `mkdir`, `rmdir` behavior (`ex_osfile.txt`, `ex_os_dir`)  
- `path` — use `pathlib.Path` to write/read/unlink (`ex_path_sample.txt`)  
- `merge` — create two small files and merge them into one (`ex_merge_a.txt`, `ex_merge_b.txt`, `ex_merged.txt`)  

Note: some example functions in `file.py` may be commented out or omitted — run `python file.py list` to see the exact names implemented in your copy.

## Examples — full code (runnable)
Below are the eight examples shown above as ready-to-run code snippets. Each example is independent: it creates its own temporary files/folders and attempts to clean them up at the end. You can copy any example into a script and run it, or paste all into `file.py` and call them from a small CLI.

Prerequisite imports (use these at the top if you copy multiple examples):

```python
import os
import shutil
from pathlib import Path
```

1) Write text & binary files

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

# example_write_files()
```

2) Create and read a file

```python
def example_read_files():
	"""Create a file, read its full content, then delete it."""
	fname = "ex_read.txt"
	with open(fname, "w", encoding="utf-8") as f:
		f.write("This file is created for reading example.\nLine 2\n")

	with open(fname, "r", encoding="utf-8") as f:
		content = f.read()
	print(content)

	os.remove(fname)

# example_read_files()
```

3) Rename & delete a file

```python
def example_rename_delete():
	"""Create a file, rename it, and delete the renamed file."""
	src = "ex_rename_src.txt"
	dst = "ex_rename_dst.txt"
	with open(src, "w", encoding="utf-8") as f:
		f.write("temporary file\n")

	os.rename(src, dst)
	print("Renamed to", dst)
	os.remove(dst)

# example_rename_delete()
```

4) Directories: create nested and remove

```python
def example_directories():
	"""Create a nested directory and remove it."""
	dirname = "ex_dir_folder"
	os.makedirs(os.path.join(dirname, "sub"), exist_ok=True)
	print("Created:", dirname)
	print("Listing current dir (first 10 entries):", os.listdir(".")[:10])
	shutil.rmtree(dirname)

# example_directories()
```

5) File methods: tell(), seek(), truncate()

```python
def example_file_methods():
	"""Demonstrate tell(), seek(), truncate() with a writable file."""
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

# example_file_methods()
```

6) OS file & directory methods: stat, access, mkdir, rmdir

```python
def example_os_file_directory_methods():
	"""Show os.stat, os.access and simple dir creation/removal."""
	fname = "ex_osfile.txt"
	with open(fname, "w", encoding="utf-8") as f:
		f.write("os methods\n")
	st = os.stat(fname)
	print("size:", st.st_size, "mtime:", st.st_mtime)
	print("readable:", os.access(fname, os.R_OK))
	dname = "ex_os_dir"
	os.mkdir(dname)
	print("Created dir:", dname)
	os.rmdir(dname)
	os.remove(fname)

# example_os_file_directory_methods()
```

7) Pathlib convenience methods

```python
from pathlib import Path

def example_os_path_methods():
	"""Use pathlib.Path to write, check and remove a file."""
	sample = Path("ex_path_sample.txt")
	sample.write_text("pathlib sample\n", encoding="utf-8")
	print("exists?", sample.exists())
	print("absolute:", sample.resolve())
	sample.unlink()

# example_os_path_methods()
```

8) Merge two small text files

```python
def example_merge_text_files():
	"""Create two small files and merge them into an output file."""
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
		if os.path.exists(p):
			os.remove(p)

# example_merge_text_files()
```


## Design / contract
- Inputs: CLI commands (`list`, `run <name>`, `run all`)  
- Outputs: console output describing each action and temporary files created  
- Success criteria: example runs without raising uncaught exceptions and cleans up its temporary files when implemented to do so

Edge cases considered:
- Running in a read-only directory will fail when creating files — run in a writable folder or run the script with appropriate permissions.  
- If a temporary file already exists, examples typically either overwrite it or remove it during cleanup.  
- Large-file merging should be implemented line-by-line to avoid excessive memory use (the current demos work with small files).

## Contributing
- If you want to add examples (CSV, JSON, binary streams, streaming large files), add a new function to `file.py` and register it in the examples registry (see the top of the file). Keep each example independent and ensure it cleans up created artifacts.

## License
You can reuse these examples in tutorials and on GitHub. Add a license file if you want stricter reuse conditions.

---

If you'd like, I can:
- turn the commented example functions in `file.py` into an uncommented registry and provide a complete `python file.py run <name>` runner, or
- create a short CONTRIBUTING.md with pull request guidelines and a checklist for adding examples.
