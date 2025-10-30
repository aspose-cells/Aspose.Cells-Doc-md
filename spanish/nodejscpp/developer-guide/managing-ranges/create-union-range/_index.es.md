---  
title: Crear un rango de unión con Node.js via C++  
linktitle: Crear rango de unión  
type: docs  
weight: 360  
url: /es/nodejs-cpp/create-union-range/  
description: Aprende cómo crear un rango de unión usando Aspose.Cells for Node.js via C++.  
keywords: Crear rango de unión en Node.js vía C++, Rango de unión Aspose.Cells en Node.js, WorksheetCollection crear rango de unión en Node.js  
---  

## **Crear rango de unión**  
Aspose.Cells ofrece la capacidad de crear un Rango de Unión usando el método [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). El método [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) acepta dos parámetros, la dirección para crear el rango de unión y el índice de la hoja de trabajo. El método devuelve un objeto [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange).  

El siguiente fragmento de código demuestra cómo crear un Rango de Unión usando el método [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). El archivo de salida generado por el código se adjunta como referencia.  

- [Archivo de salida](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
