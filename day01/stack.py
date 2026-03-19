stack = []
stack.append('A')   #push A ->['A']
stack.append('B')   #push B ->['A','B']
stack.append('C')   #push C ->['A','B','C']
print(stack.pop())  # -> 'C'
print(stack.pop())  # -> 'B'
