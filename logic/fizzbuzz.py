def generate_fizzbuzz(n):
    """Return a FizzBuzz sequence as a newline-delimited string."""
    if n is None:
        n = 0

    try:
        n = int(n)
    except (TypeError, ValueError):
        return ""

    if n < 0:
        n = 0

    fullout = ""
    for i in range(1, n + 1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if out == "":
            out += str(i)
        fullout += out + "\n"

    return fullout
