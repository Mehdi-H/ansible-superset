[![travis](https://travis-ci.org/Mehdi-H/ansible-superset.svg?branch=master)
](https://travis-ci.org/Mehdi-H/ansible-superset)
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

- System dependencies for Superset are installed
- Pip package dependencies for Superset are installed
    - Some of them are updated through pip.
- Superset and its database are initialized through the fabmanager.
- The superset server can be launched.

## TODO

- Test idempotency of the fabmanager custom module.
- Create a superset module.
- Check idempotency for this superset module.
- Check health of the superset server after it has been launched.

### Missing tests with test-infra

- Check that the superset database exists after using the fabmanager.
- Check that it contains a superset user as defined.
- Check its rights.
- Check the table it contains according the superset load-examples command.
- Check health of the superset server after it has been launched.
