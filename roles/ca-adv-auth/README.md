USAGE
-----


Role Name
=========

this role installs ca AdvAuth 9

Requirements
------------

java and tomcat are expected to be installed and located at /opt/java & /opt/tomcat

Role Variables
--------------

DEFAULTS:
rsk_auth_install_url
str_auth_install_url
JDBC_driver_url
java_home
arcot_home
catalina_home

please make var changes in the ca-adv-auth/vars/main.yml, not defaults/main.yml
adjusted var names have not been tested

Example Playbook
----------------

site.yml

---

- hosts: rsk-app
  become: true
  roles:
    - tomcat9
    - ca-adv-auth


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
