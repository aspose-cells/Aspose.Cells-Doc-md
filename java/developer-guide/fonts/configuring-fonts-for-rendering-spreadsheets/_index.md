---
title: Configuring Fonts for Rendering Spreadsheets
type: docs
weight: 10
url: /java/configuring-fonts-for-rendering-spreadsheets/
---

## **Possible Usage Scenarios**

Aspose.Cells APIs provide the facility to render the spreadsheets in image formats as well as convert them to PDF & XPS formats. In order to maximize the conversion fidelity, it is necessary that the fonts used in the spreadsheet should be available in the operating system's default font directory. In case the required fonts are not present then the Aspose.Cells APIs will try to substitute the required fonts with the ones available.

## **Selection of Fonts**

Below is the process that Aspose.Cells APIs follow behind the scene.

1. The API tries to find the fonts on the file system matching the exact font name used in the spreadsheet.
1. If API cannot find the fonts with the exact same name, it attempts to use the default font specified under the Workbook's [**DefaultStyle.Font**](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Font) property.
1. If API cannot locate the font defined under the workbook's [**DefaultStyle.Font**](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Font) property, it attempts to select the most suitable fonts from all of the available fonts.
1. Finally, if API cannot find any fonts on the file system, it renders the spreadsheet using Arial.

{{% alert color="primary" %}}

The Aspose.Cells APIs always scans the operating system's default font directory with one exception, that is; when JVM arguments **-DAspose.Cells.FontDirExc="YourFontDir"** are set. In that case, the Aspose.Cells APIs will skip scanning the operating system's default font directory and only search the path as specified in the aforementioned JVM arguments.

{{% /alert %}}

## **Set Custom Font Folders**

Aspose.Cells APIs search the operating system's default font directory for the required fonts. In case the required fonts are not available in the system's font directory then the APIs search through the custom (user defined) directories. The [**FontConfigs**](https://apireference.aspose.com/cells/java/com.aspose.cells/FontConfigs) class has exposed a number of ways to set custom font directories as detailed below.

1. [**FontConfigs.setFontFolder**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): This method is useful if there is only one folder to be set.
1. [**FontConfigs.setFontFolders**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): This method is useful when the fonts reside in multiple folders and the user wishes to set all folders separately rather than combining all fonts in a single folder.
1. [**FontConfigs.setFontSources**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): This mechanism is useful when the user wishes to load fonts from multiple folders or a single font file or font data from an array of bytes.

{{% alert color="primary" %}}

Both [**FontConfigs.setFontFolder**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)) methods accept a Boolean type second parameter. Passing **true** as second parameter will direct the Aspose.Cells APIs to search the sub folders for the fonts files.

{{% /alert %}}

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Please use any of the above mentioned methods at the start of the application, that is; before invoking any other objects of Aspose.Cells APIs.

{{% /alert %}} {{% alert color="primary" %}}

If more than one of the above-mentioned methods are used to set the font sources, only the last settings will take effect.

{{% /alert %}}

## **Font Substitution Mechanism**

Aspose.Cells APIs also provide the ability to specify the substitute font for rendering purposes. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as an alternative to the originally required font. In order to achieve this, the Aspose.Cells APIs have exposed the FontConfigs.setFontSubstitutes method which accepts 2 parameters. The first parameter is of type **String**, which should be the name of the font which needs to be substituted. The second parameter is an array of type **String**. Users can provide a list of font names as substitutes to the original font (specified in the first parameter).

Here is a simple usage scenario.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Information Gathering**

In addition to above-mentioned methods, the Aspose.Cells APIs have also provided means to gather information on what sources and substitutions have been set.

1. [**FontConfigs.getFontSources**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()): This method returns an array of type [**FontSourceBase**](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFontSource) containing the list of specified font sources. In case, no sources have been set, the [**FontConfigs.getFontSources**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) method will return an empty array.
1. [**FontConfigs.getFontSubstitutes**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)): This method accepts a parameter of type **String** allowing to specify the font name for which substitution has been set. In case, no substitution has been set for the specified font name then the [**FontConfigs.getFontSubstitutes**](https://apireference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) method will return null.
