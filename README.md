# DevEnvCLI

## Introduction
`DevEnvCLI` is a command-line tool designed to streamline the setup of development environments. It automates the installation of programming languages, configures global Git settings, and creates new projects with basic structures. This tool aims to save time and reduce the complexity of configuring development environments, making it easier for developers to start new projects.

## Features
- Install multiple programming languages with a single command.
- Configure Git with global username and email.
- Create new projects with essential files and directories.
- Support for multiple operating systems.

## Installation
To install `DevEnvCLI`, clone this repository and run the installation script:


` git clone https://github.com/brettadams0/DevEnvCLI.git `
` cd DevEnvCLI `
`python setup.py install `

## Usage
Here are some common commands you can use with DevEnvCLI:

## Install a Programming Language
DevEnvCLI install --language python

## Configure Git
DevEnvCLI configure --username "Your Name" --email "your.email@example.com"

Create a New Project
DevEnvCLI create --language python --project "my_new_project"
