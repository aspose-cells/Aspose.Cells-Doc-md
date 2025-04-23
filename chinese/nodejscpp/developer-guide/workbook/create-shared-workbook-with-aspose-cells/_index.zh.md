---  
title: 创建共享工作簿，编号为 Aspose.Cells for Node.js via C++  
linktitle: 使用Aspose.Cells创建共享工作簿  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 创建共享工作簿。  
---  

## **可能的使用场景**  

Microsoft Excel 允许您共享工作簿，如下截图所示。当您共享工作簿时，多个用户可以在网络上编辑该工作簿。Aspose.Cells for Node.js via C++ 使您能够使用 [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) 属性创建共享工作簿。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **使用Aspose.Cells创建共享工作簿**  

以下示例代码通过将[**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--)属性设置为**true**，创建一个共享工作簿。当您在Microsoft Excel中打开[输出Excel文件](55541786.xlsx)时，您将看到**共享**与输出工作簿的名称，如截图所示。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **示例代码**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

