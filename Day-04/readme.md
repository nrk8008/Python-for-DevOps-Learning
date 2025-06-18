# 🐍 Creating and Activating a Python Virtual Environment on Ubuntu

Follow these steps to create and activate a Python virtual environment using `venv`.

---

## ✅ Step 1: Install `python3-venv` (If Not Already Installed)

```bash
sudo apt update
sudo apt install python3-venv -y
```

This installs the required module for creating virtual environments.

---

## ✅ Step 2: Create a Virtual Environment

```bash
python3 -m venv project-abc
```

This will create a directory named `project-abc/` with the following structure:

```
project-abc/
├── bin/
├── lib/
└── pyvenv.cfg
```

---

## ✅ Step 3: Activate the Virtual Environment

```bash
source project-abc/bin/activate
```

Once activated, your shell prompt will change to:

```
(project-abc) your-username@your-machine:~$
```

---

## ✅ Step 4: Verify Activation

Check the paths to make sure you're using the virtual environment's Python and pip:

```bash
which python
which pip
```

They should point to the `project-abc/bin/` directory.

---

## ✅ Step 5: Deactivate When Done

To deactivate the virtual environment:

```bash
deactivate
```

---

## 📝 Notes

- Always activate the virtual environment before installing Python packages for your project.
- Each project can have its own isolated virtual environment to avoid version conflicts.

