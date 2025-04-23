---  
title: 使用Node.js通过C++将Excel转换为带有工具提示的HTML  
linktitle: 将 Excel 转换为带有工具提示的 HTML  
type: docs  
weight: 200  
url: /zh/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: 学习如何使用Aspose.Cells for Node.js via C++将Excel文件转换为HTML格式，并带有工具提示以完整显示文本。  
---  

## **将 Excel 转换为带有工具提示的 HTML**

可能会存在文本在生成的HTML中被截断的情况，你希望在悬停时显示完整文本作为工具提示。Aspose.Cells for Node.js via C++支持此功能，通过提供[**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--)属性。将[**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--)属性设置为**true**会在生成的HTML中添加完整文本作为工具提示。

以下图片显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载[源Excel文件](98107416.xlsx)并生成带有提示的[输出HTML文件](98107417.zip)。

示例代码

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

