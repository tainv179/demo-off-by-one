from pwn import *

r = process("./demo")

payload = "\x00"*64
r.sendline(payload)
r.interactive()