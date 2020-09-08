# create table (4 cols and 2 rows) with floating numbers using format method
# 15 symbols for number and 4 symbols for float part

table = '''
    {1:15.4f} {0:15.4f} {5:15.4f} {4:15.4f}
    {7:15.4f} {2:15.4f} {3:15.4f} {6:15.4f}
'''.format(
    1.54453, 1154.34235434, 42354.535, 22.4343543, 9877.345, 540087.09453, 55.93, 90.09
)
print(table)
