---  
title: 用 Node.js 在工作表中移动单元格范围  
linktitle: 移动工作表中的单元格范围  
type: docs  
weight: 370  
url: /zh/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 移动工作表中的单元格范围。  
---  

{{% alert color="primary" %}}  
本文介绍了如何移动工作表中的单元格范围。  
{{% /alert %}}  

## **在工作表中移动单元格范围**  
示例代码使用模板文件演示了该任务。  

**输入文件**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

请参阅以下生成的文件，范围 A1:B5 移动到 C1:D5。  

**输出文件**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
