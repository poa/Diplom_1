from testconst import Bun, Filling, Sauce


class TData:
    bun = Bun()
    filling = Filling()
    sauce = Sauce()

# list(filter(lambda s: not s.startswith("__"), dir(Bun)))