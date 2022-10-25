

Searching around for DNS data extraction tools. We can use included tshark tool in kali linux. We get all DNS responses exported. We use regex to get only the hex data, that we can throw in cyberchef. Save the output as a .zip file. Extract it and we find a lot of .xml files. We start searching until we find a flag in one of the files.



Flag: HTB{M4g1c_c4nn0t_pr3v3nt_d4t4_br34ch}

https://www.netresec.com/?page=Blog&month=2012-06&post=Extracting-DNS-queries

https://regex101.com/