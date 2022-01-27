''' The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values: '''


# def rgb(r, g, b):
#     lst = [r, g, b]
#     alphabet = {
#                 '01': '1',
#                 '02': '2',
#                 '03': '3',
#                 '04': '4',
#                 '05': '5',
#                 '06': '6',
#                 '07': '7',
#                 '08': '8',
#                 '09': '9',
#                 '10': 'A',
#                 '11': 'B',
#                 '12': 'C',
#                 '13': 'D',
#                 '14': 'E',
#                 '15': 'F',
#                 }
#     rgb_res = []
#     for i in lst:
#         while i > 0:
#             if i <= 0:
#                 rgb_res.append('00')
#             elif i > 255:
#                 i = 255
#             rgb_res = str(i % 16)
#             i = i // 2

    
#     return rgb_res


# print(rgb(-20,275,125))
# print(rgb(0, 0, 0))
# print(rgb(1, 2, 3))
# print(rgb(255, 255, 255))
# print(rgb(254, 253, 252))
# print(rgb(164, -12, 59))
# print(rgb(149, -61, 287))
# print(rgb(-54, 355, -38))
# print(rgb(144, 140, 2))