Operating System Guidance
===

**Disclaimer**

1. This repositories supposed to make your task easier. but you need to *understand* all the workflow by yourself
2. There is a possibility that my code is not updated yet. so, make sure to see your module.

**First Thing First**

Make sure to Download all the files related to 

Chapter 5
--

**Run every single file & make it executable**

    gcc –pthread main1.c –o main1
    chmod +x main1

**How to automate the run command and save it as a newfile (Bash)**

    for in range{1..10};do ./main1 > ./outputA/"output$i.txt"; done
    
```.``` means current directory and make sure to create outputA directory.
make sure to change the *main1* and the *outputA* to another files and directory for next task

**How to automate the checker (Bash)**

    for i in range{1..10};do for j in {1..10};do python3 samaChecker.py "outputA/output$i.txt" "outputA/output$j.txt"; done;done
    
make sure to locate a correct path for *outputA/output$i.txt*
make sure to change the directory path and the checker if you need it.

**Credit**
As far as I know, these code(Chapter 4&5) are made by github users that teach about Thread and Lock. I forgot his account. but I will make sure to link his account as soon as I know it
