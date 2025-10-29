---  
title: 使用 Node.js 和 C++ 锁定 WordArt 水印  
linktitle: 锁定WordArt水印  
type: docs  
weight: 170  
url: /zh/nodejs-cpp/locking-wordart-watermark/  
description: 学习如何用 Aspose.Cells for Node.js via C++ 锁定 WordArt 水印  
---  

{{% alert color="primary" %}}  

Aspose.Cells API 允许将 WordArt 水印作为对象添加到工作表上，您可以移动和定位它。还可以锁定 Watermark 对象，防止编辑、移动和选择。本文介绍使用 [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) 方法锁定水印的某些方面。

{{% /alert %}}  

Aspose.Cells API 允许锁定水印的某些方面，从而限制或完全阻止用户交互。以下代码示例演示如何用 Aspose.Cells for Node.js via C++ 从头创建电子表格以锁定水印的选择、移动、编辑和调整大小。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Lock Shape Aspects
wordart.setIsLocked(true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Selection, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.ShapeType, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Move, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Resize, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Text, true);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();

// Set the color
wordArtFormat.setOneColorGradient(AsposeCells.Color.Red, 0.2, AsposeCells.GradientStyleType.Horizontal, 2);

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
wordart.setHasLine(false);

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
