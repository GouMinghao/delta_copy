from deltacopy.delta_cmp import DeltaComparer
print('=== Delta Comparer ===')
src = input("Input the src directory path: ")
dst = input("Input the dst directory path: ")
dc = DeltaComparer(src, dst)
dc.compare()
print(dc.missing_record_list)