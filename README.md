# Webbf
## Description

Webbf is tool designed as a [Patator](https://github.com/lanjelot/patator) wrapper to find weak and default accounts on web administration interfaces.
Webbf takes as input a JSON file (output generated by [Paparazzi](https://github.com/bik3te/Paparazzi)). Every URL specified on this file must be as the following format : protocol://ip_or_hostname:port

## Modules

Each module corresponds to a type of web administration interface. Currently, 6 web interfaces are handled by the Webbf :

* Tomcat
* Jenkins
* Splunk
* Jira
* Grafana
* BMC Discovery

These modules are classes with the following format :

```python
class {web_solution_name}Module():
	def __init__(self, lst, nb_threads):
		...
	def tryDefaultCredsPatator(self, url):
		...
```

These classes are dynamically instanciated with the following parameters :

* lst : corresponds to a list of urls associated hosting the targeted service
* nb_threads : number of threads

## Wordlists

Each module hash its own wordlist on the config subdirectory. Each wordlist must be in the following format :
login:password\n
login2:password2\n
Etc.

## Acknowledgments

This repository contains the great lanjelot's [Patator](https://github.com/lanjelot/patator) as submodule.
Lény BUENO (@bik3te) for his tool Paparazzi :)

## Requirements

* Python 3
* [colorama](https://pypi.org/project/colorama/): `pip install -U colorama`

## Usage Examples

```
* BMC Discovery : dictionnary attack agains a BMC discovery interface

$ python3 webbf.py interfaces.json 
 [!] Loading JSON content from 'interfaces.json'
 [!] Loading BmcdiscoveryModule
 [!] Trying default credentials on http://discovery.trybmc.com:80
 [*] [http://discovery.trybmc.com:80] : (demouser:demouser)
 ...
```