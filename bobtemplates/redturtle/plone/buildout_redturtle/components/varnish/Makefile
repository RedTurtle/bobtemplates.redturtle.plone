.PHONY: lucky

PATH := .:$(PATH)

.PHONY: bootstrap
bootstrap:
	ln -s profiles/$(sitename)_staging.cfg buildout.cfg
	./.bootstrap.sh
	./bin/buildout -N
    
.PHONY: u

install_crontab:
	./bin/fab install_crontab

install_logrotate:
	./bin/fab install_logrotate

# ./bin/munin-install is generated by buildout at the moment
install_munin:
	./bin/munin-install.py

install_files: install_crontab install_logrotate install_munin

buildout:
	buildout -Nt 2

