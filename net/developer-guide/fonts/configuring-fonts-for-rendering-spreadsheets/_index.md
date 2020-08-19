---
title: Configuring Fonts for Rendering Spreadsheets
type: docs
weight: 10
url: /net/configuring-fonts-for-rendering-spreadsheets/
---

## **Possible Usage Scenarios**

Aspose.Cells APIs provide the facility to render the spreadsheets in image formats as well as convert them to PDF & XPS formats. In order to maximize the conversion fidelity, it is necessary that the fonts used in the spreadsheet should be available in the operating system's default font directory. In case the required fonts are not present then the Aspose.Cells APIs will try to substitute the required fonts with the ones available.

## **Selection of Fonts**

Below is the process that Aspose.Cells APIs follow behind the scene.

1. The API tries to find the fonts on the file system matching the exact font name used in the spreadsheet.
1. If API cannot find the fonts with the exact same name, it attempts to use the default font specified under the Workbook's **[DefaultStyle.Font](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/font)** property.
1. If API cannot locate the font defined under the workbook's **[DefaultStyle.Font](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/font)** property, it attempts to select the most suitable fonts from all of the available fonts.
1. Finally, if API cannot find any fonts on the file system, it renders the spreadsheet using Arial.

## **Set Custom Font Folders**

Aspose.Cells APIs search the operating system's default font directory for the required fonts. In case the required fonts are not available in the system's font directory then the APIs search through the custom (user defined) directories. The **[FontConfigs](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs)** class has exposed a number of ways to set custom font directories as detailed below.

1. **[FontConfigs.SetFontFolder](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: This method is useful if there is only one folder to be set.
1. **[FontConfigs.SetFontFolders](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: This method is useful when the fonts reside in multiple folders and the user wishes to set all folders separately rather than combining all fonts in a single folder.
1. **[FontConfigs.SetFontSources](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: This mechanism is useful when the user wishes to load fonts from multiple folders or a single font file or font data from an array of bytes.

{{% alert color="primary" %}}

Both **[FontConfigs.SetFontFolder](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** methods accept a Boolean type second parameter. Passing **true** as the second parameter will direct the Aspose.Cells APIs to search the subfolders for the fonts files.

{{% /alert %}}

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Please use any of the above-mentioned methods at the start of the application, that is; before invoking any other objects of Aspose.Cells APIs.

{{% /alert %}} {{% alert color="primary" %}}

If all of the above-mentioned methods are used to set the font sources, only the last settings will take effect.

{{% /alert %}}

## **Font Substitution Mechanism**

Aspose.Cells APIs also provide the ability to specify the substitute font for rendering purposes. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as an alternative to the originally required font. In order to achieve this, the Aspose.Cells APIs have exposed the **[FontConfigs.SetFontSubstitutes](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** method which accepts 2 parameters. The first parameter is of type **string**, which should be the name of the font that needs to be substituted. The second parameter is an array of type **string**. Users can provide a list of font names as a substitution to the original font name (specified in the first parameter).

Here is a simple usage scenario.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Information Gathering**

In addition to above-mentioned methods, the Aspose.Cells APIs have also provided means to gather information on what sources and substitutions have been set.

1. **[FontConfigs.GetFontSources](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** method returns an array of type **[FontSourceBase](https://apireference.aspose.com/cells/net/aspose.cells/fontsourcebase)** containing the list of specified font sources. In case, no sources have been set, the **[FontConfigs.GetFontSources](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** method will return an empty array.
1. **[FontConfigs.GetFontSubstitutes](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** method accepts a parameter of type **string** allowing to specify the font name for which substitution has been set. In case, no substitution has been set for the specified font name then the **[FontConfigs.GetFontSubstitutes](https://apireference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** method will return null.
