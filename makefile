clean:
	find . -type f -name "*.rpyb" -exec rm {} \;
	find . -type f -name "*.pyo" -not -path "./vintra-fabelo/lib/*" -exec rm {} \;
	find . -type f -name "*.rpyc" -exec rm {} \;
	find . -type f -name "log.txt" -exec rm {} \;
	rm -f vintra-fabelo.zip

pack: clean
	zip vintra-fabelo.zip vintra-fabelo -r -q
