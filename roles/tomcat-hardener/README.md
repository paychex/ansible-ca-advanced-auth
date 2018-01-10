USAGE
-----

`ansible-playbook -u rmullen -k -i inventory site.yml`

create an inventory
create a playbook to run this and or additional roles


Role Name
=========

hardening rules came from: https://wiki.paychex.com/display/WEBENG/PWM+build+information

Requirements
------------

tomcat must be installed, recommend using tomcat ansible role

Role Variables
--------------

DEFAULTS:
java_home
catalina_home
tomcat_install_url

please make var changes in the tomcat/vars/main.yml, not defaults/main.yml
adjusted var names have not been tested

Example Playbook
----------------

site.yml

---

- hosts: rsk-app
  become: true
  roles:
    - tomcat-hardener


HANDLERS
--------
if any files are updated notify the 'restart tomcat' handler will fire

notify:
name: restart tomcat


License
-------

BSD

Author Information
------------------

created by drew mullen rmullen@paychex.com
