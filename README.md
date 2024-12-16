# Bubble Git

Bubble Git is a lightweight, custom implementation of a version control system inspired by Git. It is built from scratch, focusing on the fundamental internals of how Git works. 

Currently, the implementation is written in Python, with plans to rewrite it in Rust for improved performance and safety. This project is a learning and exploratory tool for understanding Git's internals, providing insight into how hashing, trees, and basic version control operations work.

---

## **Features Implemented So Far**

The following commands are currently available in Bubble Git:

1. **`init`**: Initializes a new Bubble Git repository.
2. **`hash-object`**: Computes the SHA-1 hash of a file and stores it in the Bubble Git object database.
3. **`cat-file`**: Reads and outputs the contents of a Git object stored in the database.
4. **`write-tree`**: Generates a tree object representing the current directory structure.
5. **`read-tree`**: Reads a tree object and restores the directory structure in the working directory.

### **Planned Features**
The following features are under development:

- **`commit`**: Record changes to the repository.
- **`log`**: Display the commit history.
- **`branch`**: Manage branches within the repository.
- **`checkout`**: Switch between branches or commits.

---

## **Getting Started**

### **1. Requirements**
To run the Python implementation of Bubble Git, ensure you have:
- Python 3.8 or later
- `pip` for managing Python packages

### **2. Installation**
To set up Bubble Git locally, clone the repository and install it in **editable mode**:

```bash
# Clone the repository
git clone https://github.com/your-repo/bubble-git.git
cd py-impl

#Start the virtual environment
source bin/activate

# Install in editable mode
pip3 install -e .
```

#### **Why `pip3 install -e .`?**
The `-e` or `--editable` flag installs the package in a way that links the source code directory directly to your Python environment. This is especially useful during development, as it allows any changes you make to the source code to be immediately reflected when running the commands, without needing to reinstall the package.

---

## **Usage**

After installing Bubble Git, you can use it by running the following commands in the terminal:

1. **Initialize**:
   ```bash
   bubble-git init
   ```

2. **Hash a file and store its object**:
   ```bash
   bubble-git hash-object <file>
   ```

3. **Read an object**:
   ```bash
   bubble-git cat-file <object-hash>
   ```

4. **Write the directory tree to a tree object**:
   ```bash
   bubble-git write-tree
   ```

5. **Read a tree object and restore the directory structure**:
   ```bash
   bubble-git read-tree <tree-hash>
   ```

For planned commands like `commit`, `log`, `branch`, and `checkout`, stay tuned for updates!

---

## **Future Plans**
- Implement the remaining Git-like commands (`commit`, `log`, `branch`, `checkout`).
- Rewrite the entire implementation in Rust for better performance.
- Add comprehensive tests and documentation.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
