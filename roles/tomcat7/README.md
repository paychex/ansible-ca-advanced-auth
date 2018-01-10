USAGE
-----

`ansible-playbook -u rmullen -k -i inventory site.yml`

create an inventory
create a playbook to run this and or additional roles


Role Name
=========

this role installs tomcat 9.0.2

Requirements
------------

java is expected to be installed and located at /opt/java

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
    - tomcat


HANDLERS
--------
if the zip file is updated the unzip playbook should notify the 'restart tomcat' handler

notify:
name: restart tomcat


License
-------

BSD

Author Information
------------------

created by drew mullen rmullen@paychex.com
