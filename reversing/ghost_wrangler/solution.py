def main():
    plaintext = "[GQh{'f}g wLqjLg{ Lt{#`g&L#uLpgu&Lc'&g2n"
    flg = []
    for i in range(len(plaintext)):
       flg.append(ord(plaintext[i]) ^ 0x13) 
    print(''.join(chr(i) for i in flg))

main()