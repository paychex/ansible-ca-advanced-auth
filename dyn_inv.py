#!/usr/bin/python
"""Creates an ansible dynamic inventory for multiple hostgroups based on foreman_query() calls

    EXECUTION EXAMPLE:
        `sudo ansible all -i dynamic_inv.py -m ping`
        `sudo ansible <hostgroup_name> -i dynamic_inv.py -m ping`
        `sudo ansible-playbook -i dynamic_inv.py site.yml`

    DESCRIPTION
    User constructs a dictonary of lists used in foreman_query() calls which returns json objects used to construct dynamic inventory hostgroups

    REQUIREMENTS
        Install foreman_query.py
            Should be pre-installed and pre-referenced on all ansible machines (sys.path.append('/opt/ansible/extras/dynamic_inv'))
            If not, download from: https://code.paychex.com/projects/IA/repos/scorecards/browse/files/jobs/foreman_query.py

    TO USE
    1. Create a copy of this file and rename it for your playbook
    3. Create the foreman_query() list queries
    4. Add to playbook_dict{}
        - keys should be hostgroup names
        - values should be the list for each hostgroup
    5. `chmod +x <dynamic_inv>.py`

    EXTRA INFO:

    The foreman envinronment referenced is deteremined by the `facter | grep payx_environment` value on the executing machine

    ANSIBLE EXPECTED OUTPUT FORMAT
    A nested json object: a dictonary containing a dictonary containing a list containing a string
    ex1:    dict(dict(list['server.pxlabus.com']))

    ex2:    {'group_name_1':{ 'hosts':['FQDN.pxlabus.com', 'FQDN2.pxlabus.com']},
             'group_name_2':{'hosts': ['FQDN2.pxlabus.com','FQDN4.pxlabus.com']}
            }

    Created by Drew Mullen rmullen@paychex.com
"""
import sys
sys.path.append('/opt/ansible/extras/dynamic_inv')
import foreman_query


###############< CHANGE THESE VALUES >###################
# 1. Create the foreman_query() lists
group_query = [['params.payx_advauthrole','rsk-app']]
group_query2 = [['params.payx_advauthrole','rsk-web']]

# 2. Add to playbook_dict{}
#     - keys should be hostgroup names (ansible references these)
#     - values should be the list for each hostgroup (the hosts that you'd list in your inv group)
playbook_dict = {'rsk-app': group_query, 'rsk-web': group_query2}
###########< DO NOT CHANGE BELOW >###############


def main(playbook_dict):
    # For every key in playbook_dict
        # foreman_query(value)
        # construct group_list
        # reassign key value to = {'hosts':[server_names]}
    for key, value in playbook_dict.items():
        group_list = foreman_query.get_names(value)

        playbook_dict[key] = {'hosts': group_list}
    playbook_dict.update({'_meta':{'hostvars':{}}})
    print playbook_dict

if __name__ == '__main__':
  main(playbook_dict)

