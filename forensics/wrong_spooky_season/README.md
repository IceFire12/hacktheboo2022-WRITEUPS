# Wrong Spooky Season - WRITEUP

We get a .pcap file. After looking through we find some images and some commands. We can run "strings" on the .pcap file and at the end we get a very familiar looking text. We find a Base64 encoded text but in reverse order. We just use a online text reversing tool and decode the text with Cyberchef to get the flag.

Flag: HTB{j4v4_5pr1ng_just_b3c4m3_j4v4_sp00ky!!}
