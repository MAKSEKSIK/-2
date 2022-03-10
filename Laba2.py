len_ = 0
len_temp = 0
position = 0
position_temp = -1
sequence = []

with open("Laba2-txt.txt", "r") as f:
    sequence = f.read().split()
    print("Исходная последовательность: ", sequence)

for temp in range(0, len(sequence)-1):
    if int(sequence[temp]) == int(sequence[temp+1]):
        len_temp += 1
        if position_temp == -1:
            position_temp = temp+1
    else:
        len_temp = 0
        position_temp = -1
    if len_temp > len_:
        len_ = len_temp+1
        position = position_temp

if len_ != 0:
    del sequence[position+len_-1:]
    del sequence[0:position-1]
    print ("Самая длинная последовательность: ", sequence)
    print ("Длинна последовательности: ", len_)
    print ("Позиция, с которой началась последовательность: ", position)
else:
    print ("В данном файле последовательностей, состоящих из повтора одной и той же цифры, нет")
