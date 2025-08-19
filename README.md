# Clean Messy Text 📝

A Python script to generate messy text and clean it back to readable form.
Perfect for testing text preprocessing pipelines, NLP models, or just having fun with typos, emojis, and HTML noise.

## Features ✨

✅ Generate messy text with typos, random casing, extra punctuation, emojis, and HTML tags.  
✅ Clean messy text back to readable form.  
✅ Handles HTML entities and tags.  
✅ Fixes common typos and contractions.  
✅ Optionally remove basic stopwords.  
✅ Adjustable noise level for messiness.


## Table of Contents

* [Installation](#installation-🛠️)
* [Usage](#usage-💻)
* [Example](#example)
* [Project Structure](#project-structure-🗂️)
* [Contributing](#contributing-🤝)
* [Contact](#contact-✉️)

## Installation 🛠️

Clone this repository:

```bash
git clone https://github.com/JamilJames910/Clean_Messy_Text.git
cd Clean_Messy_Text
```

Make sure you have Python 3.x installed.

No additional dependencies are required—Python's built-in modules handle everything (`random`, `re`, `html`, `string`).

## Usage 💻

Run the script:

```bash
python Clean_Messy_Text.py
```

You can use the functions in your own scripts:

```python
from Clean_Messy_Text import make_messy, clean_text

text = "The quick brown fox jumps over the lazy dog."
messy = make_messy(text, noise_level=0.3)
restored = clean_text(messy)
print(messy)
print(restored)
```

### Key Functions

* **`make_messy(text, noise_level)`**: Turn clean text into messy text.

  * `noise_level`: `0.0` (no changes) to `1.0` (lots of noise)
* **`clean_text(text, remove_stopwords=False)`**: Clean messy input and fix typos.

  * `remove_stopwords=True` removes simple common stopwords.

## Example

```python
clean_example = "I can't believe it's already 2025! Let's test: HTML <b>bold</b>, emojis, and typos."
```

Generate messy versions:

```python
for lvl in (0.15, 0.35, 0.7):
    messy = make_messy(clean_example, noise_level=lvl)
    print(f"\n-- noise_level={lvl} --")
    print(messy)

    restored = clean_text(messy)
    print("\nrestored ->")
    print(restored)
```

Output might look like:

```
-- noise_level=0.35 --
🙂 I Cna't believE it s a lready 2025!! <b>bold</b> emoj i s!!
restored ->
i can not believe it is already 2025 ! bold emojis and typos .
```

## Project Structure 🗂️

```
Clean_Messy_Text
├── Clean_Messy_Text.py   # Main script
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Contributing 🤝

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

## Contact ✉️

Created with ❤️ by Jamil James

GitHub: [JamilJames910](https://github.com/JamilJames910)
Email: [Jamil.i.James1@gmail.com](mailto:Jamil.i.James1@gmail.com)
