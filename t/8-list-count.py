slist = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
sdic = {}
for s in slist:
    if s not in sdic:
        sdic[s] = 1
    else:
        sdic[s] += 1
for s in sdic:
    print "%s count is %s " % (s,sdic[s])
        

