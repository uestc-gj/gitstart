fh = open('../work/Accounts.txt')
content = fh.readlines()
for line in content:
    if not line.find('@') == -1:
        print content[content.index(line)+1]

        
