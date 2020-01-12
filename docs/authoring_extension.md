The document provides instructions and guidelines on how to author individual extension.


**AUTHORING EXTENSION**
=============================

## Create an extenison
```
azdev extension create [extension-name]
```
Note: 
1. For more information about azdev, please refer to https://github.com/Azure/azure-cli-dev-tools.
2. CodeGen

### Azure CLI Extension template structure


## Author your extension

- [Azure CLI Command Guideline](https://github.com/Azure/azure-cli/blob/dev/doc/command_guidelines.md)
- [Azure CLI Command Authoring](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md)

### vendored_sdk

Note:
1. Please make sure your vendored_sdk folder has _init_.py file if you want to package this folder in your extension wheel.

### Register Custom ResourceType


### azext_metadata.json
```
{
    "azext.isPreview": true,
    "azext.minCliCoreVersion": "2.0.67",
    "azext.maxCliCoreVersion": "2.1.0"
}
```
- azext.isPreview
- azext.minCliCoreVersion/azext.maxCliCoreVersion
![avatar][base64str]
Notes:
1. When CLI core version is lower than required version of your installed extension, the following error will be thrown

2. When you want to install an extension, you only can install the available extension based on your installed cli core version.

You can use `az extension list-available` to find all available extension version information.

## Publish an extension
After the code change, please remember the following steps when you publish an extension, particularly for existing extensions.

Take storage-preview for example:

1. Update the version number

https://github.com/Azure/azure-cli-extensions/blob/master/src/storage-preview/setup.py#L11
	
2. Update the HISTORY file
	
https://github.com/Azure/azure-cli-extensions/blob/master/src/storage-preview/HISTORY.rst
	
3. Run `azdev extension publish [extension-name]  --storage-account azurecliprod --update-index --storage-container cli-extensions` with --storage-subscription if required
	
Notes: 
This command will complete the following tasks:
    - Build the whl file for storage-preview extension.
	- Upload the whl file to azure-cli-extension blob.
	- Update index.json with new download url, file name and sha256Digest. The older version of extension may be removed from [index.json](https://github.com/Azure/azure-cli-extensions/blob/master/src/index.json).
	