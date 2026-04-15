str2 = "Rocky"
print(str2[0:3])
print(str2[0:4])
print(str2[0:5])
print(str2[:2])
print(str2[1:])

word = "Amazing"
print(word[0:7:2])
print(word[0:7:3])

a = "Amazing"   
print(a[-1:-7:-1])  #It's run but shows an empty string

# But Python tries to go forward (left → right)
# And -1 is already to the right of -6
