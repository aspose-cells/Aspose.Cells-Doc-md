---
title: Enviar forma al frente o al fondo dentro de la hoja con Node.js a través de C++
linktitle: Enviar la forma al frente o atrás dentro de la hoja de cálculo
type: docs
weight: 3400
url: /es/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aprende cómo enviar una forma al frente o al fondo en una hoja usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Cuando hay varias formas en la misma ubicación, su visibilidad la determina la posición en el orden Z. Aspose.Cells proporciona el método [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-), que cambia la posición Z de la forma. Para enviar una forma al fondo, usa un número negativo como -1, -2, -3, etc., y para traer una forma al frente, usa un número positivo como 1, 2, 3, etc.

## **Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo**

El código de muestra a continuación explica el uso del método [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-). Por favor, vea el [archivo Excel de ejemplo](50528330.xlsx) usado en el código y el [archivo Excel de salida](50528331.xlsx) generado. La captura muestra el efecto del código en el archivo de ejemplo al ejecutarse.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
