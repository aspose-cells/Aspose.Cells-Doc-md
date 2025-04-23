---  
title: 使用 Node.js 通过 C++ 指定要在 Excel 文件中存储的有效数字  
linktitle: 指定要存储在Excel文件中的有效数字  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 指定要在Excel文件中存储的有效数字。  
---  

## **可能的使用场景**  

默认情况下，Aspose.Cells for Node.js via C++在Excel文件中存储双精度值的17个有效数字，而不同于MS-Excel仅存储15个有效数字。你可以使用 [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) 属性将Aspose.Cells的默认行为从17个有效数字改为15个。  

## **指定要在Excel文件中存储的有效数字**  

以下示例代码强制Aspose.Cells在存储双精度值时使用15个有效数字。请查看[输出Excel文件](22774105.xlsx)。将扩展名改为.zip，解压后即可看到文件中只存储了15个有效数字。下图说明了 [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) 属性对输出Excel文件的影响。  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

