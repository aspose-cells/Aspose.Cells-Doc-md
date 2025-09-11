---
title: Configuring Fonts for Rendering Spreadsheets with Node.js via C++
linktitle: Configuring Fonts for Rendering Spreadsheets
type: docs
weight: 10
url: /nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Learn how to configure fonts for rendering spreadsheets using Aspose.Cells for Node.js via C++. Ensure fonts are available for optimal conversion fidelity.
---

## **Possible Usage Scenarios**

Aspose.Cells APIs provide the facility to render the spreadsheets in image formats as well as convert them to PDF & XPS formats. In order to maximize the conversion fidelity, it is necessary that the fonts used in the spreadsheet should be available in the operating system's default font directory. In case the required fonts are not present, then the Aspose.Cells APIs will try to substitute the required fonts with the ones available.

## **Selection of Fonts**

Below is the process that Aspose.Cells APIs follow behind the scene.

1. The API tries to find the fonts on the file system matching the exact font name used in the spreadsheet.
1. If API cannot find the fonts with the exact same name, it attempts to use the default font specified under the Workbook's [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) property.
1. If API cannot locate the font defined under the workbook's [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) property, it attempts to use the font specified under [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) or [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property.
1. If API cannot locate the font defined under [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) or [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) property, it attempts to use the font specified under [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) property.
1. If API cannot locate the font defined under [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) property, it attempts to select the most suitable fonts from all of the available fonts.
1. Finally, if API cannot find any fonts on the file system, it renders the spreadsheet using Arial.

## **Set Custom Font Folders**

Aspose.Cells APIs search the operating system's default font directory for the required fonts. In case the required fonts are not available in the system's font directory, then the APIs search through the custom (user-defined) directories. The [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) class has exposed a number of ways to set custom font directories as detailed below.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): This method is useful if there is only one folder to be set.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): This method is useful when the fonts reside in multiple folders and the user wishes to set all folders separately rather than combining all fonts in a single folder.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): This mechanism is useful when the user wishes to load fonts from multiple folders or a single font file or font data from an array of bytes.

{{% alert color="primary" %}}

Both [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) & [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) methods accept a Boolean type second parameter. Passing **true** as the second parameter will direct the Aspose.Cells APIs to search the subfolders for the fonts files.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Please use any of the above-mentioned methods at the start of the application, that is; before invoking any other objects of Aspose.Cells APIs.

{{% /alert %}} {{% alert color="primary" %}}

If all of the above-mentioned methods are used to set the font sources, only the last settings will take effect.

{{% /alert %}}

## **Font Substitution Mechanism**

Aspose.Cells APIs also provide the ability to specify the substitute font for rendering purposes. This mechanism is helpful when a required font is not available on the machine where conversion has to take place. Users can provide a list of font names as an alternative to the originally required font. In order to achieve this, the Aspose.Cells APIs have exposed the [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) method which accepts 2 parameters. The first parameter is of type **string**, which should be the name of the font that needs to be substituted. The second parameter is an array of type **string**. Users can provide a list of font names as a substitution for the original font name (specified in the first parameter).

Here is a simple usage scenario.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Information Gathering**

In addition to the above-mentioned methods, the Aspose.Cells APIs have also provided means to gather information on what sources and substitutions have been set.

1. [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) method returns an array of type [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) containing the list of specified font sources. In case, no sources have been set, the [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) method will return an empty array.
1. [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) method accepts a parameter of type **string** allowing to specify the font name for which substitution has been set. In case, no substitution has been set for the specified font name then the [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) method will return null.

## **Advance topics**
- [Set Default Font while rendering spreadsheet to images](/cells/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority](/cells/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Supported Font Formats](/cells/nodejs-cpp/supported-font-formats/)
- [Worksheet to Image - Set Pixel Format for the Rendered Image](/cells/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}