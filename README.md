<div align="center">

  # gmail-brute-force
  
  ![](https://github.com/oliviagallucci/gmail-brute-force/blob/master/misc/gmail-brute-force.gif)
  
  A Python script to brute-force GMail accounts with a target email address, a password list, and a wait duration between login attempts. The waiting period is necessary because you will be flagged by GMail otherwise. 
  
  <a href="https://www.python.org/">![Python](https://img.shields.io/badge/pythonv-3.8-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)</a>
  <a href="https://mail.google.com/">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>
  <a href="https://github.com/oliviagallucci/gmail-brute-force/blob/master/LICENSE.md">![GPLv3 license](https://img.shields.io/badge/License-GPLv3-green.svg?style=for-the-badge)</a>
  <a href="https://github.com/sponsors/oliviagallucci">![Github-sponsors](https://img.shields.io/badge/sponsor-pink?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)</a>

</div>



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
* See also the list of [contributors](https://github.com/oliviagallucci/gmail-brute-force/contributors) who participated in this project.

## License

This project is licensed under the General Public License version 3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Warranty  
The author of this tool offers no warranty or guarantee for its performance, reliability, or suitability for any particular purpose.

The tool is provided "as is" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability, fitness for a particular purpose, or non-infringement.

Use of this tool is entirely at the user's own risk. The author does not accept any liability for any loss, damage or expense incurred by the user or any third party resulting from the use of this tool, whether direct or indirect.

Furthermore, the author expressly disclaims any responsibility or liability for the accuracy, content, or availability of information found through the use of this tool, or for any harm caused by viruses, malware, or other harmful components that may be introduced into your system as a result of using this tool.

By using this tool, the user acknowledges that they have read this warranty statement and agree to assume all risks associated with its use.

## Acknowledgments

* [@PurpleBooth](https://github.com/PurpleBooth) for READMD.md inspiration
