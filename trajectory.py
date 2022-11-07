# import math
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def do_shit(a):
#     ANGLE = a
#     other_angle = 180 - (90 + ANGLE)
#
#     # hs = hs = 0
#     # hu = vu = 0
#     # hv = vv = 0
#     # ha = va = 0
#     # ht = vt = 0
#     va = 9.81
#
#     vu = 30 * math.cos(math.radians(other_angle))
#     hu = hv = 30 * math.sin(math.radians(other_angle))
#     vs = (vu * vu) / (2 * va)
#     vt = ht = vs / (0.5 * vu)
#
#     hs = 2 * hu * ht
#
#     print
#     return hs, vs
#
#
# hsl, vsl = [], []
#
# for x in range(90):
#     hs, vs = do_shit(x)
#     hsl.append(hs)
#     vsl.append(vs)

# plt.scatter(vsl, hsl)
# plt.xticks(np.arange(min(vsl), max(vsl) + 1, 5))
# plt.show()

# x = [0.187, 0.140
#     , 0.968
#     , 0.897
#     , 0.743
#     , 0.753
#     , 0.628
#     , 0.534
#     , 0, 473
#     , 0.421
#     , 0.324
#     , 0.294
#     , 0.260
#     , 0.217
#     , 0.201
#     , 0.187
#     , 0.17
#     , 0.152]
#
# y = [6.57
#     , 6.35
#     , 6.18
#     , 6.461
#     , 3.90
#     , 3.05
#     , 2.90
#     , 1.35
#     , 1.10
#     , 0.70
#     , 0.62
#     , 0.60
#     , 0.42
#     , 8.
#     , 1.39
#     , 33
#     , 0.36
#     , 0.3
#     , 0.33]
# plt.scatter(x, y)
# print(len(x))
# print(len(y))
# plt.show()

