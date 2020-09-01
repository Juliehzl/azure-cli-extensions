# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.profiles import CustomResourceType

CUSTOM_MGMT_STORAGE = CustomResourceType('azext_storage_mgmt_preview.vendored_sdks.azure_mgmt_storage',
                                         'StorageManagementClient')
