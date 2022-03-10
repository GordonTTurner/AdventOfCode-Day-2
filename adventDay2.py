# ---- PART I ----

instructions = [line.strip() for line in open('/content/drive/MyDrive/Advent/advent2.txt').readlines()]
forward = 0
depth = 0
for line in instructions:
  if 'forward' in line:
    forward += int(line[-1])
  else:
    depth += int(line[-1]) if 'down' in line else -int(line[-1])

print(f"Part I: Ship has gone {forward} m forward, {depth} m down, for {forward * depth} m in total.")

# ---- PART II ----

horizontal = 0
vertical = 0
aim = 0
for line in instructions:
  if 'forward' in line:
    horizontal += int(line[-1])
    vertical += aim * int(line[-1])
  else:
    aim += int(line[-1]) if 'down' in line else -int(line[-1])
print(f"Part II: Ship has gone {horizontal} m forward, {vertical} m down, for {horizontal * vertical} m in total.")
