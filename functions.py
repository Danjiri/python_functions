#1次元配列を2次元配列に変換     #convert_1d_to_2d(配列,行数)

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]
