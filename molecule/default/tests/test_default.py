import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_collections_dir(host):
    collections_dir = host.file('/var/lib/radicale/collections')

    assert collections_dir.user == 'radicale'
    assert collections_dir.group == 'radicale'
    assert collections_dir.mode == 0o700


def test_systemd_service_file(host):
    svc_file = host.file('/etc/systemd/system/radicale.service')

    assert svc_file.user == 'root'
    assert svc_file.group == 'root'
    assert svc_file.mode == 0o755


def test_users_file(host):
    users_file = host.file('/etc/radicale/users')

    assert users_file.user == 'root'
    assert users_file.group == 'root'
    assert users_file.mode == 0o640


def test_config_file(host):
    users_file = host.file('/etc/radicale/config')

    assert users_file.user == 'root'
    assert users_file.group == 'root'
    assert users_file.mode == 0o640


def test_web_ui(host):
    html = host.run('curl -L http://localhost:5232').stdout

    assert '<title>Radicale Web Interface</title>' in html


def test_reverse_proxy(host):
    html = host.run('curl -L http://localhost/radicale').stdout

    assert '<title>Radicale Web Interface</title>' in html
