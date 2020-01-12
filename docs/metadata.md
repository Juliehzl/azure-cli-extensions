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
![avatar](https://github.com/Juliehzl/azure-cli-extensions/blob/authoring/docs/assets/extensionversion.png)

3. When you want to install an extension, you only can install the available extension based on your installed cli core version.

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
![avatar](https://github.com/Juliehzl/azure-cli-extensions/blob/authoring/docs/assets/extensionpreview.png)
<img src="https://github.com/Juliehzl/azure-cli-extensions/blob/authoring/docs/assets/extensionpreview.png" width = "400" height = "260" alt="preview" 
align=center>
