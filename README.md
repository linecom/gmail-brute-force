![](https://github.com/oliviagallucci/gmail-brute-force/blob/master/gmail-brute-force.gif)
![Python](https://img.shields.io/badge/pythonv-3.8-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-green.svg?style=for-the-badge)](http://perso.crans.org/besson/LICENSE.html)
![Github-sponsors](https://img.shields.io/badge/sponsor-pink?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)

# gmail-brute-force

A Python script to brute-force GMail accounts with a target email address, a password list, and a wait duration between login attempts. The waiting period is necessary because you will be flagged by GMail otherwise. 

## Getting Started

### Prerequisites

#### Install the command-line parser 

```
pip install argparse
```

#### Obtain password lists 

If you do not have any password lists, I recommend [Daniel Miessler](https://github.com/danielmiessler)'s [SecList passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords). 

## Installation 

```script 
git clone https://github.com/oliviagallucci/gmail-brute-force
```

### Usage
```
# navigate to the program on the machine 
cd /filepath/gmail-brute-force/
```

```
# python3  gmail-brute-force.py  target_email  password_list_file  wait_seconds 
python3 gmail-brute-force.py target@gmail.com password_list.txt 3
```

## Contributing

### How to submit a pull request 

1. Clone the project 
2. Make your modifications 
  * Use in-line comments to explain your modifications. 
  * If your modifications are larger, please use multiple commits in your pull request. 
3. Submit a pull request. Explain your changes, why you made them, etc.

## Releases 

Alpha 1.0

## Authors

* [Olivia Gallucci](https://github.com/oliviagallucci) - code author 
* See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the General Public License version 3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [@PurpleBooth](https://github.com/PurpleBooth) for READMD.md inspiration
