---
title: Insertar una imagen basada en referencia a celda con Node.js mediante C++
linktitle: Insertar una imagen basada en una referencia de celda
type: docs
weight: 150
url: /es/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Aprenda cómo insertar una imagen en una hoja de cálculo basada en una referencia de celda usando Aspose.Cells for Node.js via C++. Mostrar datos de la celda en una imagen.
---

{{% alert color="primary" %}}
A veces tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la Barra de Fórmulas. Aspose.Cells soporta esta característica (Microsoft Excel 2010).
{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells for Node.js via C++ soporta mostrar el contenido de una celda de hoja de cálculo en una forma de imagen. Puede enlazar la imagen a la celda que contiene los datos que desea mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que realice en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico. Agregue una imagen a la hoja de cálculo llamando al método [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Especifique el rango de celdas usando el atributo [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) del objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).

### Ejemplo de código

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
