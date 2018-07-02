USAGE
-----
create an inventory create a playbook to run this and or additional roles

Role Name
this role installs advanced auth 9.0.2

Requirements
------------
- java is expected to be installed at /opt/java
- tomcat is expected to be installed at /opt/tomcat

Recommended Runtime Vars
------------------------
**You must provide the following vars:**
- arcot_enc_masterkey
- properties_db_password
- arcot_os_password

## DB Config
**These properties populte the silent install file and can be found in installer.properties.j2 template**


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

`properties_db_initialize `:
- Default: `0`

`properties_db_upgrade`: 
- Default: `0`

`properties_bootstrap`: 
- Default: `0`
`properties_admin_pw`: 
- Default: `master1234!`

`properties_default_org_key`: 
- Default: `master1234!`

## App Config
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

`arcot_install_sample_app`: 
- Default: `False`

`arcot_strong_zip_parent_dir`: 
- Default: `GEN500000000000116`

`arcot_strong_installer`: 
- Default: `CA-StrongAuthentication-9.0.0-Linux-Installer.bin`

`arcot_risk_zip_parent_dir`: 
- Default: `GEN500000000000127`

`arcot_risk_installer`: 
- Default: `CA-RiskAuthentication-9.0.0-Linux-Installer.bin`

`arcot_os_user`: 
- Default: `arcot`

`arcot_os_password`: 
- Default: `''`

## Download URLs
`arcot_risk_url`: 
- Default: `''`

`arcot_strong_url`: 
- Default: `''`

`jdbc_driver_url`: 
- Default: `''`

`arcot_adapter_patch_url`:
- Default: ''

`arcot_patch_url`:
- Default: ''

HANDLERS
--------
handlers are stored in ca-adv-auth and shared using meta dependencies

notify:
name: restart webfort


TODO
----
- auto execute oracle db scripts where required

License
BSD

Author Information
------------------
created by drew mullen rmullen@paychex.com
