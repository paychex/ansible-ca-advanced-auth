USAGE
-----
ansible-playbook -u rmullen -k -i inventory -e "strong_auth_install= yes sample_app=yes" site.yml

create an inventory create a playbook to run this and or additional roles

Role Name
this role installs tomcat 7.0.81

Requirements
------------
java is expected to be installed and located at /opt/jdk1.7.0_21

Role Variables
--------------
DEFAULTS: java_home catalina_home tomcat_install_url

please make var changes in the tomcat/vars/main.yml, not defaults/main.yml adjusted var names have not been tested

Example Playbook
site.yml

hosts: rsk-app become: true roles:
tomcat

HANDLERS
--------
if the zip file is updated the unzip playbook should notify the 'restart tomcat' handler

notify:
name: restart tomcat

License
BSD

Author Information
------------------
created by drew mullen rmullen@paychex.com
