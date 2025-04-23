---
title: Trabajando con el formato 3D de Shape o Chart con Node.js mediante C++
linktitle: Trabajar con el Formato ThreeD de la Forma o Gráfico
type: docs
weight: 250
url: /es/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Escenarios de uso posibles**
Aspose.Cells for Node.js via C++ proporciona la propiedad [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) junto con la clase [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) para trabajar con el formato 3D de forma o gráfico. La clase [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) contiene diferentes propiedades que se pueden ajustar para lograr diferentes resultados según los requisitos de la aplicación.

## **Trabajar con el Formato ThreeD de la Forma o Gráfico**
El siguiente código de ejemplo carga el [archivo excel fuente](5115419.xlsx) y accede a la primera forma en la primera hoja de trabajo y establece las subpropiedades de [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) y luego guarda el libro en [archivo excel de salida](5115410.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
