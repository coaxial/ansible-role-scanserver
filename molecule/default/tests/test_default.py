import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sane(host):
    assert host.package("sane").is_installed


def test_saned_socket_config(host):
    file = host.file("/etc/systemd/system/saned.socket")

    assert file.exists
    assert file.owner == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755


def test_saned_service_config(host):
    file = host.file("/etc/systemd/system/@saned.service")

    assert file.exists
    assert file.owner == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755


def test_saned_service(host):
    service = host.service("saned.socket")

    assert service.is_enabled
    assert service.is_running


def test_saned_config
    file = host.file("/etc/sane.d/saned.conf")

    assert file.exists
    assert file.owner == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755
    assert '192.168.0.0/24' in file.contents
