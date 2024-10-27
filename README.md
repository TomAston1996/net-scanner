[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# NetScanner

The goal of NetScanner is to create an all-in-one CLI tool for exporing network vulnerabilities. The tool will utilise NMAP amongst other libraries to conduct a series of vulnerability tests to help improve Cybersecurity Engineer workflow.

![cli](./images/cli.png)

Functionality will include host discovery, port scanning, os detection, and a software vulnerability assessment. An automated report for the network will be produced as a result.

Features:
- Host and CPE discovery using NMAP
- Vulnerability assessment based on CPE's identified using NVD (National Vulnerability Database) API
- Automated report generation
- CLI Interface to improve Engineer workflow and abract complexity

## 🧑‍💻 Tech Stack

![Python]

## 🔧 Setup

### Dependencies
``` pip install -r requirements.txt``` will install all dependcies required

### API Key
Request an API Key from https://nvd.nist.gov/developers/request-an-api-key and place it in your ```.env``` file as 'NVD_API_KEY'

### Run Locally
``` python ./main.py``` will run the CLI tool locally

## 🧑‍🤝‍🧑 Developers 

| Name           | Email                      |
| -------------- | -------------------------- |
| Tom Aston      | mailto:mail@tomaston.dev     |

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TomAston1996/net-scanner.svg?style=for-the-badge
[contributors-url]: https://github.com/TomAston1996/net-scanner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TomAston1996/net-scanner.svg?style=for-the-badge
[forks-url]: https://github.com/TomAston1996/net-scanner/network/members
[stars-shield]: https://img.shields.io/github/stars/TomAston1996/net-scanner.svg?style=for-the-badge
[stars-url]: https://github.com/TomAston1996/net-scanner/stargazers
[issues-shield]: https://img.shields.io/github/issues/TomAston1996/net-scanner.svg?style=for-the-badge
[issues-url]: https://github.com/TomAston1996/net-scanner/issues
[license-shield]: https://img.shields.io/github/license/TomAston1996/net-scanner.svg?style=for-the-badge
[license-url]: https://github.com/TomAston1996/net-scanner/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tomaston96
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[TypeScript]: https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white
[Redux]: https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white
[Chart.js]: https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white
[Bootstrap]: https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[NodeJS]: https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
