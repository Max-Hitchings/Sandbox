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

z = "3.2"
print(int(z))