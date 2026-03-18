# 🔢 Number to Words Converter

**Project 14 of 100 Python Live Projects**

**Live Preview:** [https://number-words.onrender.com](https://number-words.onrender.com)

**GitHub Repo:** [(https://github.com/nishchup489-afk/number_naming)](https://github.com/nishchup489-afk/number_naming)

**CLI Version:** `sample.py`

---

## 🚀 Project Overview

Convert any integer into its English word representation using a **scalable chunk-based system**.

### Examples

```
7 → Seven
42 → Forty Two
107 → One Hundred Seven
1234567 → One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
```

This project evolved from a simple CLI script into a **reusable number parsing engine**, and finally into a **FastAPI web application**.

---

## 🧠 Why This Project Matters

This is not just a beginner project — it's a **mini system design exercise**.

You learn:

* Breaking complex problems into smaller reusable units
* Clean handling of edge cases
* Mathematical decomposition over fragile string hacks
* Writing scalable logic instead of hardcoding
* Separating business logic from UI and routes

👉 Translation: You stopped writing scripts and started thinking like an engineer.

---

## ⚙️ Features

### 🖥 CLI Version

* Accepts integer input
* Converts number into words
* Handles zero correctly
* Supports very large numbers via scale system

### 🌐 Web Version (FastAPI)

* Input via HTML form
* Renders result dynamically
* Clean separation of logic and routes
* Uses Jinja templates for rendering

---

## 🧩 Core Idea Behind the Logic

> Numbers are not processed digit-by-digit — they are processed in chunks of 3.

Because English naming works like:

```
1 Million
234 Thousand
567
```

### Example

```
1234567 → [567, 234, 1]
```

Each chunk is converted independently, then scale names are attached.

---

## 🏗 Building Blocks

### 1. ONES

```
ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
```

### 2. TEENS

```
TEENS = ["Ten", "Eleven", "Twelve", ...]
```

### 3. TENS

```
TENS = ["", "", "Twenty", "Thirty", "Forty", ...]
```

### 4. SCALES

```
["", "Thousand", "Million", "Billion", "Trillion", ...]
```

⚠️ Important Design Insight:

* **Hundred belongs inside a chunk**
* **Thousand+ belongs outside chunks**

---

## 🔍 Step-by-Step Logic

### Step 1: Convert 0–999 (`get_hundred(n)`)

Break number:

$$
\text{hundreds} = n // 100
$$

$$
\text{rest} = n % 100
$$

Example:

```
342 → Three Hundred Forty Two
107 → One Hundred Seven
700 → Seven Hundred
```

👉 Uses a `parts` list to avoid:

* trailing spaces
* "Zero" bugs
* ugly formatting

---

### Step 2: Split into Chunks

```
number % 1000
number //= 1000
```

Example:

```
1234567 → [567, 234, 1]
```

---

### Step 3: Attach Scale Names

| Index | Scale    |
| ----- | -------- |
| 0     | ""       |
| 1     | Thousand |
| 2     | Million  |

Skip zero chunks to avoid garbage output.

---

### Step 4: Reverse and Join

```
["567", "234 Thousand", "1 Million"]
→ Reverse → Join
```

Final:

```
One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
```

---

## 🔄 Full Flow

1. If number == 0 → return "Zero"
2. Split into chunks
3. Convert each chunk
4. Attach scale names
5. Reverse
6. Join

---

## ❌ Earlier Mistakes (and Why They Failed)

### 1. Digit-Level Thinking

→ Breaks at scale

### 2. Hardcoding Cases

→ Not scalable

### 3. Wrong Scale Design

→ Mixed "Hundred" incorrectly

### 4. Mixing Chunk + Conversion

→ Messy logic

👉 Fix: **First chunk, then process**

---

## 🖥 CLI Version Explained

### Input

```
number = int(input())
```

### Conversion

```
get_name(number)
```

### Output

```
print(result)
```

### Error Handling

Use `try/except` to prevent crashes.

---

## 🌐 FastAPI Version Explained

### Structure

```
app = FastAPI()
templates = Jinja2Templates(...)
```

### Flow

* GET → show form
* POST → process input
* Call core logic
* Return result to template

---

## 🎭 Jinja Role

Jinja injects backend data into HTML.

```
{{ result }}
```

Simple, clean, and effective.

---

## 🔁 Web Flow

1. User enters number
2. POST request sent
3. Backend processes
4. Template renders result

---

## 🧪 Edge Cases Handled

* Zero → "Zero"
* Teens → correct names
* Exact hundreds → clean output
* Missing chunks → skipped
* Large numbers → supported via scales

---

## ⚠️ Limitations

* Integers only
* No decimals
* No currency formatting
* Scale list is finite

---

## 📈 Future Improvements

* Negative numbers → "Minus Forty Two"
* Decimal support → "Point"
* Currency mode
* Copy button (UI)
* JSON API endpoint
* Huge number validation

---

## 🧠 What You Learned

### Programming

* Decomposition
* Clean function design
* Mathematical thinking
* Defensive coding

### Backend

* FastAPI basics
* Template rendering
* Input validation

### Engineering Mindset

> Build one strong unit → reuse everywhere

That unit here is:

```
get_hundred()
```

---

## 📁 Folder Structure

```
project/
│
├── main.py
├── sample.py
└── templates/
    └── index.html
```

---

## 🧾 Summary

This project converts numbers into words by:

* Splitting into 3-digit chunks
* Converting each chunk independently
* Attaching scale names
* Combining into final output

---

## 🏁 Final Thought

You didn’t just write a converter.

You built a **number parsing engine**.

And that shift — from script to system — is where real engineering begins. 🚀
