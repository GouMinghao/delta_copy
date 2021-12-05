from deltacopy.delta_cmp import DeltaComparer
d = DeltaComparer("dir1", "dir2")
d.compare()
print(d.missing_record_list)