# aihelper

A handy CLI tool that uses AI to generate and optionally execute shell commands from natural language prompts.

## Prerequisites

- Python 3.6 or higher installed on your system.
- The `aihelper.py` script (place it in a convenient location).

## Installation

### Linux & macOS

1. **Place the script**  
   Copy `aihelper.py` to `~/bin/` (create the directory if it doesn't exist):
   ```bash
   mkdir -p ~/bin
   cp /path/to/aihelper.py ~/bin/
   ```

2. **Make it executable**  
   ```bash
   chmod +x ~/bin/aihelper.py
   ```

3. **Create an alias**  
   Add the following line to your shell configuration file (`~/.bashrc` for Bash, `~/.zshrc` for Zsh, or `~/.bash_profile` on macOS):
   ```bash
   alias ai="python3 ~/bin/aihelper.py"
   ```
   Then reload the configuration:
   ```bash
   source ~/.bashrc   # or source ~/.zshrc / ~/.bash_profile
   ```

### Windows

1. **Place the script**  
   Create a folder for your scripts, e.g., `C:\Users\YourName\bin`, and copy `aihelper.py` there.

2. **Ensure Python is in your PATH**  
   During Python installation, check the option **"Add Python to PATH"**. Verify by opening a new Command Prompt and running:
   ```cmd
   python --version
   ```

3. **Create an alias (PowerShell)**  
   - Open your PowerShell profile configuration:
     ```powershell
     notepad $PROFILE
     ```
     (If the file doesn't exist, it will ask to create it.)
   - Add the following function:
     ```powershell
     function ai { python C:\Users\YourName\bin\aihelper.py $args }
     ```
   - Save and reload the profile:
     ```powershell
     . $PROFILE
     ```

   **For Command Prompt (cmd.exe)**, you can create a batch file:
   - Create a new file `ai.cmd` in a folder that is in your `PATH` (e.g., `C:\Windows` or a custom folder added to `PATH`), containing:
     ```cmd
     @python C:\Users\YourName\bin\aihelper.py %*
     ```

## Usage

Once installed, simply prefix your natural language request with `ai`:

```bash
$ ai rename all .jpeg to .jpg

  ➜  for file in *.jpeg; do mv "$file" "${file%.jpeg}.jpg"; done

Execute? [y/N]
```

The tool will suggest a command and ask for confirmation before executing it.

---

**Note:** The exact behavior of the alias/function may vary slightly between shells, but the core functionality remains the same. Adjust paths to match your actual script location.
