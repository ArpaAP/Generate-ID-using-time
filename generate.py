import time

# ID generation function
def genid():
    twos = str(time.time()).split('.')
    return '{0}{1:0<7}'.format(*twos)

# Use
for x in range(10):
    print(genid())
