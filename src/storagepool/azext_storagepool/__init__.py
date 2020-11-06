# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azext_storagepool.generated._help import helps  # pylint: disable=unused-import
try:
    from azext_storagepool.manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass


class StoragePoolManagementCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_storagepool.generated._client_factory import cf_storagepool_cl
        storagepool_custom = CliCommandType(
            operations_tmpl='azext_storagepool.custom#{}',
            client_factory=cf_storagepool_cl)
        parent = super(StoragePoolManagementCommandsLoader, self)
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=storagepool_custom)

    def load_command_table(self, args):
        from azext_storagepool.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_storagepool.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError:
            pass
        return self.command_table

    def load_arguments(self, command):
        from azext_storagepool.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_storagepool.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError:
            pass


COMMAND_LOADER_CLS = StoragePoolManagementCommandsLoader
