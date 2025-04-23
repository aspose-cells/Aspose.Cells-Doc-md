---  
title: Följande kodexempel visar hur man skapar en Union Range med hjälp av [WorksheetCollection.createUnionRange](https //reference.aspose.com/cells/nodejs cpp/worksheetcollection/#createUnionRange string number ). Utdatan för filen som genereras av koden är bifogad för referens.  
linktitle: Klipp och Klistra Range  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/cut-and-paste-cells/  
description: Lär dig hur man klipper och klistrar celler inom ett kalkylblad med Aspose.Cells for Node.js via C++.  
---  

## **Klipp och klistra celler**  

Lär dig hur man klipper ut och klistrar in celler inom ett kalkblad med Aspose.Cells for Node.js via C++.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): Området med celler som ska klippas.  
- Radindex: Index för raden att infoga celler.  
- Kolumnindex: Index för kolumnen att infoga celler.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): Kolumnernas förflyttningsriktning.  

Följande exempel visar hur du klipper och klistrar celler inom en arbetsbok.  

## **Exempelkod**  

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

