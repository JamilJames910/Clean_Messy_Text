# Messy Text Generator & Cleaner

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A robust Python utility for **generating messy, noisy text** and **cleaning it back** into readable form. This project is ideal for **text processing, NLP experiments, and data augmentation**.

---

## 🚀 Project Overview

Text data in the real world is rarely perfect — it may contain **typos, inconsistent casing, extra punctuation, emojis, or HTML tags**. This library provides two complementary tools:

1. **Messy Text Generator**  
   Introduce controlled noise into clean text with configurable levels:
   - Typos (swap, drop, duplicate, insert characters)
   - Random punctuation duplication
   - Mixed casing
   - Emoji and HTML insertion
   - Random whitespace variations

2. **Text Cleaner**  
   Recover clean text from noisy input using:
   - HTML unescaping and tag removal
   - Control/non-printable character removal
   - Punctuation normalization
   - Contraction expansion
   - Common typo fixes
   - Optional stopword removal

This dual functionality makes it perfect for testing **NLP pipelines, chatbots, AI text models, and data preprocessing**.

---

## 💡 Features

- Generate messy text with **adjustable noise levels**
- Correct typos, normalize punctuation, and **clean HTML/emoji artifacts**
- Expand common contractions (`can't` → `cannot`)
- Optional stopword removal for cleaner outputs
- Lightweight and easy-to-integrate Python module

---

## ⚙️ Installation

Clone this repository and ensure Python 3.10+ is installed:

```bash
git clone https://github.com/yourusername/messy-text-generator.git
cd messy-text-generator
pip install -r requirements.txt
````

> No external dependencies are strictly required; standard Python libraries (`re`, `html`, `random`, `string`) are sufficient.

---

## 🛠 Usage

### Generate Messy Text

```python
from messy_text import make_messy

text = "The quick brown fox jumps over the lazy dog."
messy_text = make_messy(text, noise_level=0.35)
print(messy_text)
```

### Clean Messy Text

```python
from messy_text import clean_text

messy_input = "ThE qui!ck brOwn fOx jum!ps over teh lazy dog!!!"
cleaned = clean_text(messy_input)
print(cleaned)
# Output: "the quick brown fox jumps over the lazy dog"
```

### Example with Both

```python
original = "I can't believe it's 2025! HTML <b>bold</b>, emojis, and typos."
messy = make_messy(original, noise_level=0.5)
restored = clean_text(messy)
```

---

## 🎯 Use Cases

* **Data augmentation** for NLP or machine learning pipelines
* **Testing chatbots** on noisy or user-generated input
* **Simulating human typos** in input fields
* **Text preprocessing pipelines** for AI models
* Cleaning legacy datasets with inconsistent formatting

---

## 📝 Contributing

Contributions, bug reports, and feature requests are welcome!
Please follow these steps:

1. Fork the repository
2. Create a branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m "Add new feature"`
4. Push branch: `git push origin feature/new-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🔗 References & Related Projects

* [NLTK](https://www.nltk.org/) – Python natural language toolkit
* [spaCy](https://spacy.io/) – Industrial-strength NLP
* [Text Augmentation Techniques](https://arxiv.org/abs/2003.02245) – Academic reference for text noise/augmentation

---

## 👩‍💻 Author

**Jamil James** – Passionate Python developer focused on **NLP, AI, and automation**.
GitHub: https://github.com/JamilJames910

```

