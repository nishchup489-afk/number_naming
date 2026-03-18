from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# ================= BASE SETUP =================
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# ================= CORE LOGIC =================

ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
         "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", 
        "Sixty", "Seventy", "Eighty", "Ninety"]

SCALES = [
    "", "Thousand", "Million", "Billion", "Trillion",
    "Quadrillion", "Quintillion", "Sextillion", "Septillion",
    "Octillion", "Nonillion", "Decillion",

    "Undecillion", "Duodecillion", "Tredecillion", "Quattuordecillion",
    "Quindecillion", "Sexdecillion", "Septendecillion",
    "Octodecillion", "Novemdecillion", "Vigintillion",

    "Unvigintillion", "Duovigintillion", "Tresvigintillion",
    "Quattuorvigintillion", "Quinvigintillion", "Sesvigintillion",
    "Septemvigintillion", "Octovigintillion", "Novemvigintillion",

    "Trigintillion", "Untrigintillion", "Duotrigintillion",
    "Trestrigintillion", "Quattuortrigintillion",
    "Quintrigintillion", "Sestrigintillion",
    "Septentrigintillion", "Octotrigintillion",
    "Novemtrigintillion",

    "Quadragintillion", "Unquadragintillion", "Duoquadragintillion",
    "Tresquadragintillion", "Quattuorquadragintillion",
    "Quinquadragintillion", "Sesquadragintillion",
    "Septenquadragintillion", "Octoquadragintillion",
    "Novemquadragintillion",

    "Quinquagintillion", "Unquinquagintillion", "Duoquinquagintillion",
    "Tresquinquagintillion", "Quattuorquinquagintillion",
    "Quinquinquagintillion", "Sesquinquagintillion",
    "Septenquinquagintillion", "Octoquinquagintillion",
    "Novemquinquagintillion",

    "Sexagintillion", "Unsexagintillion", "Duosexagintillion",
    "Tresexagintillion", "Quattuorsexagintillion",
    "Quinsexagintillion", "Sesexagintillion",
    "Septensexagintillion", "Octosexagintillion",
    "Novemsexagintillion",

    "Septuagintillion", "Unseptuagintillion", "Duoseptuagintillion",
    "Treseptuagintillion", "Quattuorseptuagintillion",
    "Quinseptuagintillion", "Seseptuagintillion",
    "Septenseptuagintillion", "Octoseptuagintillion",
    "Novemseptuagintillion",

    "Octogintillion", "Unoctogintillion", "Duooctogintillion",
    "Tresoctogintillion", "Quattuoroctogintillion",
    "Quinoctogintillion", "Sesoctogintillion",
    "Septemoctogintillion", "Octooctogintillion",
    "Novemoctogintillion",

    "Nonagintillion", "Unnonagintillion", "Duononagintillion",
    "Tresnonagintillion", "Quattuornonagintillion",
    "Quinnonagintillion", "Sesnonagintillion",
    "Septennonagintillion", "Octononagintillion",
    "Novemnonagintillion",

    "Centillion"
]

def get_hundred(n: int) -> str:
    parts = []

    hundreds = n // 100
    rest = n % 100

    if hundreds > 0:
        parts.append(ONES[hundreds] + " Hundred")

    if rest > 0:
        if rest < 10:
            parts.append(ONES[rest])
        elif 10 <= rest < 20:
            parts.append(TEENS[rest - 10])
        else:
            tens = rest // 10
            ones = rest % 10

            if tens > 0:
                parts.append(TENS[tens])
            if ones > 0:
                parts.append(ONES[ones])

    return " ".join(parts)


def get_name(number: int) -> str:
    if number == 0:
        return "Zero"

    temp = number
    chunk_list = []

    while temp > 0:
        chunk_list.append(temp % 1000)
        temp //= 1000

    name_parts = []

    for i, chunk in enumerate(chunk_list):
        if chunk == 0:
            continue

        chunk_name = get_hundred(chunk)
        scale = SCALES[i]

        if scale:
            name_parts.append(f"{chunk_name} {scale}")
        else:
            name_parts.append(chunk_name)

    return " ".join(name_parts[::-1])


# ================= ROUTES =================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": None
    })


@app.post("/convert", response_class=HTMLResponse)
def convert(request: Request, number: str = Form(...)):
    try:
        num = int(number)
        result = get_name(num)
    except ValueError:
        result = "Invalid input. Please enter a valid number."

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "input": number
    })