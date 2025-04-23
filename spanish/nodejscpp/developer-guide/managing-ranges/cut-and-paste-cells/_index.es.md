---  
title: Cortar y pegar rango con Node.js vía C++  
linktitle: Cortar y Pegar Rango  
type: docs  
weight: 130  
url: /es/nodejs-cpp/cut-and-paste-cells/  
description: Aprende cómo cortar y pegar celdas dentro de una hoja con Aspose.Cells for Node.js via C++.  
---  

## **Cortar y Pegar Celdas**  

Aspose.Cells for Node.js via C++ te permite cortar y pegar celdas dentro de una hoja usando el método [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/). El [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) acepta los siguientes parámetros.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): El rango de celdas que se van a cortar.  
- Índice de Fila: El índice de la fila para insertar celdas.  
- Índice de Columna: El índice de la columna para insertar celdas.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): La dirección de desplazamiento de las columnas.  

El siguiente ejemplo muestra cómo cortar y pegar celdas dentro de una hoja de cálculo.  

## **Código de muestra**  

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

