---  
title: قص ولصق النطاق باستخدام Node.js عبر C++  
linktitle: قص ولصق المجموعة  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/cut-and-paste-cells/  
description: تعلم كيفية قص ولصق الخلايا داخل ورقة العمل باستخدام Aspose.Cells for Node.js via C++.  
---  

## **قص ولصق الخلايا**  

 توفر لك Aspose.Cells for Node.js via C++ القدرة على قص ولصق الخلايا داخل ورقة العمل باستخدام طريقة [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/). يقبل [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) المعلمات التالية.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): مجموعة الخلايا التي سيتم قصها.  
- فهرس الصف: فهرس الصف لإدراج الخلايا.  
- فهرس العمود: فهرس العمود لإدراج الخلايا.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): اتجاه التحريك للأعمدة.  

المثال التالي يوضح كيفية قص ولصق الخلايا داخل ورقة العمل.  

## **الكود المثالي**  

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

