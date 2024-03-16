def sel_reverse(arr,l):
    results = []
    if(l==0):
      return arr
    count = 0
    while count<=len(arr):
      slice_object = slice(0+count,l+count)
      sec = arr[slice_object]
      rev = sec[::-1]
      count += l
      results.append(rev)
      slice_object = ''
    x = [b for sl in results for b in sl]
    return x


print(sel_reverse([2,4,6,8,10,12,14,16], 3))
print(sel_reverse([1,2,3,4,5,6], 2))
print(sel_reverse([1,2,3,4,5,6], 0))