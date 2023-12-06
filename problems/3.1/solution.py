# class Number:
#     def __init__(self, value=None, indexes=[]):
#         self.value = value
#         self.indexes = indexes
#         self.flag = False

#     def set_value(self, value):
#         self.value = value

#     def get_value(self):
#         return self.value
    
#     def set_state(self, value):
#         self.flag = value

#     def get_state(self):
#         return self.flag
    
#     def set_indexes(self, indexes):
#         self.indexes = indexes

#     def get_indexes(self):
#         return self.indexes
    
#     def __str__(self):
#         return f"Value: {self.value}, Indexes: {self.indexes}, Flag: {self.flag}"
    
# rows = []
# symbols = []

# with open('input.txt','r') as file:
#     lines = file.readlines()
    
# for row, line in enumerate(lines):
#     cur_num = ''
#     rows.append({})
#     for i, c in enumerate(line):
#         if c.isdigit():
#             cur_num += c
#         elif cur_num:
#             indexes = range(i-len(cur_num),i)
#             number = Number(int(cur_num), indexes)
#             for j in indexes:
#                 rows[row][j] = number
#             cur_num = ''
#         if not c.isdigit() and c != '.':
#             symbols.append((row, i))
            
# for row in rows:
#     for num in row:
#         print(row[num])
# print('----------------------------------------------------')
# sum = 0
# for s_row, s_col in symbols:
#     cur_rows = [s_row-1, s_row, s_row+1]
#     for cur_row in cur_rows:
#         if cur_row < 0 or cur_row > len(rows)-1: continue
#         cur_cols = [s_col-1, s_col, s_col+1]
#         for cur_col in cur_cols:
#             if cur_col < 0 or cur_col > len(lines[0])-1: continue
#             number = rows[cur_row].get(cur_col, None)
#             if number is not None and not number.get_state():
#                 sum += number.get_value()
#                 number.set_state(True)
# for row in rows:
#     for num in row:
#         print(row[num])
# print(sum)

# approach:
# pass through once and populate row indexed array of dictionaries
# [row 0 {2: 467, 7: 114}]


# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

import math as m, re

board = list(open('input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))