---
title: Farbe des Glüheffekts eines Shapes mit Node.js via C++ lesen
linktitle: Lesen Sie die Farbe des Leuchteffekts der Form.
type: docs
weight: 330
url: /de/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Erfahren Sie, wie Sie die Farbe des Glüheffekts eines Shapes mit Aspose.Cells for Node.js via C++ lesen. 
---

## Mögliche Anwendungsszenarien

Wenn Sie die Farbe des Glüheffekts eines Shapes lesen möchten, verwenden Sie bitte die Eigenschaft [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--). Sie hilft Ihnen, die verschiedenen Eigenschaften im Zusammenhang mit der Farbe des Glüheffekts des Shapes zu finden.

## Farbe des Glow-Effekts der Form lesen

Bitte sehen Sie sich den folgenden Beispielcode und seine [Quelldatei](22774108.xlsx) sowie die Konsolenausgabe zu Ihrer Referenz an. Der folgende Screenshot zeigt den Leuchteffekt der Form in der Quelldatei, wenn sie in Microsoft Excel angezeigt wird.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Node.js-Code zum Lesen der Farbe des Glüheffekts eines Shapes

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

## Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der bereitgestellten [Quelldatei](22774108.xlsx) ausgeführt wird.

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
