---  
title: 通过Node.js与C++指定数据范围和切片群组位置，复制Sparkline。  
linktitle: 通过指定数据范围和 Sparkline 组的位置来复制 Sparkline  
type: docs  
weight: 300  
url: /zh/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: 学习如何使用Aspose.Cells for Node.js via C++通过指定数据范围和切片群组位置在Excel中复制Sparkline。  
---  

{{% alert color="primary" %}}  
Microsoft Excel允许您通过指定火花线组的数据范围和位置来复制火花线。Aspose.Cells支持此功能。  
{{% /alert %}}  

在Microsoft Excel中复制火花线到其他单元格：  

1. 选择包含火花线的单元格。  
1. 从**设计**选项卡的**火花线**部分选择**编辑数据**。  
1. 选择**编辑组位置和数据**。  
1. 指定数据范围和位置。  
1. 点击**确定**。  

Aspose.Cells提供`SparklineCollection.add(dataRange, row, column)`方法，用于指定切片群组的数据范围和位置。以下示例加载源Excel文件（如上图所示），访问第一个切片群组，并添加数据范围和位置，最后将结果写入磁盘中的Excel文件，也如上图所示。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

