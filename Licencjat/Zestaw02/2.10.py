def liczenie(line):
    x = len(line.split())
    return x;
# przykladowy input
line = "\tAla  ma\ndwa\t\tkoty "
print(f"Input: {line}\nLiczba słow: {liczenie(line)}")