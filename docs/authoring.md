# Authoring

The commands for Command modules and Extensions are authored in the same way. See [Authoring Commands](https://github.com/Azure/azure-cli/blob/master/doc/authoring_command_modules/authoring_commands.md) for authoring guidance.

## Common Flows

This represents the most common sequence of steps you would perform to create, test and publish your extension.

### Setup

Development of extensions have been simplified by the public release of the azdev CLI. Please visit https://github.com/Azure/azure-cli-dev-tools for more information.

1. In a new virtual environment, install azdev: `pip install azdev`
2. Setup your CLI and install your extension:
  - If you prefer to be guided via an interactive experience, just run `adev setup` with no additional arguments.
  - If you are creating a brand new extension, run `azdev setup -r <PATH>` to add the repo to your extension dev sources. From there you can run `azdev extension create` to generate and install starter code.
  - If you are only developing on an existing extension, run: `azdev setup -r <PATH> -e <NAME>` where PATH is the path to the local git folder your extension resides in and NAME is the name of your extension. If you don't know the name of the extension, you can omit `-e` to complete the setup. Then you can run `azdev extension list -o table` to see which extensions are installable for your repo and add that extension with `azdev extension add <NAME>`.
  - If you would like to develop for a CLI module and your extension, run the above, but include `-c [<CLI_PATH>]` where CLI_PATH is the path to your local Azure CLI repo. If omitted, the command will attempt to find the repo by crawling your current working directory.

### Create

Run `azdev extension create <NAME>` to create skeleton code for a new extension. As an example (for a fictional widget API):

```
azdev extension create  widget --local-sdk <PATH TO SDK ZIP> --operation-name WidgetOperations --client-name WidgetManagementClient --sdk-property widget_name --github-alias myalias
```

The fields `--operation-name`, `--client-name` and `--sdk-property` will come from a review of your Python SDK.

After running `azdev extension create`, your extension should be installed in **dev mode** and you should be set to begin developing.

```
.
|-- azext_<EXTENSION_NAME>
|   |-- __init__.py
|   |-- _client_factory.py
|   |-- _help.py
|   |-- _params.py
|   |-- _validators.py
|   |-- azext_metadata.json
|   |-- commands.py
|   |-- custom.py
|   |-- profiles.py (Optional)
|   |-- tests
|       |-- __init__.py
|       |-- latest
|           |-- __init__.py
|           |-- test_xxx.py
|           |-- recordings
|               `-- test_xxx.yml
|   |-- vendored_sdks
|       |-- __init__.py
|       |-- <SOURCE_SDK>
`-- HISTORY.rst
|-- README.rst/README.md
`-- setup.cfg
`-- setup.py
```
Important file/folder:
1. [azext_matadata.json](metadata.md)
2. vendored_sdks/__init__.py to package folder in your extension wheel.
```Python
__import__('pkg_resources').declare_namespace(__name__)
```
3. README 
  - Follow [Extension Summary Guidelines](extension_summary_guidelines.md)

### Validate

Periodically run the following to ensure your extension will pass CI:

`azdev style <NAME>`
`azdev test <NAME>`
`azdev linter <NAME>`

Address comments as appropriate and consult the CLI team if something is unclear.

### Publish

Once your extension is ready, you need to build and publish the WHL file to a public location and optionally advertise the new extension in the repo's index.json file for discoverability. 

For public extensions that are published to a storage account, the following command will accomplish all of this.

`azdev extension publish <NAME> --update-index [--storage-account NAME --storage-container NAME --storage-subscription GUID]`

Notes: 
1. This command will complete the following tasks:
    - Build the whl file for extension.
	  - Upload the whl file to azure-cli-extension blob.
	  - Update index.json with new download url, file name and sha256Digest. 

The storage fields can be stored in your config file or as environment variables so you need not supply them every time. Once the publish command has been run (you must be logged in to the Azure CLI for it to succeed), you can open a PR that will contain your code changes and the index update. This used to be done in two steps.

In summary, after the code change, please remember the following steps when you publish an extension, particularly for existing extensions.

Take storage-preview for example:

1. Update the version number

https://github.com/Azure/azure-cli-extensions/blob/master/src/storage-preview/setup.py#L11
	
2. Update the HISTORY file
	
https://github.com/Azure/azure-cli-extensions/blob/master/src/storage-preview/HISTORY.rst
	
3. Run `azdev extension publish [extension-name]  --storage-account azurecliprod --update-index --storage-container cli-extensions` with --storage-subscription if required
	
Notes:
 The older version of extension may be removed from [index.json](https://github.com/Azure/azure-cli-extensions/blob/master/src/index.json).

## Uncommon Flows

These are operations you may never need to do, or only do occasionally.

### Register Custom Resource Types
1. Define CustomResourceType in profile.py
```Python
from azure.cli.core.profiles import CustomResourceType

CUSTOM_DATA_STORAGE = CustomResourceType('azext_storage_preview.vendored_sdks.azure_storage', None)
CUSTOM_DATA_STORAGE_ADLS = CustomResourceType('azext_storage_preview.vendored_sdks.azure_adls_storage_preview', None)
CUSTOM_MGMT_STORAGE = CustomResourceType('azext_storage_preview.vendored_sdks.azure_mgmt_storage',
                                         'StorageManagementClient')
CUSTOM_MGMT_PREVIEW_STORAGE = CustomResourceType('azext_storage_preview.vendored_sdks.azure_mgmt_preview_storage',
                                                 'StorageManagementClient')
```
2. Register in __init__.py
```Python
class StorageCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType

        register_resource_type('latest', CUSTOM_DATA_STORAGE, '2018-03-28')
        register_resource_type('latest', CUSTOM_DATA_STORAGE_ADLS, '2019-02-02-preview')
        register_resource_type('latest', CUSTOM_MGMT_STORAGE, '2018-07-01')
        register_resource_type('latest', CUSTOM_MGMT_PREVIEW_STORAGE, '2018-03-01-preview')
        storage_custom = CliCommandType(operations_tmpl='azext_storage_preview.custom#{}')

        super(StorageCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                    resource_type=CUSTOM_DATA_STORAGE,
                                                    custom_command_type=storage_custom,
                                                    command_group_cls=StorageCommandGroup,
                                                    argument_context_cls=StorageArgumentContext)
```
3. Register again for tests against target profile if you want to use these resource types
- latest\__init__.py
```Python
from azure.cli.core.profiles import register_resource_type
from ...profiles import CUSTOM_MGMT_STORAGE
register_resource_type('latest', CUSTOM_MGMT_STORAGE, '2018-03-01-preview')
```
- latest\test_xx.py
```Python
@api_version_constraint(CUSTOM_MGMT_STORAGE, min_api='2017-06-01')
@ResourceGroupPreparer(location='southcentralus')
def test_create_storage_account_with_assigned_identity(self, resource_group):\
  ...
```

### Building

`azdev extension build <NAME>`

This will create a `dist` directory containing your `.whl` extension.

The `.whl` is the artifact that can be installed with the `az extension add` command. You will rarely need to use this command, however. Instead, you will most likely use the publish command.

### Trying out your extension

Normally, you will have you extension installed in dev mode and your code changes will be immediately testable. However, if you want to test a generated WHL file specfically, follow these directions.

**(Step 1)** Build the extension to generate a WHL file.

`azdev extension build myexampleextesion`

**(Step 2)** Uninstall the dev extension.

`azdev extension remove myexampleextension`

Verify it is removed:
```
az extension list -ojson
[]
```

**(Step 3)** Add the extension using the path to the `.whl`:

`az extension add --source ~/Dev/myexampleextension/dist/FILENAME.whl`

You can verify the extension was installed as follows:

```
az extension list -ojson
[
  {
    "extensionType": "whl",
    "name": "myexampleextension",
    "version": "0.0.1"
  }
]
```

## Extension Metadata (optional)

Additional metadata can be added to your extension.

See [Extension Metadata](metadata.md) for more information.


## Tips/Notes

### What can I import in my extension?

- You can import any of the modules available inside of azure-cli-core.
- You can also import any of its dependencies (see [azure-cli-core setup.py](https://github.com/Azure/azure-cli/blob/master/src/azure-cli-core/setup.py)).
- You can choose to add your own dependencies if required but keep the next point in mind...

### Limit dependencies in setup.py

- Before adding a dependency to your setup.py, check that it's not already available in [azure-cli-core setup.py](https://github.com/Azure/azure-cli/blob/master/src/azure-cli-core/setup.py).
- For Azure SDKs, use autorest to generate your SDK into a package that isn't under the `azure` directory.
- You can verify that your extension doesn't use the `azure` directory by opening your `.whl` and opening the `top_level.txt` file in the `*.dist-info` directory. It should not contain `azure`.

### How do I know I'm using my dev extension(s)?

- When you run `az --version` it will list your normal extensions directory as well as any directories being used to find developer extensions. Developer extensions will appear in the output with a path next to the version number.

Example:
```
(e-env) E:\Projects\AzureCLI>az --version
azure-cli                         2.0.79

command-modules-nspkg              2.0.3
core                              2.0.79
nspkg                              3.0.4
telemetry                          1.0.4
testsdk                            0.2.4

Extensions:
alias                              0.5.2
db-up                             0.1.13
interactive                        0.4.3
storage-ors-preview                0.1.0 (dev) E:\Projects\AzureCLI\azure-cli-extensions\src\storage-ors-preview
storage-preview                   0.2.10 (dev) E:\Projects\AzureCLI\azure-cli-extensions\src\storage-preview

Python location 'E:\Projects\AzureCLI\azure-cli-extensions\e-env\Scripts\python.exe'
Extensions directory 'C:\Users\zuh\.azure\cliextensions'
Development extension sources:
    E:\Projects\AzureCLI\azure-cli-extensions
```

- `az extension list`

Example:
```
[
  {
    "extensionType": "whl",
    "name": "alias",
    "version": "0.5.2"
  },
  {
    "extensionType": "whl",
    "name": "db-up",
    "version": "0.1.13"
  },
  {
    "extensionType": "whl",
    "name": "interactive",
    "version": "0.4.3"
  },
  {
    "extensionType": "dev",
    "name": "storage-ors-preview",
    "version": "0.1.0"
  },
  {
    "extensionType": "dev",
    "name": "storage-preview",
    "version": "0.2.10"
  }
]
```
### Test your extension on both Python 2 & 3

- The CLI supports both Python 2 & 3 so verify that your extension does the same.
- You can create both a Python 2 and 3 virtual environment and run your extension in both.
- e.g. `virtualenv env27` and `virtualenv -p /usr/local/bin/python3 env`.


:zap: IMPORTANT :zap:
- Since azure-cli uses the `azure` directory, no extension can use this.
- This applies to all other dependencies used by azure-cli-core.
- See [this Stack Overflow question](https://stackoverflow.com/questions/8936884/python-import-path-packages-with-the-same-name-in-different-folders).


Also, see the [FAQ](faq.md).
