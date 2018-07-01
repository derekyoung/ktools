import sys

if len(sys.argv) == 2:
    infile = str(sys.argv[1])
else:
    print("huh?")
    quit()

with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [x.rstrip('\n') for x in lines]
    for line in lines:
        foo = str(line).split(' - ')
        if ', ' in foo[1] and 'Hawaiian' not in foo[1] :
            name = foo[1].split(', ')
            if len(str(name).split()) == 2: #its a name
                print(foo[0] + ' - ' + name[1] + ' ' + name[0])
            else:
                print(line)
        else:
            print(line)

