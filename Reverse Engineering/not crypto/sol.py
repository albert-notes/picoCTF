import angr
from claripy import *

p=angr.Project("./not-crypto",auto_load_libs=False)

flag_chars=[BVS(f'x_{i}',8) for i in range(100)]
flag=Concat(*flag_chars+[BVV(b'\n')])

st=p.factory.entry_state(stdin=flag)
sm=p.factory.simgr(st)
sm.explore(find=lambda s: b'Yep, that\'s it!' in s.posix.dumps(1),avoid=lambda s: b'Nope, come back later' in s.posix.dumps(1))

for s in sm.found:
    print(s.posix.dumps(0))
