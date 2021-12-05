from deltacopy.delta_cp import DeltaCopier
print('=== Delta Copier ===')
log_name = input("Input the compare log: ")
dc = DeltaCopier(log_name)
dc.print_and_exec_delta_copy()