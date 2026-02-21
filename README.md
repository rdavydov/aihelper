# aihelper

# Installation

```
mkdir -p ~/bin
chmod +x ~/bin/aihelper.py
echo 'alias ai="python3 ~/bin/aihelper.py"' >> ~/.bashrc
```

# Usage

```
$ ai rename all .jpeg to .jpg

  ➜  for file in *.jpeg; do mv "$file" "${file%.jpeg}.jpg"; done

Execute? [y/N]
```
