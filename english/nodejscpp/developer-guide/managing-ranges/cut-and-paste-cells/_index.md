---  
title: Cut and Paste Range with Node.js via C++  
linktitle: Cut and Paste Range  
type: docs  
weight: 130  
url: /nodejs-cpp/cut-and-paste-cells/  
description: Learn how to cut and paste cells within a worksheet using Aspose.Cells for Node.js via C++.  
---  
  
## **Cut and Paste Cells**  
  
Aspose.Cells for Node.js via C++ provides you with the ability to cut and paste cells within a worksheet by using the [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/) collection. The [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) accepts the following parameters.  
  
- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): The range of cells to be cut.  
- Row Index: The index of the row to insert cells.  
- Column Index: The index of the column to insert cells.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): The shift direction of the columns.  
  
The following example shows how to cut and paste cells within a worksheet.  
  
## **Sample Code**  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 2).setValue(1);
worksheet.getCells().get(1, 2).setValue(2);
worksheet.getCells().get(2, 2).setValue(3);
worksheet.getCells().get(2, 3).setValue(4);
worksheet.getCells().createRange(0, 2, 3, 1).setName("NamedRange");

const cut = worksheet.getCells().createRange("C:C");
worksheet.getCells().insertCutCells(cut, 0, 1, AsposeCells.ShiftType.Right);
workbook.save(path.join(outDir, "CutAndPasteCells.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}