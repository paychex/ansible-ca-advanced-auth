# Overview

-----

This is an ansible role that installs strong auth 9, risk auth 9, and adapter 9. It then applies patch 9.0.02 to all those tools. Although it does a full adapter install, it only deploys statemanager. But it would be easy to extend (PR welcome). Its intended for system admins / engineers who want to manage their CA tool configurations via code.

USAGE

-----

It is my intention that you consume this role by populating an inventory with hosts + vars. Meaning, all key installation concerns take their direction from variables. You can populate those vars in your inventory or vars/. If a feature you need is not satisfied by a variable, create the feature and open a PR, please. 

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

- arcot_db_password
- arcot_os_password

Recommend including:

- arcot_install_enc_masterkey

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
    arcot_db_host=dbhostname
    arcot_db_sid=mydbsid
    arcot_db_dsn='adsnname'

    build_environment='n2a'

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

    ansible-playbook -i <your_inventory_file> <your_playbook_that_calls_role> -e "arcot_install_enc_masterkey=<your_masterkey> arcot_db_password=<your_db_password> arcot_os_password=<your_password>"



## Variables

### Role Options

`arcot_adapter_install_home`:

- where adapter installs. The default installs to the same /opt/CA/AdvAuth. This value is only needed because of what appear to be inconsistenencies in the installation procedure across tools.
- Default: `/opt`

`arcot_patch_update`:

- boolean, true to install patches 9.02_patch.yml
- Default: false

`arcot_web_services`:

- Installs the webapps to tomcat
- Default: true

`arcot_3.x_db_update`:

- boolean, true to install 3.x db update. [CA Docs](https://docops.ca.com/ca-advanced-authentication/9-0/en/upgrading/upgrade-from-older-versions)
- Default: false

`arcot_db_rac`:

- boolean, true to configure for a RAC DB
- Default: false

`arcot_install_sample_app`: 

- boolean, true to install risk / web sample apps
- Default: `False`

`jdbc_64_bit`:

- boolean, true for 64 bit CPUs.
- Default: `true`

`pip_configure_proxy`:

- boolean, true will configure pip proxy settings
- Default: `false`


### Installation Properties File Options

**These properties populate the silent install file and can be found in installer.properties.j2 template**


`arcot_install_configure_db`: 

- the arcotcommon.ini db 
- Default: `true`

`arcot_install_db_initalize`:

- Default: `0`

`arcot_install_db_upgrade`:

- Default: `0`

`arcot_install_bootstrap`:

- Default: `0`

`arcot_install_admin_pw`:

- Default: `'master1234!'`

`arcot_install_default_org_key`:

- Default: `'master1234!'`

`arcot_install_enc_masterkey`:

- password for the encryption key `securestore.enc`
- Default: `'master1234!'`

### Database Information

`arcot_db_port`:

- Default: `1521`

`arcot_db_user`:

- Default: `ARCOTUSER`

`arcot_db_password`:

- Default: No default. You must set this

`arcot_db_host`: 

- Default: `''`

`arcot_db_sid`: 

- Default: `''`

`arcot_db_dsn`: 

- Default: `''`

`arcot_db_rac_service_name`: 

- Default: `''`

`arcot_db_rac_section_name`: 

- Default: `''`

`arcot_db_rac_shared_datafile_path`: 

- Default: `''`

`arcot_db_rac_connect_string`: 

- Default: `''`

`arcot_db_rac_desc_additions`: 

- Default: `''`

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

`arcot_db_upgrade_zip_dir`:

- folder name that zip unpacks
- Default: `GEN500000000000104`

`arcot_db_upgrade_AA_dir`:

- name of sub folder zip creates
- Default: `AA-Upgrade-6.2.x-7.x-2.2.6-above-3.x-to-9.0`

### System User

`arcot_os_user`: 

- name for the service owning user
- Default: `arcot`

`arcot_os_password`:

- password for the os user
- Default: None. You must supply


### Download URLs

URLs for downloading components. Recommend these are hosted internally

`arcot_risk_url`: 

- Default: `'http://example.com/CA-RiskAuthentication-9.0.0-Linux-Installer.zip'`

`arcot_strong_url`: 

- Default: `'http://example.com/CA-StrongAuthentication-9.0.0-Linux-Installer.zip'`

`jdbc_driver_url`: 

- Default: `'http://example.com/ojdbc8.jar'`

`arcot_adapter_patch_url`:

- Default: `'http://example.com/CA-Adapter-Patch-9.0.02-Linux.zip'`

`arcot_patch_url`:

- Default: `'http://example.com/CA-AdvancedAuthentication-Patch-9.0.02-Linux.zip'`

`arcot_db_upgrade_zip_url`:

- URL used to download upgrade zip file
- Default: `'http://example.com/GEN500000000000104.zip'`

`arcot_sm_url`:

- URL to download statemanager properties file
- Default: `'http://example.com/arcotsm.properties'`

`pip_proxy_url`:

- URL to set as pip proxy
- Default: `'http://host.example.com'`

`pip_trusted_host`:

- Host to set as trusted
- Default: `'host.example.com'`

HANDLERS

-----

start stack

License

Apache 2.0

Author Information

created by drew mullen rmullen@paychex.com
