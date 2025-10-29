---
title: Установить предустановленный стиль WordArt для текста формы с помощью Node.js через C++
linktitle: Установить предварительный стиль WordArt для текста формы
type: docs
weight: 280
url: /ru/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Узнайте, как установить предустановленный стиль WordArt для текста формы, используя Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**
Вы можете установить предустановленный стиль WordArt для текста формы, используя Aspose.Cells for Node.js via C++. Пожалуйста, используйте методы [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) или [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) для этой цели.

## **Установить предварительный стиль WordArt для текста формы**
Следующий пример кода создает текстовое поле с текстом и затем устанавливает предустановленный стиль WordArt для его текста с помощью метода [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). Вот как выглядит созданный файл Excel в Microsoft Excel.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
