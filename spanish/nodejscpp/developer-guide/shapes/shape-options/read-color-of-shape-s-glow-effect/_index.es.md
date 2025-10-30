---
title: Leer color del efecto brillo de la forma con Node.js mediante C++
linktitle: Leer color del efecto de resplandor de la forma
type: docs
weight: 330
url: /es/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Aprende cómo leer el color del efecto brillo de una forma usando Aspose.Cells for Node.js via C++. 
---

## Posibles Escenarios de Uso

Si deseas leer el color del efecto brillo de alguna forma, usa la propiedad [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--). Esto te ayudará a encontrar las diversas propiedades relacionadas con el color del efecto brillo de la forma.

## Leer color del efecto de resplandor de la forma

Consulte el siguiente código de ejemplo y su [archivo de Excel fuente](22774108.xlsx) y la salida de la consola para su referencia. La siguiente captura de pantalla muestra el efecto de resplandor de la forma dentro del archivo de Excel fuente cuando se ve en Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Código Node.js para leer el color del efecto brillo de una forma

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Read the source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourceGlowEffectColor.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the shape
const shape = sheet.getShapes().get(0);

// Read the glow effect color and its various properties
const effect = shape.getGlow();
const color = effect.getColor();
console.log("Color: " + color.getColor());
console.log("ColorIndex: " + color.getColorIndex());
console.log("IsShapeColor: " + color.isShapeColor());
console.log("Transparency: " + color.getTransparency());
console.log("Type: " + color.getType());
```

## Salida de la consola

Esta es la salida de la consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel fuente](22774108.xlsx) proporcionado.

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
