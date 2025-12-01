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
