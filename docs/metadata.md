Extension Metadata
==================

Additional metadata can be added to your extension.

This is useful if you want to:
- Specify a version contract for your extension and the CLI.
- etc.


How To
------

Create the file `azext_metadata.json` under your extension.

For example `azext_*/azext_metadata.json`.

In your `setup.py`, include the following:
``` python
package_data={'azext_*': ['azext_metadata.json']}
```

Now, the CLI will be able to read your extension metadata.

Note: Replace `*` with your module name.

Python documentation - [Installing Package Data](https://docs.python.org/2/distutils/setupscript.html#installing-package-data)


Metadata Format
---------------
Example:
```
{
    "azext.isPreview": true,
    "azext.minCliCoreVersion": "2.0.67",
    "azext.maxCliCoreVersion": "2.1.0"
}
```

This documents the known metadata entries.
- azext.isPreview
- azext.minCliCoreVersion/azext.maxCliCoreVersion

Note: You can optionally extend this with your own metadata by adding your own namespace. We use the `azext` namespace.

### azext.minCliCoreVersion
Description: The minimum CLI core version required (inclusive).
Exclude to not specify a minimum.

Type: `string`

Example: `"azext.minCliCoreVersion": "2.0.67"`

Note:
1. 2.0.67 is a widely used minCliCoreVersion number, because there are some breaking changes and new features invloved in this version.
e.g. new flag like `is_preview`
2. When CLI core version is lower than required version of your installed extension, the following error will be thrown:
<img src="https://github.com/Juliehzl/azure-cli-extensions/blob/authoring/docs/assets/extensionversion.png" width = "820" height = "74" alt="version" 
align=center>
3. An extension can have different versions with different azure cli core requirement. When user want to install an extension, they only can install the available extension based on your installed cli core version.
For example,
```
 "storage-preview": [
            {
                "downloadUrl": "https://azurecliprod.blob.core.windows.net/cli-extensions/storage_preview-0.2.8-py2.py3-none-any.whl",
                "filename": "storage_preview-0.2.8-py2.py3-none-any.whl",
                "metadata": {
                    "azext.isPreview": true,
                    "azext.minCliCoreVersion": "2.0.52",
                    "classifiers": [
                        "Development Status :: 4 - Beta",
                        "Intended Audience :: Developers",
                        "Intended Audience :: System Administrators",
                        "Programming Language :: Python",
                        "Programming Language :: Python :: 2",
                        "Programming Language :: Python :: 2.7",
                        "Programming Language :: Python :: 3",
                        "Programming Language :: Python :: 3.4",
                        "Programming Language :: Python :: 3.5",
                        "Programming Language :: Python :: 3.6",
                        "License :: OSI Approved :: MIT License"
                    ],
                    "extensions": {
                        "python.details": {
                            "contacts": [
                                {
                                    "email": "azpycli@microsoft.com",
                                    "name": "Microsoft Corporation",
                                    "role": "author"
                                }
                            ],
                            "document_names": {
                                "description": "DESCRIPTION.rst"
                            },
                            "project_urls": {
                                "Home": "https://github.com/Azure/azure-cli-extensions/tree/master/src/storage-preview"
                            }
                        }
                    },
                    "generator": "bdist_wheel (0.30.0)",
                    "license": "MIT",
                    "metadata_version": "2.0",
                    "name": "storage-preview",
                    "summary": "Provides a preview for upcoming storage features.",
                    "version": "0.2.8"
                },
                "sha256Digest": "a3d48247051e95847ded28217433c4b98fc02d6ee21eedfcb24dd43f7360569d"
            },
            {
                "downloadUrl": "https://azurecliprod.blob.core.windows.net/cli-extensions/storage_preview-0.2.9-py2.py3-none-any.whl",
                "filename": "storage_preview-0.2.9-py2.py3-none-any.whl",
                "metadata": {
                    "azext.isPreview": true,
                    "azext.minCliCoreVersion": "2.0.67",
                    "classifiers": [
                        "Development Status :: 4 - Beta",
                        "Intended Audience :: Developers",
                        "Intended Audience :: System Administrators",
                        "Programming Language :: Python",
                        "Programming Language :: Python :: 2",
                        "Programming Language :: Python :: 2.7",
                        "Programming Language :: Python :: 3",
                        "Programming Language :: Python :: 3.4",
                        "Programming Language :: Python :: 3.5",
                        "Programming Language :: Python :: 3.6",
                        "License :: OSI Approved :: MIT License"
                    ],
                    "extensions": {
                        "python.details": {
                            "contacts": [
                                {
                                    "email": "azpycli@microsoft.com",
                                    "name": "Microsoft Corporation",
                                    "role": "author"
                                }
                            ],
                            "document_names": {
                                "description": "DESCRIPTION.rst"
                            },
                            "project_urls": {
                                "Home": "https://github.com/Azure/azure-cli-extensions/tree/master/src/storage-preview"
                            }
                        }
                    },
                    "generator": "bdist_wheel (0.30.0)",
                    "license": "MIT",
                    "metadata_version": "2.0",
                    "name": "storage-preview",
                    "summary": "Provides a preview for upcoming storage features.",
                    "version": "0.2.9"
                },
                "sha256Digest": "880e01de0fab8893770497ef9410559ae223a1f09dbd6a23712226ab4e2d5ecb"
            },
            {
                "downloadUrl": "https://azurecliprod.blob.core.windows.net/cli-extensions/storage_preview-0.2.10-py2.py3-none-any.whl",
                "filename": "storage_preview-0.2.10-py2.py3-none-any.whl",
                "metadata": {
                    "azext.isPreview": true,
                    "azext.minCliCoreVersion": "2.0.67",
                    "classifiers": [
                        "Development Status :: 4 - Beta",
                        "Intended Audience :: Developers",
                        "Intended Audience :: System Administrators",
                        "Programming Language :: Python",
                        "Programming Language :: Python :: 2",
                        "Programming Language :: Python :: 2.7",
                        "Programming Language :: Python :: 3",
                        "Programming Language :: Python :: 3.4",
                        "Programming Language :: Python :: 3.5",
                        "Programming Language :: Python :: 3.6",
                        "License :: OSI Approved :: MIT License"
                    ],
                    "extensions": {
                        "python.details": {
                            "contacts": [
                                {
                                    "email": "azpycli@microsoft.com",
                                    "name": "Microsoft Corporation",
                                    "role": "author"
                                }
                            ],
                            "document_names": {
                                "description": "DESCRIPTION.rst"
                            },
                            "project_urls": {
                                "Home": "https://github.com/Azure/azure-cli-extensions/tree/master/src/storage-preview"
                            }
                        }
                    },
                    "generator": "bdist_wheel (0.30.0)",
                    "license": "MIT",
                    "metadata_version": "2.0",
                    "name": "storage-preview",
                    "summary": "Provides a preview for upcoming storage features.",
                    "version": "0.2.10"
                },
                "sha256Digest": "8c87013be456849f27ea7f76df284e998e6f3911d3de478ec19abe84bb30fbe9"
            }
        ],
```

Users will install different storage-preview version when they run `az extension add -n storage-preview`:
- When 2.0.52 <= version < 2.0.67, `az extension add -n storage-preview` will install storage-preview 2.0.8
- When version >= 2.0.67, `az extension add -n storage-preview` will install storage-preview 2.0.10


You can use `az extension list-available` to find all available extension version information.

### azext.maxCliCoreVersion
Description: The maximum CLI core version required (inclusive).
Exclude to not specify a maximum.

Type: `string`

Example: `"azext.maxCliCoreVersion": "2.1.0"`

Note:
1. 2.1.0 is also a widely used maxCliCoreVersion number in existing extensions. (alomost 10 extensions)
2. When applying new version shcema, we should be care about these extensions.

### azext.isPreview
Description: Indicate that the extension is in preview.

Type: `boolean`

Example: `"azext.isPreview": true`

Notes:
1. The following message will be shown up when users run the commands in your extension with `"azext.isPreview": true` :
<img src="https://github.com/Juliehzl/azure-cli-extensions/blob/authoring/docs/assets/extensionpreview.png" width = "820" height = "67" alt="preview" 
align=center>
