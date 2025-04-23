---
title: 使用Aspose.Cells for Node.js via C++计算IFNA函数
description: 如何通过C++的Node.js使用Aspose.Cells库计算IFNA函数。加载现有Excel文件或创建新文件，然后计算IFNA函数以获取结果。最后，将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells，Excel，IFNA函数，计算，Node.js通过C++
type: docs
weight: 40
url: /zh/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持计算Excel中的IFNA函数。如果公式返回#N/A错误值，IFNA函数会返回你指定的值，否则返回公式的结果。

{{% /alert %}} 
## **使用Aspose.Cells for Node.js via C++计算IFNA函数**
以下示例代码演示了如何使用Aspose.Cells for Node.js via C++计算IFNA函数。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
