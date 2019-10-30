# Solution for - https://open.kattis.com/problems/summertrip
__author__ = "Taras Basiuk"

s = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = 0

for c in alphabet:

    # Find the first occurrence of the character
    i = s.find(c)
    if i == -1:
        continue

    # Keep track of encountered characters which are not c
    seen = set()

    # Iterate through other characters
    i += 1
    while i < len(s):
        if s[i] == c:
            # If c is encountered again, reset the seen characters, new start event established
            seen = set()
        else:
            if s[i] not in seen:
                # Found a new character in a substring starting with c, it can work as last event in the itinerary
                seen.add(s[i])
                result += 1

        i += 1

print(result)
