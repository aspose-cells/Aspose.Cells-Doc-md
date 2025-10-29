---
title: 使用 C++ via Node.js 在保存为PDF时仅更改单个Unicode字符的字体
linktitle: 在保存为PDF时仅更改特定Unicode字符的字体
type: docs
weight: 260
url: /zh/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: 了解如何在使用Aspose.Cells for Node.js via C++保存为PDF时更改单个Unicode字符的字体。 
---

{{% alert color="primary" %}} 

一些Unicode字符无法使用用户指定的字体显示。其中一个这样的Unicode字符是**非间断连字**（U+2011），其Unicode编号为8209。这个字符不能用**Times New Roman**显示，但可以用其他字体如**Arial Unicode MS**显示。

 当某个字符出现在一些单词或句子中，而这些内容使用特定字体（如Times New Roman）时，Aspose.Cells会将整个单词或句子的字体更改为可以显示该字符的字体，如Arial Unicode MS或MS。

 然而，对于一些用户来说，这种行为是不理想的，他们希望只改变该特定字符的字体，而不是更改整个单词或句子的字体。

 为了解决这个问题，Aspose.Cells提供了`PdfSaveOptions.isFontSubstitutionCharGranularity`属性，应将其设置为true，以便只更改那些无法显示的特定字符的字体为可显示的字体，而其余的单词或句子仍然保持原始字体。

{{% /alert %}} 

## **示例**
以下屏幕截图比较了以下示例代码生成的两个输出PDF。

 一个是在不设置`PdfSaveOptions.isFontSubstitutionCharGranularity`属性的情况下生成的，另一个是在设置`PdfSaveOptions.isFontSubstitutionCharGranularity`属性为true后生成的。

 如第一个PDF所示，由于非断字符号，整个句子的字体由Times New Roman变为Arial Unicode MS。而在第二个PDF中，只有非断字符号的字体发生了变化。

| **第一个PDF文件** |
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


| **第二个PDF文件** |
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **示例代码**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



{{< app/cells/assistant language="nodejs-cpp" >}}
