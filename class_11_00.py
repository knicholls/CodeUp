directions = []
streets = []

while True:
    direction = input(str())
    street = input(str())

    directions.append(direction)
    streets.append(street)

    if street == "SCHOOL":
        break

directions.reverse()
streets.reverse()

for x in range(len(directions)):
    if directions[x] == 'R':
        reverse_direction = 'LEFT'
    else:
        reverse_direction = 'RIGHT'

    if x == len(directions) - 1:
        print(f"Turn {reverse_direction} into your HOME.")
    else:
        print(f"Turn {reverse_direction} onto {streets[x + 1]} street.")
