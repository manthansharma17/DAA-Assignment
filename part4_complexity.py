# -------------------------
# Single Loop
# -------------------------

print("Single Loop:")

count = 0

for i in range(1, 6):
    print(i)
    count = count + 1

print("Single loop runs:", count)


# -------------------------
# Single Loop for n = 20
# -------------------------

n = 20
count = 0

for i in range(1, n + 1):
    count = count + 1

print("\nFor n = 20:")
print("Single loop runs:", count)


# -------------------------
# Nested Loop
# -------------------------

print("\nNested Loop:")

count = 0

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        count = count + 1

print("Nested loop total prints:", count)


# -------------------------
# Nested Loop for n = 10
# -------------------------

n = 10
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        count = count + 1

print("\nFor n = 10:")
print("Nested loop runs:", count)