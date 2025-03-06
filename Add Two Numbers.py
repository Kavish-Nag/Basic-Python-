l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
l3=l1[::-1]
l4=l2[::-1]
l5=[]
carry = 0
for i in range(max(len(l3), len(l4))):
    val1 = l3[i] if i < len(l3) else 0
    val2 = l4[i] if i < len(l4) else 0
    sum_val = val1 + val2 + carry
    carry = sum_val // 10
    l5.append(sum_val % 10)
if carry:
    l5.append(carry)
print(l5)
