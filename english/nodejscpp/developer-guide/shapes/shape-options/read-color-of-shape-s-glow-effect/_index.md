---
title: Read Color of Shape's Glow Effect with Node.js via C++
linktitle: Read Color of Shape's Glow Effect
type: docs
weight: 330
url: /nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Learn how to read the color of a shape's glow effect using Aspose.Cells for Node.js via C++. 
---

## Possible Usage Scenarios

If you want to read the color of the glow effect of any shape, then please use the [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--) property. It will help you find the various properties relating to the color of the glow effect of the shape.

## Read Color of the Glow Effect of Shape

Please see the following sample code and its [source excel file](22774108.xlsx) and the console output for your reference. The following screenshot shows the glow effect of the shape inside the source excel file when viewed in Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Node.js code to read color of shape's glow effect

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

## Console Output

Here is the console output of the above sample code when executed with the provided [source excel file](22774108.xlsx).

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
