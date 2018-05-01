import json

x = ["aaaa", 13, 28, 50, 74, 108, 148, 171, 192, 203, 208, 209, 207, 184, 169, 151, 137, 129, 119, 113, 109, 105, 102, 101, 100, 101, 102, "aaaa", 381, 381, 380, 377, 372, 369, 368, 369, 379, 408, 449, 494, 534, 601, 628, 646, 662, 668, "aaaa", 626, 632, 638, 655, 671, 695, 715, 742, 755, 762, 764, 761, 746, 731, 714, 699, 693, "aaaa", 905, 908, 914, 922, 933, 949, 962, 972, 979, 985, 987, 989, 990, 991, 997, 1008, 1019, 1033, 1046, 1059, 1069, 1076, 1080, 1085, 1088, 1092, 1095, 1099, 1101, 1103, 1104, 1105, "aaaa"]
y = ["aaaa", 31, 31, 31, 31, 31, 35, 40, 48, 58, 68, 84, 102, 136, 150, 163, 172, 175, 179, 181, 183, 184, 184, 185, 185, 185, 184, "aaaa", 50, 55, 69, 91, 137, 170, 207, 235, 255, 276, 288, 293, 294, 290, 283, 278, 270, 266, "aaaa", 22, 22, 22, 24, 27, 33, 41, 58, 78, 103, 145, 170, 201, 218, 232, 238, 238, "aaaa", 12, 17, 31, 45, 64, 87, 105, 117, 127, 135, 140, 142, 143, 143, 143, 139, 136, 129, 122, 115, 109, 103, 99, 95, 91, 87, 84, 82, 80, 79, 79, 79, "aaaa"]


def parse(x , y):

    length = len(x)

    var = []

    i = 1

    while(i < length):
        temp_x=[]
        temp_y=[]

        while(x[i] != "aaaa"):
            if (i % 3 == 0):
                temp_x.append(x[i])
                temp_y.append(y[i])
            i = i + 1
        temp_total=[]
        temp_total.append(temp_x)
        temp_total.append(temp_y)
        var.append(temp_total)
        i += 1
    # print(var)
    return var

var = parse(x, y)

data = json.dumps({"drawing": var})
print(data)

fileObject = open('inputData.json', 'w')
fileObject.write(data)
fileObject.close()