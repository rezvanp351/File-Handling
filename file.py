# file.py
# Python File Handling — Independent runnable examples via CLI
# Usage:
#   python file.py list
#   python file.py run write
#   python file.py run read
#   python file.py run all

import os
import shutil
import argparse
from pathlib import Path

# ---------------------------
# Example functions (each independent)
# ---------------------------

# def example_write_files():
#     """
#     Example: write text and binary files (independent).
#     Explanation (printed + comments):
#       - This example demonstrates how to create and write to a text file using the
#         built-in open() with 'w' mode and how to create a small binary file using 'wb'.
#       - Files created here are removed at the end so the example is self-contained.
#     """
#     print("\n--- example_write_files ---")
#     print("Demonstration: create a text file with text content, and a binary file.")
#     # Create a text file and write UTF-8 text to it
#     text_path = "ex_write.txt"
#     with open(text_path, "w", encoding="utf-8") as f:
#         f.write("Hello — this file was created by example_write_files()\n")
#     print("Created:", text_path)

#     # Create a binary file and write raw bytes
#     binary_path = "ex_write.bin"
#     with open(binary_path, "wb") as f:
#         f.write(bytes(range(8)))  # writes bytes 0..7
#     print("Created binary:", binary_path)

#     # Cleanup: remove created files so example remains independent
#     for p in (text_path, binary_path):
#         if os.path.exists(p):
#             os.remove(p)
#             print("Removed:", p)
# example_write_files()

# def example_read_files():
#     """
#     Example: create a file and then read it (independent).
#     Explanation:
#       - Shows how to write a file and then open it for reading.
#       - Demonstrates reading the entire file content into a string with read().
#       - Cleans up the temporary file at the end.
#     """
#     print("\n--- example_read_files ---")
#     print("Demonstration: create a text file, read its full content, then delete it.")
#     fname = "ex_read.txt"

#     # Create the file to ensure the read operation always succeeds (self-contained)
#     with open(fname, "w", encoding="utf-8") as f:
#         f.write("This file is created by example_read_files()\nLine 2\n")
#     print("Created for reading:", fname)

#     # Read the entire file into memory and print it
#     with open(fname, "r", encoding="utf-8") as f:
#         content = f.read()
#     print("Content:\n", content)

#     # Cleanup the temporary file
#     os.remove(fname)
#     print("Removed:", fname)
# example_read_files()

# def example_rename_delete():
#     """
#     Example: rename a file then delete it (independent).
#     Explanation:
#       - Demonstrates using os.rename() to change a filename.
#       - Then shows os.remove() to delete the renamed file.
#       - The example creates its own source file so it does not depend on external state.
#     """
#     print("\n--- example_rename_delete ---")
#     print("Demonstration: create a file, rename it, then delete it.")
#     a = "ex_rename_src.txt"
#     b = "ex_rename_dst.txt"

#     # Create the source file
#     with open(a, "w", encoding="utf-8") as f:
#         f.write("rename me\n")
#     print("Created:", a)

#     # Rename the file (moves or renames depending on platform)
#     os.rename(a, b)
#     print("Renamed ->", b)

#     # Delete the renamed file
#     # os.remove(b)
#     # print("Deleted:", b)
# example_rename_delete()

# def example_directories():
#     """
#     Example: create and remove a directory (independent).
#     Explanation:
#       - Demonstrates os.makedirs() to create nested directories.
#       - Shows os.listdir() to list directory contents.
#       - Demonstrates shutil.rmtree() to remove an entire directory tree.
#       - All operations target a directory unique to this example.
#     """
#     print("\n--- example_directories ---")
#     print("Demonstration: create nested directories, list, then remove them.")
#     dirname = "ex_dir_folder"

#     # Create nested directory 'ex_dir_folder/sub'
#     os.makedirs(os.path.join(dirname, "sub"), exist_ok=True)
#     print("Created:", dirname, "with sub/")

#     # List current directory entries (showing first 10 for brevity)
#     print("Listing current dir (first 10 entries):", os.listdir(".")[:10])

#     # # Remove the directory tree created above
#     # shutil.rmtree(dirname)
#     # print("Removed directory tree:", dirname)
# example_directories()

