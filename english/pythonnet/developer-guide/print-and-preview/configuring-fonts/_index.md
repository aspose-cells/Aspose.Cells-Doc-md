---
title: Configuring Fonts for Rendering Spreadsheets
type: docs
weight: 10
url: /python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Possible Usage Scenarios**

Aspose.Cells for Python via .NET APIs provide the facility to render the spreadsheets in image formats as well as convert them to PDF & XPS formats. In order to maximize the conversion fidelity, it is necessary that the fonts used in the spreadsheet should be available in the operating system's default font directory. In case the required fonts are not present then the Aspose.Cells for Python via .NET APIs will try to substitute the required fonts with the ones available.

## **Selection of Fonts**

Below is the process that Aspose.Cells for Python via .NET APIs follow behind the scene.

1. The API tries to find the fonts on the file system matching the exact font name used in the spreadsheet.
1. If API cannot find the fonts with the exact same name, it attempts to use the default font specified under the Workbook's [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) property.
1. If API cannot locate the font defined under the workbook's [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) property, it attempts to use the font specified under [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) or [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property.
1. If API cannot locate the font defined under [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) or [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property, it attempts to use the font specified under [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) property.
1. If API cannot locate the font defined under [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) property, it attempts to select the most suitable fonts from all of the available fonts.
1. Finally, if API cannot find any fonts on the file system, it renders the spreadsheet using Arial.

## **Set Custom Font Folders**

Aspose.Cells for Python via .NET APIs search the operating system's default font directory for the required fonts. In case the required fonts are not available in the system's font directory then the APIs search through the custom (user defined) directories. The [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) class has exposed a number of ways to set custom font directories as detailed below.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): This method is useful if there is only one folder to be set.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): This method is useful when the fonts reside in multiple folders and the user wishes to set all folders separately rather than combining all fonts in a single folder.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): This mechanism is useful when the user wishes to load fonts from multiple folders or a single font file or font data from an array of bytes.

{{% alert color="primary" %}}

Both [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) & [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) methods accept a Boolean type second parameter. Passing **true** as the second parameter will direct the Aspose.Cells for Python via .NET APIs to search the subfolders for the fonts files.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Please use any of the above-mentioned methods at the start of the application, that is; before invoking any other objects of Aspose.Cells for Python via .NET APIs.

{{% /alert %}} {{% alert color="primary" %}}

If all of the above-mentioned methods are used to set the font sources, only the last settings will take effect.

{{% /alert %}}

## **Font Substitution Mechanism**

Aspose.Cells for Python via .NET APIs also provide the ability to specify the substitute font for rendering purposes. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as an alternative to the originally required font. In order to achieve this, the Aspose.Cells for Python via .NET APIs have exposed the [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) method which accepts 2 parameters. The first parameter is of type **string**, which should be the name of the font that needs to be substituted. The second parameter is an array of type **string**. Users can provide a list of font names as a substitution to the original font name (specified in the first parameter).

Here is a simple usage scenario.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Information Gathering**

In addition to above-mentioned methods, the Aspose.Cells for Python via .NET APIs have also provided means to gather information on what sources and substitutions have been set.

1. [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) method returns an array of type [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) containing the list of specified font sources. In case, no sources have been set, the [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) method will return an empty array.
1. [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) method accepts a parameter of type **string** allowing to specify the font name for which substitution has been set. In case, no substitution has been set for the specified font name then the [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) method will return null.

## **Advance topics**
- [Set Default Font while rendering spreadsheet to images](/cells/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority](/cells/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Supported Font Formats](/cells/python-net/supported-font-formats/)
- [Worksheet to Image - Set Pixel Format for the Rendered Image](/cells/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

