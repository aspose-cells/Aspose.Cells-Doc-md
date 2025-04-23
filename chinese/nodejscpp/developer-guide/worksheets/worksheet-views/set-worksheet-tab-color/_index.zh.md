---  
title: 通过Node.js和C++设置工作表标签颜色  
linktitle: 设置工作表标签颜色  
type: docs  
weight: 120  
url: /zh/nodejs-cpp/set-worksheet-tab-color/  
description: 本文展示了用于通过Node.js在C++中程序化设置Excel工作表标签颜色的示例代码。  
keywords: 设置Excel标签颜色通过Node.js和C++，代码示例  
---  

{{% alert color="primary" %}}  

Aspose.Cells允许您更改单个工作表标签的颜色，使其与其他工作表区分开。例如，您可以将支出设置为红色，销售设置为绿色，资产设置为蓝色，等等。

{{% /alert %}}  
## **使用Microsoft Excel设置工作表标签颜色**  
1. 在当前工作表底部的标签工作表上右键单击。  
1. 选择**标签颜色**。  
1. 从调色板中选择一种颜色。  
1. 点击**确定**。  
## **使用Aspose.Cells设置工作表选项卡颜色**  
以下示例代码显示如何使用Aspose.Cells来设置选项卡颜色。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

