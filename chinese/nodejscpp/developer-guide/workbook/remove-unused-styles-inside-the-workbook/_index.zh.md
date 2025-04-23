---  
title: 用 Node.js 通过 C++ 删除工作簿中的未使用样式  
linktitle: 删除工作簿中的未使用样式  
type: docs  
weight: 340  
url: /zh/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 从工作簿中删除未使用的样式。  
---  

{{% alert color="primary" %}}  
未使用的样式不仅占用空间，还会在转换为PDF、HTML等不同格式时引发性能问题。Aspose.Cells提供了[**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--)以删除工作簿内所有未使用的样式。  
{{% /alert %}}  

以下代码说明了[**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--)的用法。该代码加载了[模板Excel文件](5115520.xlsx)，可以通过提供的链接下载。它包含一个名为**AsposeStyle**的未使用样式；执行后，此样式及所有其他未使用样式将被删除。  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

