---  
title: 使用Node.js via C++剪切和粘贴范围  
linktitle: 剪切和粘贴范围  
type: docs  
weight: 130  
url: /zh/nodejs-cpp/cut-and-paste-cells/  
description: 学习如何在Aspose.Cells for Node.js via C++中剪切和粘贴工作表中的单元格。  
---  

## **剪切和粘贴单元格**  

Aspose.Cells for Node.js via C++ 通过使用 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/) 集合的 [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) 方法，提供在工作表中剪切和粘贴单元格的功能。[**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) 接受以下参数。  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/)：要剪切的单元格范围。  
- 行索引：要插入单元格的行索引。  
- 列索引：要插入单元格的列索引。  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/)：列的移动方向。  

以下示例展示了如何在工作表中剪切和粘贴单元格。  

## **示例代码**  

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
