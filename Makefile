# SPDX-FileCopyrightText: 2024 antlers <antlers@illucid.net>
# SPDX-License-Identifier: GPL-3.0-or-later

.ONESHELL:

SOURCES = $(wildcard src/*)

README.md: SHELL = guix
README.md: .SHELLFLAGS = shell --pure -m manifest.scm -- emacs -nw --batch --quick --eval
README.md: README.md.src $(SOURCES)
	(progn
	  (require (quote dash))
	  (find-file "./README.md.src")
	  (org-mode)
	  (org-babel-do-load-languages
	   (quote org-babel-load-languages)
	   (quote ((shell . t))))
	  (setq org-confirm-babel-evaluate nil)
	  (org-babel-execute-buffer))
