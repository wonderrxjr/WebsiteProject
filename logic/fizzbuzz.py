def generate_fizzbuzz(n):
    """Return a FizzBuzz sequence as a list of strings."""
    if n is None:
        return []

    try:
        n = int(n)
    except (TypeError, ValueError):
        return []

    if n < 1:
        return []

    if n > 1000:
        n = 1000

    results = []
    for i in range(1, n + 1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if out == "":
            out += str(i)
        results.append(out)

    return results
