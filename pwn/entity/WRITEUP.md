# Entity

We are provided with a fake flag text file, a binary executable and C source code. First I checked to see what the binary does. It gives you questions and options that you have to execute in the correct order, to successfuly print the flag. I opened the source code to see what is going on.

We can discover that with the right combination we can read our values stored in  DataStore integer (R + L) and string (R + S). We can also see that in order to get the flag, we need to pass in C and our DataStorage integer has to be equal to 13371337. Now we have to find a correct string that will set our integer to our desired value.








Flag: