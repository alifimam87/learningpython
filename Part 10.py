#bitwise (masing - masing bit)

a = 9
b = 5

# operator bitwise OR |

c = a | b
print ('=======OR=======')
print ('Nilai : ', a, 'binary',format(a,'08b'))
print ('Nilai : ', b, 'binary',format(b,'08b'))
print ('=============== |')
print ('Nilai : ', c, 'binary',format(c,'08b'))


# operator bitwise OR &

c = a & b
print ('=======&=======')
print ('Nilai : ', a, 'binary',format(a,'08b'))
print ('Nilai : ', b, 'binary',format(b,'08b'))
print ('=============== &')
print ('Nilai : ', c, 'binary',format(c,'08b'))


# operator bitwise XOR ^

c = a ^ b
print ('=======^=======')
print ('Nilai : ', a, 'binary',format(a,'08b'))
print ('Nilai : ', b, 'binary',format(b,'08b'))
print ('=============== ~')
print ('Nilai : ', c, 'binary',format(c,'08b'))


# operator bitwise NOT ~

c = ~ a
print ('=======~=======')
print ('Nilai : ', a, 'binary',format(a,'08b'))
print ('Nilai : ', b, 'binary',format(b,'08b'))
print ('=============== ~')
print ('Nilai : ', c, 'binary',format(c,'08b'))
