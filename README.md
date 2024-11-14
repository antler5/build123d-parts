<!-- SPDX-FileCopyrightText: 2024 antlers <antlers@illucid.net> -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- This file is generated from $< -->
<!-- Do not edit it directly -->
<h1>antler5' build123d parts</h1>

## Cloning and Authenticating

``` bash
git clone 'https://github.com/antler5/build123d-parts' && cd build123d-parts
```

You may verify that each commit in this branch has been signed by an
authorized contributer via GNU Guix's
[authentication](https://guix.gnu.org/manual/en/html_node/Invoking-guix-git-authenticate.html)
mechanism.

``` bash
git fetch origin keyring:keyring
guix git authenticate \
  'dc26658e5d1f248b3f3e56d48456adb6d7e40b20' \
  'DACB 035F B9B0 EE9C 7E13  1AAA C310 15D9 6620 A955'
```

## Included parts

<table>
<thead>
<tr class="header">
<th>File-name</th>
<th>Description</th>
<th>License</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>src/singer-handle.py</td>
<td>A handle for my partner's Singer sewing machine. The original wooden
handle wore through. Not sure how long the filament will last, tbh.</td>
<td>GPL-3.0-only</td>
</tr>
</tbody>
</table>

## License

Unless otherwise specified:

- Code sources and snippets are
  [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0.html).  
- The documentation and other texts are
  [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/).  
- Trivial files may be explicitly released as
  [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/legalcode).
