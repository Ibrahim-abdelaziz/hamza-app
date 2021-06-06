
from napalm import get_network_driver
import json
 
 
def connection(host, username, password):
    driver = get_network_driver('ios')
    iosvl2 = driver(host, username, password)
    iosvl2.open()
    print("connected to :", host)
    return iosvl2
 
 
def getconfig(host, username, password):
    iosvl2 = connection(host, username, password)
    output = iosvl2.get_config()
    config_list = output.get('running').splitlines()
    json_config = json.dumps(config_list, sort_keys=True, indent=4)
    config_list = json.loads(json_config)
    iosvl2.close()
    return config_list
 
 
def getacl(file):
    line = []
    for item in file:
        if item.strip(' ').startswith('access-list'):
            line.append(item)
    if line:
        for item in line:
            print(item)
            print(item)
        print('ACLs configured')
    else:
        print('no ACL configured')
 
 
def getaccessclass(file):
    line = []
    for item in file:
        if item.strip(' ').startswith('access-class'):
            line.append(item)
    if line:
        for item in line:
            print(item)
        print('access-class configured')
    else:
        print('no access-class configured')
 
 
def getssh2(file):
    version2 = []
    ssh = []
    for item in file:
        if item.strip(' ') == 'ip ssh version 2':
            version2 = item
        if item.strip(' ') == 'transport input ssh':
            ssh = item
 
    if version2:
        print('ssh 2 configured')
    else:
        print('no ssh 2 configured')
 
    if ssh:
        print('ssh is forced')
    else:
        print('ssh is not forced')
 
 
def getaaa(file):
    aaa = []
    authentication = []
    for item in file:
        if item.strip(' ') == 'aaa new-model':
            aaa = item
        if item.strip(' ').startswith('aaa authentication'):
            aaa = item
    if aaa:
        print('aaa model created')
    else:
        print('no aaa model created')
 
    if authentication:
        print('aaa authentication is configured')
    else:
        print('aaa authentication is not configured')
 
 
def getntp(file):
    ntp = []
    for item in file:
        if item.strip(' ').startswith('ntp server'):
            ntp.append(item)
 
    if ntp:
        print('ntp is configured')
    else:
        print('ntp is not configured')
 
# sur interface mode access
# cdp neighbor interface verif
 
def getbpdu_guard(file):
    guard = []
    for item in file:
        if item.strip(' ') == 'spanning-tree bpduguard enable':
            guard = item
    if guard:
        print('spanning-tree bpduguard is configured')
    else:
        print('spanning-tree bpduguard is not configured')
 
 
def getsnmpv3(file):
    snmp = []
    for item in file:
        if 'v3' in item and item.strip(' ').startswith('snmp-server'):
            snmp = item
 
    if snmp:
        print('SNMPv3 is configured')
    else:
        print('SNMPv3 is not configured')
 
# vlan configured
def getarp(file):
    arp = []
    for item in file:
        if item.strip(' ').startswith('ip arp inspection'):
            snmp = item
    if arp:
        print('ARP inspection is configured')
    else:
        print('ARP inspection is not configured')
 
# vlan
def getdhcpsnooping(file):
    dhcp = []
    for item in file:
        if item.strip(' ').startswith('ip dhcp snooping vlan'):
            snmp = item
 
    if dhcp:
        print('DHCP snooping is configured')
    else:
        print('DHCP snooping is not configured')
 
 
def getbackup(file):
    archive = []
    for item in file:
        if item.strip(' ') == 'archive' or item.strip(' ').startswith('path'):
            archive = item
 
    if archive:
        print('Backup is configured')
    else:
        print('Backup is not configured')
 
 

def check_ip(ip, user, password):
    config = getconfig(ip, user, password)
    getacl(config)
    getaccessclass(config)
    getssh2(config)
    getaaa(config)
    getntp(config)
    getbpdu_guard(config)
    getsnmpv3(config)
    getarp(config)
    getdhcpsnooping(config)
    getbackup(config)