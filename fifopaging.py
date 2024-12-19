nofault = 0
page = []
listp = [1,2,3,4,5,3,4,4,78,9,0,11]
for el in listp:
    if el not in page and len(page)<3:
        page.append(el)
    elif el not in page and len(page)>=3:
        page.pop(0)
        page.append(el)
    elif el in page:
        nofault+=1
    print(page)
# print(page)
fault = len(listp)-nofault
print("Pages: ", end = '')
print(listp)
print("Number of faults :" + str(fault))
print(f'Fault Ratio: {fault} / {len(listp)}')
