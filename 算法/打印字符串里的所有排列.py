import copy


def string_to_list(string):
    ls = []
    for char in string:
        ls.append(char)
    return ls


def add_char_to_er_list(newchar, ls):  # 向二维数组中插入数据
    newls = []
    for i in range(0, len(ls) + 1):
        temp = copy.deepcopy(ls)  # 使用 a[:], list(a),
        # a*1, copy.copy(a)四种方式复制列表
        # 结果都可以得到一个新的列表，但是如果列表中含有列表，所有
        # b, c, d, e四个新列表的子列表都是指引到同一个对象上。
        # 只有使用copy.deepcopy(a)方法得到的新列表f才是包括子列表
        # 在内的完全复制。
        temp.insert(i, newchar)
        newls.append(temp)
    return newls


def add_char_to_san_list(newchar, ls):  # 向三维数组中插入数据
    newls = [[]]
    if len(ls) == 0:
        temp = [1]
        temp[0] = newchar
        newls[0] = temp
        return newls
    newls = []
    for er_ls in ls:
        temp = add_char_to_er_list(newchar, er_ls)
        for tls in temp:
            newls.append(tls)
    return newls


print_string = input("请输入待打印的字符串：")
print_char_list = string_to_list(print_string)  # 将待打印的字符串转成字符数组
print_string_list = []  # 存放所有的可能的字符数组排列组合
print_content = []  # 将字符数组转化成字符串数组
for i in range(0, len(print_char_list)):
    print_string_list = add_char_to_san_list(print_char_list[i],
                                             print_string_list)
for content in print_string_list:
    print_content.append("".join(content))
print_content.sort()
print("共{}种排列，打印如下：".format(len(print_content)))
for i in range(0, len(print_content)):
    print("{}:{}".format(i + 1, print_content[i]))
