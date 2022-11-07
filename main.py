# # class Node:
# #     def __init__(self, data = None):
# #         self.data = data
# #         self.nextNode = None
# #
# # class LinkedList:
# #     def __init__(self):
# import random, requests, json
# import time
# words = []
# for x in range(random.randint(5, 9)):
#     wordRequest = requests.get("https://random-word-api.herokuapp.com/word")
#     words.append(wordRequest.json()[0])
#     time.sleep(.1)
# input = ' '.join(words)
# print(input)


def testing(x, y):
    bad(x)
    return x * y

def bad(x):
    pass
x = 2
y = 5
test = testing(x, y)
bad(x)
print(test)