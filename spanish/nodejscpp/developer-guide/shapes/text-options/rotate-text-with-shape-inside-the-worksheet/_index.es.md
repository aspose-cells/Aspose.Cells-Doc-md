---
title: Rotar texto con forma dentro de la hoja de cálculo usando Node.js vía C++
linktitle: Rotar Texto con Forma dentro de la Hoja de Cálculo
type: docs
weight: 1300
url: /es/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aprende cómo rotar texto con forma dentro de una hoja de cálculo de Excel usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Puedes agregar texto dentro de cualquier forma usando Microsoft Excel. Si agregas una forma usando Microsoft Excel 2003 muy antiguo, el texto no rotará con la forma. Pero si agregas una forma usando versiones más modernas de Microsoft Excel, por ejemplo, 2007, 2010, 2013 o 2016, etc., el texto rotará con la forma. Puedes controlar si el texto debería rotar con la forma o no usando la propiedad [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--). El valor predeterminado de esta es **true**, lo que significa que el texto rotará con la forma, pero si lo estableces como **false**, entonces el texto no rotará con la forma.

## **Rotar texto con forma dentro de la hoja de cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716896.xlsx) que tiene una forma de triángulo y su texto rota con la forma. Si abres el archivo de Excel de muestra en Microsoft Excel y giras la forma del triángulo, el texto también rotará con ella. Luego, el código establece la propiedad [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) como **false** y lo guarda como [archivo de Excel de salida](64716897.xlsx). Si ahora abres el archivo de Excel de salida en Microsoft Excel y giras la forma del triángulo, el texto no rotará con ella. Por favor, mira la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra para referencia.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
