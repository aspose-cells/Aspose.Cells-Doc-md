---
title: 使用C++为Node.js配置字体以呈现电子表格
linktitle: 配置字体以渲染电子表格
type: docs
weight: 10
url: /zh/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: 学习如何使用Aspose.Cells for Node.js via C++配置字体以渲染电子表格。确保字体可用以获得最佳转换效果。
---

## **可能的使用场景**

Aspose.Cells API提供渲染电子表格为图片格式，以及转换为PDF和XPS格式的功能。为了最大化转换的准确性，必须确保电子表格中使用的字体已在操作系统的默认字体目录中。如果缺少所需字体，Aspose.Cells API将尝试用可用的字体进行替代。

## **选择字体**

以下是 Aspose.Cells API 在幕后执行的过程。

1. API试图在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
1. 如果API无法找到具有相同名称的精确字体，则尝试使用工作簿的[**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)属性下指定的默认字体。
1. 如果API无法找到工作簿的[**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)属性下定义的字体，则尝试使用[**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--)或[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)属性下指定的字体。
1. 如果API无法找到[**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--)或[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)属性下定义的字体，则尝试使用[**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--)属性下指定的字体。
1. 如果API无法找到[**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--)属性下定义的字体，则尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

## **设置自定义字体文件夹**

Aspose.Cells API在操作系统的默认字体目录中搜索所需字体。如未找到，API会在自定义（用户定义）目录中搜索。[**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs)类提供了多种设置自定义字体目录的方法。

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-)：如果只有一个要设置的文件夹，则此方法很有用。
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-)：当字体存在于多个文件夹中，而用户希望将所有文件夹分开设置而不是将所有字体合并到一个文件夹中时，此方法很有用。
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-)：当用户希望从多个文件夹加载字体或从字节数组加载单个字体文件或字体数据时，此机制很有用。

{{% alert color="primary" %}}

Both [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) 和 [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) 方法接受一个布尔类型的第二个参数。 将 **true** 作为第二个参数传递将指示 Aspose.Cells API 在子文件夹中搜索字体文件。

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

请在应用程序启动时使用以上任一方法，在调用 Aspose.Cells API 的其他对象之前使用。

{{% /alert %}} {{% alert color="primary" %}}

如果使用所有上述方法设置字体源，则只有最后一次设置将生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells API还提供了指定替代字体以便渲染的能力。当目标机器上没有所需字体时，此机制非常有用。用户可以提供一份字体名称列表作为替代。为实现此功能，Aspose.Cells API提供了接受两个参数的[**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-)方法，第一个参数为**string**类型，表示需要替代的字体名称，第二个参数为**string**数组，列出作为原字体替代的字体名称。

这里是一个简单的使用场景。

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

## **信息收集**

除上述方法外，Aspose.Cells API还提供了收集已设置的源和替代信息的方式。

 1. [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--)方法返回一个包含指定字体源列表的[**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase)类型数组。如果未设置任何源，[**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--)方法将返回空数组。
 1. [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-)方法接受一个**string**类型的参数，可以用来指定已设置替代的字体名。如未为该字体名设置替代，则[**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-)方法返回null。

## **高级主题**
- [在将电子表格呈现为图像时设置默认字体](/cells/zh/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级](/cells/zh/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/nodejs-cpp/supported-font-formats/)
- [电子表格转图像 - 设置呈现图像的像素格式](/cells/zh/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
