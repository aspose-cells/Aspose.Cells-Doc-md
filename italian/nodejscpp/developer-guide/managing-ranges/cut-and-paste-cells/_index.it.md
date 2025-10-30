---  
title: Taglia e incolla intervallo con Node.js via C++  
linktitle: Taglia e Incolla Intervallo  
type: docs  
weight: 130  
url: /it/nodejs-cpp/cut-and-paste-cells/  
description: Impara come tagliare e incollare celle all interno di un foglio di lavoro usando Aspose.Cells for Node.js via C++.  
---  

## **Taglia e Incolla Celle**  

Aspose.Cells for Node.js via C++ ti consente di tagliare e incollare celle all'interno di un foglio di lavoro utilizzando il metodo [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) della collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/). Il [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) accetta i seguenti parametri.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): L'intervallo di celle da tagliare.  
- Indice riga: L'indice della riga in cui inserire le celle.  
- Indice colonna: L'indice della colonna in cui inserire le celle.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): La direzione di spostamento delle colonne.  

L'esempio seguente mostra come tagliare e incollare celle all'interno di un foglio di lavoro.  

## **Codice di Esempio**  

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
