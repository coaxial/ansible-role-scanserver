Based upon instructions from https://pimylifeup.com/raspberry-pi-scanner-server/

# Role variables

Name | Default | Possible values | Description
---|---|---|---
`access_list` | `192.168.0.0/24` | An array of CIDR notation strings | Hosts that are allowed to access `saned`

# Example Playbook

```yaml
- hosts: all
  become: true
  tasks:
    - name: Setup saned
      include_role:
        name: coaxial.scanserver
```

# Firewall

If the firewall is a Linux machine, use the
Netfilter nf_conntrack_sane connection
tracking module instead.

