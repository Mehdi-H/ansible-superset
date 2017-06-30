![travis](https://travis-ci.org/Mehdi-H/ansible-superset.svg?branch=master)

# Ansible-superset

An Ansible role to install superset on an Ubuntu distribution.

It was developed in TDD with idempotency checks using the Molecule framework, and with Travis-CI.

## Dependencies for development

- Some dependencies are needed to run molecule, as stated on the ! [doc](molecule.readthedocs.io/en/stable-1.22/index.html#quick-start).
```
    $apt-get update
    $apt-get install gcc python-pip python-vagrant libssl-dev libffi-dev
```

- Create a Python environment dedicated for this project, with Conda env for instance.
```
    $conda create --name ansible_molecule python=2.7 ansible docker molecule
    $source activate ansible_molecule
```

- You can then run molecule and test that the build is passing correctly. `sudo` rights may be necessary.
```
    $cd superset
    $molecule test || OR || $sudo molecule test.
```

## Ansible role details

The role was built according to the superset installation guildelines [from the Apache repository](https://github.com/ApacheInfra/superset/blob/master/docs/installation.rst).

- Dependencies for Superset are installed
