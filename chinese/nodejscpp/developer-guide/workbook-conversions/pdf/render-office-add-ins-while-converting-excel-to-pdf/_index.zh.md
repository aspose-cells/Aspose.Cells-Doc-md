---
title: 在将Excel转换为PDF时使用Node.js通过C++渲染Office加载项
linktitle: 转换Excel为PDF时呈现Office加载项
type: docs
weight: 100
url: /zh/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **可能的使用场景**

早期，Aspose.Cells 在将 Excel 文件保存为 PDF 格式时无法渲染 Office 插件。现在 Aspose.Cells 可以正常渲染。您无需使用任何特殊方法或属性来在输出 PDF 中渲染 Office 插件。只需将您的 Excel 文件保存为 PDF 格式，它将自动渲染 Office 插件。

## **在将Excel转换为PDF时呈现Office加载项**

以下示例代码保存了包含Office加载项的[示例Excel文件](60489769.xlsx)。请查看[之前版本（即17.11）生成的输出PDF](60489770.pdf)和[较新版本（即17.12及之后版本）生成的输出PDF](60489771.pdf)。之前版本的输出PDF为空白，但较新版本的输出PDF显示了Office加载项。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
