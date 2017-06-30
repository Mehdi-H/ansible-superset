import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_package_dependencies(Package):

    # Given a list of dependencies,
    dependencies = [
        "build-essential", "libssl-dev", "libffi-dev",
        "python-dev", "python-pip", "libsasl2-dev", "libldap2-dev"
    ]

    # Then, for each of our package dependencies,
    for dependency in dependencies:
        # This dependency is installed
        assert Package(dependency).is_installed


def test_pip_package_dependencies(PipPackage):

    # Given a list of pip package dependencies
    dependencies = ["virtualenv", "setuptools"]
    # and the list of pip packages
    pip_packages_list = PipPackage.get_packages().keys()

    # Then, for each of theses dependencies,
    for dependency in dependencies:
        # They should be installed
        assert dependency in pip_packages_list
