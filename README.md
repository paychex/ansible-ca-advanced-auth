# USAGE

-----
It is my intention that you consume this role by populating an inventory with hosts + vars. Meaning, all key installation concerns take their direction from variables. You can populate those vars in your inventory or vars/. If a feature you need is not satisfied by a variable, create the feature and open a PR, please. 

Overview

-----

This role installs strong auth 9, risk auth 9, and adapter 9. It then applies patch 9.0.02 to all those tools. Although it does a full adapter install, it only deploys statemanager. But it would be easy to extend (PR welcome).

Requirements

-----

- linux installation
- java is expected to be installed at /opt/java
- tomcat is expected to be installed at /opt/tomcat
- oracle DB is currently expected
- CA zip files not included and are expected to be accessible via wget at runtime

TODO

-----

- auto execute oracle db scripts where required
- auto upgrade db
- oracle RAC setup
- check files/ for downloads first & change download to control then push to host

Recommended Runtime Vars

-----

**You must provide the following vars:**

- properties_enc_masterkey
- properties_db_password
- arcot_os_password

## Example 

I have an inventory that defines the desired config and a playbook to mary the inv to the role. I also pass some vars during execution.


### Playbook

    - hosts: rm-app
      become: true
      roles:
          - /home/rmullen/git/roles/tomcat9
          - /home/rmullen/git/advanced_auth

### Inventory

    [rm-app]
    riskminder-app.hostname.com

    [rm-app:vars]
    properties_db_host=dbhostname
    properties_db_sid=mydbsid
    properties_db_dsn='adsnname'

    arcot_risk_url=http://example.com/file.zip
    arcot_strong_url=http://example.com/file.zip
    jdbc_driver_url=http://example.com/file.zip
    tomcat_install_url=http://example.com/file.zip
    arcot_adapter_patch_url=http://example.com/file.zip
    arcot_patch_url=http://example.com/file.zip
    arcot_patch_update=true
    arcot_adapter_install=true
    arcot_web_services=true

    pip_configure_proxy=true
    pip_proxy_url=http://example.com/
    pip_trusted_host=example.com

### Execute

    ansible-playbook -i <your_inventory_file> <your_playbook_that_calls_role> -e "properties_enc_masterkey=<your_masterkey> properties_db_password=<your_db_password> arcot_os_password=<your_password>"



## Variables

### DB Config

**These properties populate the silent install file and can be found in installer.properties.j2 template**

`properties_configure_db`: 

- the arcotcommon.ini db 
- Default: `true`

`properties_db_port`:

- Default: `1521`

`properties_db_user`:

- Default: `ARCOTUSER`

`properties_db_password`: 

- Default: `''`

`properties_db_host`: 

- Default: `''`

`properties_db_sid`: 

- Default: `''`

`properties_db_dsn`: 

- Default: `''`

`properties_db_service_name`: 

- Default: `''`

`properties_db_initialize`:

- Default: `0`

`properties_db_upgrade`: 

- Default: `0`

`properties_bootstrap`: 

- Default: `0`

`properties_admin_pw`: 

- Default: `master1234!`

`properties_default_org_key`: 

- Default: `master1234!`

`properties_enc_masterkey`:

- password for the encryption key `securestore.enc`
- Default: `master1234!`

### App Config

**These vars determine where the apps will be installed**

`java_home`: 

- where java has been installed
- Default: `/opt/java`

`catalina_home`: 

- where tomcat has been installed
- Default: `/opt/tomcat`

`arcot_home`: 

- where advanced auth tools will be installed
- Default: `/opt/CA/AdvAuth`

`arcot_adapter_install_home`:

- where adapter installs. The default installs to the same /opt/CA/AdvAuth. This value is only needed because of what appear to be inconsistenencies in the installation procedure across tools.
- Default: `/opt`

`arcot_web_services`:

- Installs the webapps to tomcat
- Default: true

`arcot_install_sample_app`: 

- Default: `False`

`arcot_strong_zip_parent_dir`: 

- name of the sub directory in strong auth zip
- Default: `GEN500000000000116`

`arcot_strong_installer`: 

- Default: `CA-StrongAuthentication-9.0.0-Linux-Installer.bin`

`arcot_risk_zip_parent_dir`: 

- name of the sub directory in risk auth zip
- Default: `GEN500000000000127`

`arcot_risk_installer`: 

- Default: `CA-RiskAuthentication-9.0.0-Linux-Installer.bin`

`arcot_os_user`: 

- name for the service owning user
- Default: `arcot`

`arcot_os_password`: 

- password for the os user
- Default: `''`

`arcot_patch_update`:

- boolean, true to install patches 9.02_patch.yml
- Default: false

`arcot_3.x_db_update`:

- boolean, true to install 3.x db update. [CA Docs](https://docops.ca.com/ca-advanced-authentication/9-0/en/upgrading/upgrade-from-older-versions)
- Default: false

`arcot_db_upgrade_zip_dir`:

- folder name that zip unpacks
- Default: `GEN500000000000104`

`arcot_db_upgrade_AA_dir`:

- name of sub folder zip creates
- Default: `AA-Upgrade-6.2.x-7.x-2.2.6-above-3.x-to-9.0`

`arcot_db_upgrade_zip_url`: 

- URL used to download upgrade zip file
- Default: ''


### Download URLs

URLs for downloading components. Recommend these are hosted internally

`arcot_risk_url`: 

- Default: `''`

`arcot_strong_url`: 

- Default: `''`

`jdbc_driver_url`: 

- Default: `''`

`arcot_adapter_patch_url`:

- Default: `''`

`arcot_patch_url`:

- Default: `''`

HANDLERS

-----

start stack

License

Apache 2.0

Author Information

created by drew mullen rmullen@paychex.com
