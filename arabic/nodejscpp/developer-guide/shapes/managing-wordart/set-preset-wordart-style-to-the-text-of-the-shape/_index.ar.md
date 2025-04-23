---
title: تعيين نمط WordArt مخصص لنص الشكل باستخدام Node.js عبر C++
linktitle: تعيين نمط نص فني محدد مسبقًا لنص الشكل
type: docs
weight: 280
url: /ar/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: تعلم كيفية تعيين نمط WordArt مخصص إلى نص شكل باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك تعيين نمط WordArt مخصص إلى نص الشكل باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) أو [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) للغرض ذاته.

## **تعيين نمط WordArt المحدد مسبقًا لنص الشكل**
الكود النموذجي التالي ينشئ مربع نص مع نص معين ثم يضبط نمط WordArt المسبق للنص باستخدام طريقة [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). هكذا يبدو ملف Excel المخرجاتي ([ملف الإكسل](5115445.xlsx)) في Microsoft Excel.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a textbox with some text
const textbox = worksheet.getShapes().addTextBox(0, 0, 0, 0, 100, 700);
textbox.setText("Aspose File Format APIs");
textbox.getFont().setSize(44);

// Sets preset WordArt style to the text of the shape.
const fntSetting = textbox.getRichFormattings()[0];
fntSetting.setWordArtStyle(AsposeCells.PresetWordArtStyle.WordArtStyle3);

// Save the workbook in xlsx format
workbook.save(outputDir + "outputSetPresetWordArtStyle.xlsx");
```
