---  
title: Mover rango de celdas en una hoja de cálculo con Node.js vía C++  
linktitle: Mover rango de celdas en una hoja de cálculo  
type: docs  
weight: 370  
url: /es/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Aprenda a mover un rango de celdas en una hoja de cálculo usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Este artículo muestra cómo mover un rango de celdas en una hoja de cálculo.  
{{% /alert %}}  

## **Mover rango de celdas en una hoja de cálculo**  
El código de ejemplo utiliza un archivo de plantilla para demostrar la tarea.  

**El archivo de entrada**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Por favor, vea el siguiente archivo generado con el rango A1:B5 movido a C1:D5.  

**El archivo de salida**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
