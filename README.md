# vulnscanner

1. this program will same return the vuln from the open ports and also after that we want to add a function which will check those vuln with text file which contains vuln software banners.

2. I have created a file 'vuln.txt'. Its all gibberish except the third line, it is the banner from the SSH port from metasploitable, which we received earlier.

<img width="479" alt="image" src="https://github.com/juikalan21/vulnscanner/assets/159107774/1b63e306-eed6-44c7-a2d3-05979e728c93">

3. lets create the program now,
we will use three libraries in this program, 
1. socket: which allows us to perform the connection an receive data from the target.
2. os : in order to check whether the specified flies of vulnerable banners exist or not, an whether we can actually execute it and read from it. the os library comes with some functions that allows us to check whether file exists or not.
3. sys: in order to checkout the number of arguments specified in the command of the program.

4. first define the main function, 
we want to checkout is to use the sys library to check whether we have the correct number of argument specified in the command itself. if we count the arguments, the first one is the name of file, and second one is name of the file that we will use for the vuln banners.

5. so in our case, after the user specify the correct command, we want to continue executing the program, so i will create a list of ports and we scan multiple hosts, i.e. the entire local network. then we will just make a loop that will look through all the local machines in our local network. right now we will just scan 2 or 3 macines.

<img width="458" alt="image" src="https://github.com/juikalan21/vulnscanner/assets/159107774/bd79432e-38c5-4ca4-8eea-7b0c324dd3d3">

6. i have specified range (1,130) since my ip address of the  windows machine end in 1 and metasploitable in 129. If you want to scan th entire local network just type 1 to 255, since that is the maximum number of hosts available on a local network.

7. now we will code the return banner function like we did earlier.

<img width="305" alt="image" src="https://github.com/juikalan21/vulnscanner/assets/159107774/ee162496-2bd2-40db-b0f2-0c4af3874659">

8. and lastly, the checkVuln function, here will specify the mode, we only want to read. we want to read line by line. we will use the decode utf-8 which will simply decode bytes like object banner to a string using UTF-8 enoding.

<img width="508" alt="image" src="https://github.com/juikalan21/vulnscanner/assets/159107774/3357e0d0-d662-4efa-887d-0fb14bfb2e49">


