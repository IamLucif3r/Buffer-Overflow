#This Scripts generate all bad characters to be used in the exploit script
for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()