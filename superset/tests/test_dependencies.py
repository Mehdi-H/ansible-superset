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

    # Then, for each of these dependencies,
    for dependency in dependencies:
        # They should be installed
        assert dependency in pip_packages_list


def test_pip_package_dependencies_are_up_to_date(PipPackage):

    # Example of output from the get_outdated_packages() function
    # {
    #   u'virtualenv': {u'current': u'15.1.0', u'latest': u'15.1.0'},
    #   u'wheel': {u'current': u'0.29.0', u'latest': u'0.29.0'},
    #   ...
    # }

    # Given a list of pip package dependencies
    dependencies = ["setuptools", "pip"]
    # and the list of pip packages
    # with their current & latest versions
    outdated_pip_packages = PipPackage.get_outdated_packages()

    # If the list is empty, there is no outdated packages
    if not outdated_pip_packages:
        return True

    # Else
    # Then, for each of these dependencies,
    for dependency in dependencies:
        # The current dependency version should be equal to the latest
        pip_dependency_v = outdated_pip_packages.get(dependency)
        assert pip_dependency_v["current"] == pip_dependency_v["latest"]
