;; SPDX-FileCopyrightText: 2024 antlers <antlers@illucid.net>
;; SPDX-License-Identifier: CC0-1.0

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
