INSTALL = $(HOME)/PythonLib/lib

.PHONY : install uninstall

install :
	cp -vr src/ $(INSTALL)/thoth

uninstall :
	rm -rfv $(INSTALL)/thoth

