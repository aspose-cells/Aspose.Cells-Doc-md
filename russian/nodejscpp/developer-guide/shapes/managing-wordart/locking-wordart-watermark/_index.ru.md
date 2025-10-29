---  
title: Блокировка водяного знака WordArt с помощью Node.js через C++  
linktitle: Блокировка водяного знака WordArt  
type: docs  
weight: 170  
url: /ru/nodejs-cpp/locking-wordart-watermark/  
description: Узнайте, как заблокировать водяные знаки WordArt с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

API Aspose.Cells позволяют добавлять водяные знаки WordArt на лист так, что WordArt становится объектом, который можно перемещать и позиционировать на листе. Также возможно заблокировать объект WordArt для взаимодействия, такого как редактирование, перемещение и выбор. Эта статья объясняет использование метода [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) для блокировки некоторых аспектов водяного знака.

{{% /alert %}}  

API Aspose.Cells позволяет заблокировать определенные аспекты водяного знака, чтобы ограничить или полностью запретить взаимодействие пользователя. Следующий код демонстрирует использование Aspose.Cells for Node.js via C++ для блокировки выбора, перемещения, редактирования и изменения размера водяного знака, создавая таблицу с нуля.  

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
