---
title: Convertir el Art Smart a Forma Group con Node.js vía C++
linktitle: Convertir el Arte Inteligente en Forma de Grupo
type: docs
weight: 200
url: /es/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Escenarios de uso posibles**

Puedes convertir la Forma Smart Art en una Forma de Grupo usando el método [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Esto te permitirá manejar la forma de arte inteligente como una forma de grupo. En consecuencia, tendrás acceso a las partes o formas individuales del grupo.

## **Convertir el Arte Inteligente en Forma de Grupo**

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](55541793.xlsx) que contiene una forma de arte inteligente como se muestra en esta captura de pantalla. Luego convierte la forma de arte inteligente en forma de grupo y muestra la propiedad Shape.isGroup. Por favor, consulte la salida de la consola del código de ejemplo a continuación.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **Salida de la consola**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
