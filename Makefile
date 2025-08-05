INSTALL = $(HOME)/PythonLib/lib

.PHONY : install uninstall

install :
	cp -vr src/ $(INSTALL)/thoth_src
	ln -s $(INSTALL)/thoth_src/thoth $(INSTALL)/thoth

uninstall :
	unlink $(INSTALL)/thoth
	rm -rfv $(INSTALL)/thoth_src

