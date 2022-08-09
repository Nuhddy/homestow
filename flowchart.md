# homestow

## Outline

Available functions:
- install
- uninstall
- reinstall
- convert from files to links (stow mode)
- convert from links to files (non-stow mode)

Configuration:
- YAML config file
- profiles (hostname, host, kernel, etc.)
- add stow packages to current profile when added

## Usage

```
homestow ACTION ARGS PACKAGES
_________________________________________________________________________________

homestow install ARGS PACKAGES

ARGS:
-p, --profile:      profile to source package list from
-c, --config:       path to configuration file

PACKAGES:           packages to install (space-separated)
_________________________________________________________________________________

homestow uninstall PACKAGES

PACKAGES:           packages to uninstall (space-separated)
_________________________________________________________________________________

homestow reinstall ARGS PACKAGES

ARGS:
-p, --profile:      profile to source package list from
-c, --config:       path to configuration file

PACKAGES:           packages to reinstall (space-separated)
_________________________________________________________________________________

homestow add TARGET-PATH PACKAGE-NAME ARGS

TARGET-PATH:        path of directory to add

PACKAGE-NAME:       name of package

ARGS:
-p, --profile:      profile(s) to add package to
-c, --config:       path to configuration file
_________________________________________________________________________________

homestow forget PACKAGE-NAME

PACKAGE-NAME:       name of package(s) to forget (reinstall as non-link files)
```
