USAGE
-----
ansible-playbook -u rmullen -k -i inventory -e "strong_auth_install=yes risk_auth_install=yes sample_app=yes" site.yml

create an inventory create a playbook to run this and or additional roles

Role Name
this role installs advanced auth 9.0.2

Requirements
------------
java is expected to be installed at /opt/java
tomcat is expected to be installed at /opt/tomcat

Role Variables
--------------
check group_vars/all.yml

Group vars can be overwritten using ansible precedence. Please do not write over group_vars values unless they are intended to be permanent
http://docs.ansible.com/ansible/latest/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable

Example Playbook
site.yml

hosts: rsk-app
become: true
roles:
  - ca-adv-auth
  - ca-strong-auth
  - ca-risk-auth

HANDLERS
--------
handlers are stored in ca-adv-auth and shared using meta dependencies

notify:
name: restart webfort


License
BSD

Author Information
------------------
created by drew mullen rmullen@paychex.com
