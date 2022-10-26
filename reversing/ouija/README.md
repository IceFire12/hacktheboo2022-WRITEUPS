# Ouija

![reversing](https://img.shields.io/badge/category-reversing-brightgreen) <br>
![difficulty](https://img.shields.io/badge/difficulty-easy-green) <br>
![solvetime](https://img.shields.io/badge/solved-durring%20event-green)

## Description

> You've made contact with a spirit from beyond the grave! Unfortunately, they speak in an ancient tongue of flags, so you can't understand a word. You've enlisted a medium who can translate it, but they like to take their time...

Provided file is:
- [ouija](ouija)

## Solving process

Throw the file into [DogBolt](https://dogbolt.org). Immediately notice the flag in the `main` function that is encrypted with a Ceasar cipher.

```
setvbuf(stdout,(char *)0x0,2,0);
local_20 = strdup("ZLT{Svvafy_kdwwhk_lg_qgmj_ugvw_escwk_al_wskq_lg_ghlaearw_dslwj!}");
puts("Retrieving key.");
sleep(10);
```

Throwing the string into a [ceasar decryptor](https://www.dcode.fr/caesar-cipher), we get the flag.

**Flag:** *HTB{Adding_sleeps_to_your_code_makes_it_easy_to_optimize_later!}*
