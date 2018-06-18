USAGE
-----
create an inventory create a playbook to run this and or additional roles

Role Name
this role installs advanced auth 9.0.2

Requirements
------------
java is expected to be installed at /opt/java
tomcat is expected to be installed at /opt/tomcat

Role Variables
--------------
**You must provide the following vars:**
- arcot_enc_masterkey
- arcot_db_password

`java_home`: 
- where java has been installed
- Default: `/opt/java`

`catalina_home`: 
- where tomcat has been installed
- Default: `/opt/tomcat`

`arcot_home`: 
- where advanced auth tools will be installed
- Default: `/opt/CA/AdvAuth`

## DB Config
**These properties populte the silent install file and can be found in installer.properties.j2 template**


`arcot_config_db`: 
- 
- Default: `true`

`arcot_db_port`:

- Default: `1521`

`arcot_db_user`:

- Default: `ARCOTUSER`

`arcot_db_password`: 
- Default: `''`

`arcot_db_host`: 
- Default: `''`

`arcot_sid`: 
- Default: `''`

`arcot_dsn`: 
- Default: `''`

`arcot_service_name`: 
- Default: `''`

# initalize DB - only desired on blank DBs
`arcot_init_db`:
- Default: `0`

# will auto run db upgrade scripts
`arcot_upgrade_db`: 
- Default: `0`


# bootstrap the admin console - only desireable on blank DBs
`arcot_bootstrap`: 
- Default: `0`
`arcot_masteradmin_pw`: 
- Default: `master1234!`

`arcot_default_org_key`: 
- Default: `master1234!`

`sample_app`: 
- Default: `False`

`str_zip_dir`: 
- Default: `GEN500000000000116`

`str_bin`: 
- Default: `CA-StrongAuthentication-9.0.0-Linux-Installer.bin`

`rsk_zip_dir`: 
- Default: `GEN500000000000127`

`rsk_bin`: 
- Default: `CA-RiskAuthentication-9.0.0-Linux-Installer.bin`

`arcot_user`: 
- Default: `arcot`

`arcot_password`: 
- Default: `''`

# ROLE: ca-adv-auth
#Download URLs
`rsk_auth_install_url`: 
- Default: `''`

`str_auth_install_url`: 
- Default: `''`

`JDBC_driver_url`: 
- Default: `''`


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
