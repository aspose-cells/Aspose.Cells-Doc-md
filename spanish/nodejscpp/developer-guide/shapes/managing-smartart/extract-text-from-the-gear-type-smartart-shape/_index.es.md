---
title: Extraer texto de la forma de arte inteligente de tipo Engranaje con Node.js vía C++
linktitle: Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje
type: docs
weight: 500
url: /es/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aprende cómo extraer texto de la forma de arte inteligente de tipo Engranaje usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**

Aspose.Cells puede extraer texto de la forma de arte inteligente de tipo Engranaje. Para ello, primero debes convertir la forma de arte inteligente en una forma de grupo usando el método [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Luego obtén la matriz de todas las formas individuales que componen el grupo usando el método [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--). Finalmente, puedes iterar todas las formas individuales una por una en un ciclo y extraer su texto usando la propiedad [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).

## **Extraer Texto de la Forma de Arte SmartArt de Tipo de Engranaje**

El siguiente código de muestra carga el [archivo Excel de muestra](67338483.xlsx) que contiene una Forma de Arte SmartArt de Tipo de Engranaje. Luego extrae el texto de sus formas individuales como se discutió anteriormente. Consulte la salida de la consola del código a continuación para una referencia.

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **Salida de la consola**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
