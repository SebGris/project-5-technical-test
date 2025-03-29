def square(x):
    """Function to calculate the square of a number."""
    if not isinstance(x, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return x * x
