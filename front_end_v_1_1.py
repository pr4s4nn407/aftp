import pyfiglet
import time

def usage():
    print("# send -> sending a file")
    print("# receive -> receiving a file")
    print("# exit - > goodbye")
    print("# -k -> a key value, used to identify which process needs to receive the file")
    print("# -p -> number of parts to be made out of the file")
    print("# 'hash' symbol followed by a value may be used to indicate size of a part")
    print("# -A -> append all parts of a file if available offline, not to be used with any other argument")
    print("# -b -> size of each part in bits")
    print("# -B -> size of each part in bytes")
    print("# -K -> size of each part in kilobytes")
    print("# -G -> size of each part in gigabytes")
    print("# [Note]: Address of file should be given for sender, address of directory for receiver")

title = pyfiglet.figlet_format("PRAS INDUSTRIES", font = "computer" ) 
print(title) 
i=3
instructions=["send", "receive", "exit", "-k", "-p", "-A", "-b", "-B", "-K", "-G"]
while(True):
    #here goes the interface...
    instruction = input("aftp > ")
    words = instruction.split(" ")

    # parsing keywords....
    # send -> sending a file
    # receive -> receiving a file
    # exit - > goodbye
    # -k ->a key value, used to identify which process needs to receive the file
    # "/address/" -> address of file in fiile system of sender
    # -p -> number of parts to be made out of the file
    # -A -> receive all parts of a file and append it
    # -b -> size of each part in bits
    # -B -> size of each part in bytes
    # -K -> size of each part in kilobytes
    # -G -> size of each part in gigabytes

    # initializing values we get from command
    addr=""
    part=0
    size=0
    check=0

    # exit
    if(len(words)>6):
        usage()
    if(words[0] == "exit"):
        print("Bye!")
        time.sleep(1)
        break
    # send
    elif(words[0]=="send"):
        addr=words[1]
        sizee=-1
        parts=0
        if(instructions[4] in instruction): # -p
            parts = 300
            parts = instruction[instruction.index(instruction[4])]
            print("number of parts is ", parts)
            print("--> ", instruction[instruction.index(instruction[4])])
            print(instruction)
        # print("This is the demo version, only the CLI is available for usage. Other functions will be added in later versions.")
    # receive
    elif(words[0] == "receive"):
        print("This is the demo version, only the CLI is available for usage. Other functions will be added in later versions.")
    else:
        usage()
    
    