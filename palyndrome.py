def palyndrome (word) :
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and palyndrome(word[1:-1])

def palyndorme_banale(word):
    return word[::-1] == word

if __name__ == "__main__":
    print(palyndrome("casa"))
    print(palyndrome("civic"))
    print(palyndorme_banale("casa"))
    print(palyndorme_banale("civic"))

