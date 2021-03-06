# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_vmware_site_create
from .example_steps import step_vmware_site_show
from .example_steps import step_hyperv_cluster_show
from .example_steps import step_hyperv_cluster_list
from .example_steps import step_hyperv_host_show
from .example_steps import step_hyperv_host_list
from .example_steps import step_hyperv_machine_show
from .example_steps import step_hyperv_machine_list
from .example_steps import step_hyperv_run_as_account_show
from .example_steps import step_hyperv_run_as_account_list
from .example_steps import step_hyperv_site_create
from .example_steps import step_hyperv_site_show
from .example_steps import step_hyperv_site_delete
from .example_steps import step_vmware_machine_show
from .example_steps import step_vmware_machine_list
from .example_steps import step_vmware_run_as_account_show
from .example_steps import step_vmware_run_as_account_list
from .example_steps import step_vmware_vcenter_show
from .example_steps import step_vmware_vcenter_list
from .example_steps import step_vmware_site_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg_5, rg_6, rg_7, rg_8):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg_5, rg_6, rg_7, rg_8):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg_5, rg_6, rg_7, rg_8):
    setup_scenario(test, rg_5, rg_6, rg_7, rg_8)
    step_vmware_site_create(test, rg_5, rg_6, rg_7, rg_8, checks=[
        test.check("name", "{mySite2}", case_sensitive=False),
    ])
    step_vmware_site_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_cluster_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_cluster_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_host_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_host_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_machine_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_machine_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_run_as_account_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_run_as_account_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_site_create(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_site_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_hyperv_site_delete(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_machine_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_machine_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_run_as_account_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_run_as_account_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_vcenter_show(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_vcenter_list(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    step_vmware_site_delete(test, rg_5, rg_6, rg_7, rg_8, checks=[])
    cleanup_scenario(test, rg_5, rg_6, rg_7, rg_8)


# Test class for Scenario
@try_manual
class OffazureScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(OffazureScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'mySite': 'hyperv121319c813site',
            'mySite2': 'appliance1e39site',
            'mySite3': 'pajind_site1',
            'mySite4': 'rahasapp122119d37csite',
            'myVCenter': '10-150-8-50-6af5f800-e9f6-56ff-9c3c-7be56d242c31',
            'myProject4': 'default',
            'myMachine3': '96d27052-052b-48db-aa84-b9978eddbf5d',
            'myMachine4': 'machine1',
        })

    @ResourceGroupPreparer(name_prefix='clitestoffazure_ipsahoo-RI-121119'[:7], key='rg_5', parameter_name='rg_5')
    @ResourceGroupPreparer(name_prefix='clitestoffazure_pajindTest'[:7], key='rg_6', parameter_name='rg_6')
    @ResourceGroupPreparer(name_prefix='clitestoffazure_myResourceGroup'[:7], key='rg_7', parameter_name='rg_7')
    @ResourceGroupPreparer(name_prefix='clitestoffazure_rahasijaBugBash050919'[:7], key='rg_8', parameter_name='rg_8')
    def test_offazure_Scenario(self, rg_5, rg_6, rg_7, rg_8):
        call_scenario(self, rg_5, rg_6, rg_7, rg_8)
        calc_coverage(__file__)
        raise_if()
