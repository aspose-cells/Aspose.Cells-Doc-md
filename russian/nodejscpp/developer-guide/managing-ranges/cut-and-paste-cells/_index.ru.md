---  
title: Вырезать и вставить диапазон с помощью Node.js через C++  
linktitle: Вырезать и вставить диапазон  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/cut-and-paste-cells/  
description: Узнайте, как вырезать и вставить ячейки внутри листа, используя Aspose.Cells for Node.js via C++.  
---  

## **Вырезать и вставить ячейки**  

Aspose.Cells for Node.js via C++ предоставляет возможность вырезать и вставлять ячейки внутри листа с помощью метода [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/). Параметры метода [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-).  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): Диапазон ячеек для вырезания.  
- Индекс строки: Индекс строки для вставки ячеек.  
- Индекс столбца: Индекс столбца для вставки ячеек.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): Направление сдвига столбцов.  

В следующем примере показано, как вырезать и вставить ячейки в пределах рабочего листа.  

## **Образец кода**  

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
