odd_list = []
even_list = []
with open('./words.txt', 'r')as f:
    lines = f.readlines()
    for line in lines:
        odd,even = line.split()
        odd_list.append(odd)
        even_list.append(even)

print(odd_list)
print(even_list)
print("odd_list length:", len(odd_list))
print("even_list length:", len(even_list))