def example_file_methods():
    """
    Example: tell(), seek(), truncate() (independent).
    Explanation:
      - Uses a file opened in 'w+' mode (write + read).
      - Demonstrates f.write(), f.flush(), f.tell() to get file pointer,
        f.seek() to move the pointer, f.read() to read from the pointer,
        and f.truncate() to shorten the file.
      - Deletes the temporary file after the demo.
    """
    print("\n--- example_file_methods ---")
    print("Demonstration: write to file, inspect and move pointer, truncate file.")
    fname = "ex_methods.txt"

    # Open file for writing and reading
    with open(fname, "w+", encoding="utf-8") as f:
        f.write("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")  # write data
        f.flush()  # ensure data is flushed to disk
        print("Wrote and flushed to", fname)

        # tell() returns the current file pointer offset in bytes
        pos = f.tell()
        print("tell() ->", pos)

        # seek(0) moves pointer to file start, then read 10 characters
        f.seek(0)
        head = f.read(10)
        print("First 10 bytes:", head)

        # truncate(5) shortens the file to 5 bytes from the start
        f.seek(0)
        f.truncate(5)
        f.seek(0)
        print("After truncate, content:", f.read())

    # Remove the file to keep the example independent
    os.remove(fname)
    print("Removed:", fname)


# def example_os_file_directory_methods():
#     """
#     Example: os.stat, os.access, mkdir, rmdir (independent).
#     Explanation:
#       - Demonstrates os.stat() to get file metadata (size, timestamps).
#       - Demonstrates os.access() to check permissions like readability.
#       - Creates and removes a temporary directory using os.mkdir() and os.rmdir().
#       - Cleans up the temporary file created for metadata inspection.
#     """
#     print("\n--- example_os_file_directory_methods ---")
#     print("Demonstration: get file metadata, check access, create/remove a dir.")
#     fname = "ex_osfile.txt"

#     # Create a temporary file for stat/access demonstration
#     with open(fname, "w", encoding="utf-8") as f:
#         f.write("os methods\n")
#     st = os.stat(fname)
#     print("os.stat -> size:", st.st_size, "mtime:", st.st_mtime)
#     print("Readable:", os.access(fname, os.R_OK))

#     # Create and remove a temporary directory
#     dname = "ex_os_dir"
#     os.mkdir(dname)
#     print("Created dir:", dname)
#     os.rmdir(dname)
#     print("Removed dir:", dname)

#     # Remove the temporary file used for demonstration
#     os.remove(fname)
#     print("Removed file:", fname)

# example_os_file_directory_methods()

# def example_os_path_methods():
#     """
#     Example: os.path and pathlib usage (independent).
#     Explanation:
#       - Uses pathlib.Path to create a small file and shows how to check existence
#         and resolve an absolute path.
#       - Demonstrates Path.write_text() and Path.unlink() for cleanup.
#     """
#     print("\n--- example_os_path_methods ---")
#     print("Demonstration: use pathlib to write a file, check path, and remove it.")
#     sample = Path("ex_path_sample.txt")

#     # Write a short text using pathlib convenience method
#     sample.write_text("pathlib sample\n", encoding="utf-8")
#     print("Path exists?", sample.exists())
#     print("Absolute:", sample.resolve())

#     # Remove created sample file
#     sample.unlink()
#     print("Removed:", sample)


# def example_merge_text_files():
#     """
#     Example: create two files and merge them into one (independent).
#     Explanation:
#       - Creates two temporary text files, opens a new output file, and copies
#         the contents of the two input files into the output file sequentially.
#       - Demonstrates basic file reading and writing, and then deletes all files.
#     """
#     print("\n--- example_merge_text_files ---")
#     print("Demonstration: create two text files, merge them into a third file.")
#     a = "ex_merge_a.txt"
#     b = "ex_merge_b.txt"
#     out = "ex_merged.txt"

#     # Create two input files
#     with open(a, "w", encoding="utf-8") as f:
#         f.write("Content A\n")
#     with open(b, "w", encoding="utf-8") as f:
#         f.write("Content B\n")

#     # Merge the two into a single output file
#     with open(out, "w", encoding="utf-8") as m:
#         for p in (a, b):
#             with open(p, "r", encoding="utf-8") as src:
#                 m.write(src.read())
#     print("Created merged:", out)

#     # Cleanup created files so the example remains self-contained
#     # for p in (a, b, out):
#     #     os.remove(p)
#     #     print("Removed:", p)
# example_merge_text_files()

# ---------------------------
# Registry: map short names to functions & descriptions
# ---------------------------
# EXAMPLES = {
#     "write": (example_write_files, "Write text & binary files (independent)"),
#     "read": (example_read_files, "Create & read a file (independent)"),
#     "rename": (example_rename_delete, "Rename then delete a file (independent)"),
#     "dirs": (example_directories, "Create and remove directories (independent)"),
#     "methods": (example_file_methods, "tell/seek/truncate example (independent)"),
#     "os": (example_os_file_directory_methods, "os.stat / mkdir / rmdir (independent)"),
#     "path": (example_os_path_methods, "os.path & pathlib example (independent)"),
#     "merge": (example_merge_text_files, "Merge two text files (independent)"),
#     "all": (None, "Run all examples one-by-one (independent)"),
# }


