# Entity

![pwn](https://img.shields.io/badge/category-pwn-brightgreen) <br>
![difficulty](https://img.shields.io/badge/difficulty-easy-green) <br>
![solvetime](https://img.shields.io/badge/solved-durring%20event-green)

## Description

> This Spooky Time of the year, what's better than watching a scary film on the TV? Well, a lot of things, like playing CTFs but you know what's definitely not better? Something coming out of your TV!

Provided files are:
- [entity](entity)
- [entity.c](entity.c)
- [flag.txt](flag.txt)

## Solving process

We are provided with a fake flag text file, a binary executable and C source code. First I checked to see what the binary does. It gives you questions and options that you have to execute in the correct order, to successfuly print the flag. I opened the source code to see what is going on.

We can discover that with the right combination we can read our values stored in  DataStore integer (R + L) and string (R + S). We can also see that in order to get the flag, we need to pass in C and our DataStorage integer has to be equal to 13371337. Now we have to find a correct string that will set our integer to our desired value.








Flag: