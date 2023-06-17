import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sane(host):
    assert host.package("sane").is_installed


def test_saned_socket_file(host):
    assert host.file("/etc/systemd/system/saned.socket").exists
