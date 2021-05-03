# Algorithms (Flask-Restplus) Web API
​
This is a web api exposing methods for summing, finding closest number to zero from a list of numbers and grouping users by gender.
​
## Getting Started
​
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
​
​
### Prerequisites
​
What things you need to install the software and how to install them.
​
​
- python
- pip
- vs code
- docker desktop
​
​
### Installing
​
A step by step series of examples that tell you how to get a development env running.
​
### python
​
visit the [python](https://www.python.org/downloads/) website to download the python package for your operating system.

### pip

visit the [pip](https://pip.pypa.io/en/stable/installing/) website to learn how to install pip for your operating system.
​
### vs code

install [vs code](https://code.visualstudio.com/download) or any python IDE of your choice.

### docker desktop

install [docker desktop](https://www.docker.com/products/docker-desktop) by following instructions on the website.

## Running development
Make sure you are in the root folder of the project.
​
#### Install dependencies
```sh
pip install --upgrade pip setuptools==44.1.0
```
​
```sh
pip install --trusted-host pypi.python.org -r requirements.txt
```

## Usage


```sh
python manage.py run
```


## Running the tests
​
```sh
python manage.py test
```
​
### Detail testing methods
​
Explain what these tests test and why
​
```
TODO
```
​
## Docker

### DEV
```sh
docker build -t webapi .
```

```sh
docker run -p 5000:5000 webapi
```

## Environments
​
Provide a detailed list of current environments, how they can accessed and any other relevant information.
​
### DEV
​
## UAT
​
## PROD 
​
Add additional notes about how to deploy this on a live system
​
## Built With
​
Details of the tech stack that has been used.
​
- [Flask-RestPlus](https://flask-restplus.readthedocs.io/en/stable/) - The Web API framework used
​
​
## Architecture
​
A basic architecture diagram or description of the chosen architecture should be detailed here.
​
                                                                                                |
​
## Contributing
​
Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on the Eblocks standard for commit messages and the accepted pull request process.
​
## Versioning
​
We use [SemVer](http://semver.org/) for versioning. Versioning occurs automatically in the pipelines using [Semantic Release](https://github.com/semantic-release/semantic-release). For the versions available, see the tags on this repository.
​
## Changelog
​
A running changelog can be found here: [CHANGELOG.md](CHANGELOG.md)
​
## Authors
​
- **Jacob Khoza** <jacob.khoza@eblocks.co.za>
​
## Licenses
​
Place the result of `npx license-checker --summary` here
​
```
├─ MIT: 31
├─ ISC: 19
├─ Apache-2.0: 2
├─ BSD-3-Clause: 1
├─ BSD-2-Clause: 1
├─ CC-BY-3.0: 1
├─ CC0-1.0: 1
└─ (MIT AND CC-BY-3.0): 1
```
​
## Troubleshooting
​
List any common errors and their solutions
​
- Some common error
  > solution
​
## Meta
​
| Version | Author                       | Date       |
| ------- | ---------------------------- | ---------- |
| 0.0.1   | Jacob Khoza <jacob.khoza@eblocks.co.za> | 03/05/2021 |
