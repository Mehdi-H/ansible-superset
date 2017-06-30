import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_package_depencies(Package):

    # Given a list of dependencies,
    dependencies = [
        "build-essential", "libssl-dev", "libffi-dev",
        "python-dev", "python-pip", "libsasl2-dev", "libldap2-dev"
    ]

    # Then, for each of our package dependencies,
    for dependency in dependencies:
        # This dependency is installed
        assert Package(dependency).is_installed
