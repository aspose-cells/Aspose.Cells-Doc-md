---
title: 使用 Node.js 和 C++ 读取形状发光效果的颜色
linktitle: 读取形状的发光效果的颜色
type: docs
weight: 330
url: /zh/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: 学习如何用 Aspose.Cells for Node.js via C++ 读取形状发光效果的颜色 
---

## 可能的使用场景

如果你想读取任何形状的发光效果颜色，请使用 [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--) 属性。它可以帮你查找与形状发光颜色相关的各种属性。

## 读取形状发光效果的颜色

请查看以下示例代码及其[源Excel文件](22774108.xlsx)和控制台输出，供您参考。以下屏幕截图显示了在Microsoft Excel中查看源Excel文件时形状的发光效果。

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## 使用 Node.js 读取形状发光效果颜色的代码示例

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

## 控制台输出

以下是在提供的[源Excel文件](22774108.xlsx)上执行上述示例代码时的控制台输出。

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
