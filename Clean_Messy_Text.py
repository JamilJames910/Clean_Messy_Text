import random
import re 
import html 
import string 

# ----------------------------
# Messy text generator 
# ----------------------------

EMOJIS = ["🙂", "😂", "🔥", "👍", "🙈", "💥", "🤷‍♂️"]
HTML_TAGS = ["<b>", "<i>", "<span style='color:red'>", "<a href='#'>", "</a>", "</span>"]

def _random_typo(s:str) -> str: 
    """Introduce a simple random typo: swap, drop, duplicate, or insert char."""
    if len(s) < 2: 
        return s
    i = random.randrange(len(s))
    typo_type = random.choice(["swap", "drop", "dup", "insert"])
    if typo_type == "swap" and i < len(s)-1: 
        lst = list(s)
        lst[i], lst[i+1] = lst[i+1], lst[i]
        return "".join(lst)
    if typo_type == "drop": 
        return s[:i] + s[i+1:]
    if typo_type == "dup":
        return s[:i] + s[i] + s[i] + s[i+1:]
    # insert random number
    return s[:i] + random.choice(string.ascii_letters) + s[i:]

def make_messy(text: str, noise_level: float = 0.25) -> str: 
    """Turn clean text into messy text. 
    noise_level: 0.0 (no changes) .. 1.0 (lots of noise)"""

    tokens = re.split(r"(\s+)", text) # keep whitespace tokens 
    out = []
    for tok in tokens: 
        if tok.isspace(): 
            # randomize whitespace: sometimes extra spaces/newlines
            if random.random() < noise_level * 0.5: 
                out.append(random.choice([" ","  ","   ", "\n", "\n\n"]))
            else: 
                out.append(tok)
            continue

        # maybe change casing
        if random.random() < noise_level * 0.5: 
            tok = "".join(ch.upper() if random.random() < 0.4 else ch.lower() for ch in tok)

        # maybe add a typo inside token
        if random.random() < noise_level: 
            # apply type to a random substring of token: 
            i0 = random.randrange(len(tok))
            i1 = min(len(tok), i0 + random.randrange(1,3))
            bad = _random_typo(tok[i0:i1])
            tok = tok[:i0] + bad + tok[i1:]

        # maybe repeat punctuation or add random punctuation 
        if random.random() < noise_level * 0.4: 
            tok = re.sub(r"([.!?])$", lambda m: m.group(1) * random.randint(1,4), tok)

        # maybe insert emjoi or HTML
        if random.random() < noise_level * 0.2: 
            tok = random.choice(EMOJIS) + " " + tok
        if random.random() < noise_level * 0.15: 
            tag = random.choice(HTML_TAGS)
            tok = tag + tok + ("" if tag.startswith("</") else random.choice(["", "</b>", "</i","</span>"]))


        out.append(tok)
    
    # maybe add stray non-printable chars or control chars
    messy = "".join(out)
    if random.random() < noise_level * 0.1: 
        messy = messy + "\x0c" # form feed
    return messy 

# ----------------------------
# Cleaner 
# ----------------------------

CONTRACTIONS = {
    "can't": "can not", "won't": "will not", "n't": " not", "'re": " are", "'s": " is", 
    "'ll": " will", "'ve": " have", "'m": " am"
}

COMMON_FIXES = { 
    "teh": "the", 
    "recieve": "receive",
    "adn": "and",
    "liek": "like"
}

def clean_text(text: str, remove_stopwords: bool = False) -> str: 
    """Basic cleaning pipeline for messy input."""
    if text is None: 
        return ""
    
    # unescape HTML entities and strip HTML tags
    text = html.unescape(text)
    text = re.sub(r",[^>]+>", " ", text)

    # remove non-printable/control characters
    text = "".join(ch for ch in text if ch.isprintable())

    # normalize some emjois / keep them but separated 
    text = re.sub(r"([^\w\s'+-])", r" \1) ", text) # space punctuation so repeated punctuation becomes easy to collapse

    # collapse repeated punctuation: "!!!" -> "!"
    text = re.sub(r"([!?.,])\1+", r"\1)", text)

    # normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Lower-case safely 
    text = text.lower()

    # expand simple contractions 
    for k, v in CONTRACTIONS.items(): 
        text = text.replace(k,v)

    # quick common typo fixes (word boundaries)
    for bad, good in COMMON_FIXES.items(): 
        text = re.sub(rf"\b{re.escape(bad)}\b", good, text)


    # remove stray puntuation stuck to words (except inner apostrophes and hypens)
    text = re.sub(r"(?<=\w)[^\w\s'-]+(?=\w)"," ", text)

    text = re.sub(r"\s{2,}", " ", text).strip()


    # optional: remove stopwords (very small example set)
    if remove_stopwords:
        stop = {"the", "a", "an", "and", "or", "but", "is", "are"}
        words = [w for w in text.split() if w not in stop]
        text = " ". join(words)

    return text 


# ----------------------------
# Example usage 
# ----------------------------

if __name__ == "__main__":
    clean_example = ("The quick brown fox jumps over the lazy dog. "
                     "I can't believe it's already 2025! Let's test: HTML <b>bold</b>, emojis, and typos.")
    
    print("===ORIGINAL CLEAN TEXT ===")
    print(clean_example)
    print("\n=== GENERATED MESSY VERISONS ===")
    for lvl in (0.15, 0.35, 0.7):
        messy = make_messy(clean_example,noise_level=lvl)
        print(f"\n-- noise_level={lvl} --")
        print(messy)

        restored = clean_text(messy)
        print("\nrestored ->")
        print(restored)