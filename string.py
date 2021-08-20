string = "Beautiful place"

string_rev = string[::-1]
string_1 = string[-1:-7:-1]
string_2 = string[-1:-7:1]  #gives no output
string_3 = string[1:6:1]
string_4 = string[1:6:-1]      #gives not output

print(string, string_rev, string_1, string_3, sep='\n')
print(string[:5], string[::], string[3:7], sep=' ')

py_string = 'Python'
slice_object = slice(3)
print((py_string[slice_object]))

slice_object = slice(0, 5, 2)
print((py_string[slice_object]))


py_list = []
for i in py_string:
    py_list.append(i)

py_tuple = tuple(py_list)

slice_object = slice(-1, -4, -1)
print(py_list[slice_object], py_tuple[slice_object], sep='\n')

print(py_string[0:5:2])
print(py_string[0:4])
print(py_string[-1:-5:-2])


