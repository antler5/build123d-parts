(use-modules (guix profiles))

(specifications->manifest
  '("bash"
    "emacs"
    "emacs-dash"
    "emacs-ox-pandoc"
    "grep"
    "make"
    "pandoc"
    "which"))
