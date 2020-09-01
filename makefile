install:
	cp prename /usr/local/bin/prename
	-mkdir -p /usr/local/share/man/man1
	cp prename.1 /usr/local/share/man/man1/
	gzip /usr/local/share/man/man1/prename.1 
uninstall:
	rm /usr/local/bin/prename
	rm /usr/local/share/man/man1/prename.1.gz
