# The foundational building blocks
ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# Special case for 10-19 because they don't follow the "Tens + Ones" pattern
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
         "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

# Multiples of ten
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

# Large scale denominators (Near Googol)
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

try:
    number = int(input("Enter your number:  "))
except ValueError:
    print("Numbers only")

def get_hundred(n):
    parts = []

    hundreds = n // 100
    rest = n % 100

    if hundreds > 0:
        parts.append(ONES[hundreds] + " Hundred")

    # Tens & Ones
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



def get_name(number):
    if number == 0:
        name = "Zero"
        return name

    chunk_list = []
    
    while number > 0:
        chunk_list.append(number % 1000)
        number //= 1000

    name_parts = []

    for i , chunk in enumerate(chunk_list):
        if chunk == 0:
            continue

        chunk_name = get_hundred(chunk)
        scale = SCALES[i]

        if scale :
            name_parts.append(chunk_name + " " + scale)
        else :
            name_parts.append(chunk_name)
    return " ".join(name_parts[::-1])

print(get_name(number))

