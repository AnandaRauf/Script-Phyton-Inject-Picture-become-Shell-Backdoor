from sys import argv
script, shell, img = argv
i = open(shell,'rb').read()
i += open(img,'rb').read()
f = open('unks.jpg','wb').write(i)
