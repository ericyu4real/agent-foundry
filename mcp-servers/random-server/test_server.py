from server import random_choice, random_integer


value = random_integer(3, 3)
assert value == 3
assert random_choice(["agent", "tool"]) in {"agent", "tool"}

try:
    random_integer(2, 1)
except ValueError:
    pass
else:
    raise AssertionError("reversed bounds should fail")

try:
    random_choice([])
except ValueError:
    pass
else:
    raise AssertionError("empty choices should fail")

print("random-server checks passed")
