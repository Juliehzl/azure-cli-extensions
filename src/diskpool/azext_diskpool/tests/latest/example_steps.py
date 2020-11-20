# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /DiskPools/put/Create or Update a Disk Pool
@try_manual
def step_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool create '
             '--name "{myDiskPool}" '
             '--location "westus" '
             '--availability-zones "1" '
             '--disks "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/vm-name_D'
             'ataDisk_0" '
             '--disks "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/vm-name_D'
             'ataDisk_1" '
             '--subnet-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetw'
             'orks/{vn}/subnets/default" '
             '--sku name="Standard_ABC" '
             '--tags key="value" '
             '--resource-group "{rg}"',
             checks=checks)
    test.cmd('az disk-pool wait --created '
             '--name "{myDiskPool}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /DiskPools/get/Get a diskPool
@try_manual
def step_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool show '
             '--name "{myDiskPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DiskPools/get/List Disk Pools
@try_manual
def step_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DiskPools/get/List Disk Pools by subscription
@try_manual
def step_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool list '
             '-g ""',
             checks=checks)


# EXAMPLE: /DiskPools/patch/Update Disk Pool
@try_manual
def step_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool update '
             '--name "{myDiskPool}" '
             '--location "westus" '
             '--availability-zones "1" '
             '--disks "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/vm-name_D'
             'ataDisk_0" '
             '--disks "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/vm-name_D'
             'ataDisk_1" '
             '--subnet-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetw'
             'orks/{vn}/subnets/default" '
             '--tags key="value" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IscsiTargets/put/Create or Update an iSCSI Target
@try_manual
def step_iscsi_target_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool iscsi-target create '
             '--disk-pool-name "{myDiskPool}" '
             '--name "{myIscsiTarget}" '
             '--target-iqn "iqn.2005-03.org.iscsi:server1" '
             '--tpgs "[{{\\"acls\\":[{{\\"credentials\\":{{\\"password\\":\\"some_pa$$word\\",\\"username\\":\\"some_us'
             'ername\\"}},\\"initiatorIqn\\":\\"iqn.2005-03.org.iscsi:client\\",\\"mappedLuns\\":[\\"lun0\\"]}}],\\"att'
             'ributes\\":{{\\"authentication\\":true,\\"prodModeWriteProtect\\":false}},\\"luns\\":[{{\\"name\\":\\"lun'
             '0\\",\\"managedDiskAzureResourceId\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/M'
             'icrosoft.Compute/disks/vm-name_DataDisk_1\\"}}]}}]" '
             '--resource-group "{rg}"',
             checks=checks)
    test.cmd('az disk-pool iscsi-target wait --created '
             '--name "{myIscsiTarget}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /IscsiTargets/get/Get an iscsiTarget
@try_manual
def step_iscsi_target_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool iscsi-target show '
             '--disk-pool-name "{myDiskPool}" '
             '--name "{myIscsiTarget}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IscsiTargets/get/List Disk Pools by Resource Group
@try_manual
def step_iscsi_target_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool iscsi-target list '
             '--disk-pool-name "{myDiskPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IscsiTargets/delete/Delete an iscsiTarget
@try_manual
def step_iscsi_target_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool iscsi-target delete -y '
             '--disk-pool-name "{myDiskPool}" '
             '--name "{myIscsiTarget}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DiskPools/delete/Update Disk Pool
@try_manual
def step_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az disk-pool delete -y '
             '--name "{myDiskPool}" '
             '--resource-group "{rg}"',
             checks=checks)
