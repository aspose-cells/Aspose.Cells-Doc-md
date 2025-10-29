---
title: Добавьте Word Art Text с встроенными стилями с помощью Node.js через C++
linktitle: Добавление словесного искусства текста с встроенными стилями
type: docs
weight: 270
url: /ru/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Узнайте, как добавить Word Art Text с встроенными стилями, используя Aspose.Cells for Node.js via C++. Создавайте визуально привлекательный текст в Excel с помощью встроенных стилей.
---

## **Возможные сценарии использования**
Вы можете добавить Word Art Text с встроенными стилями, используя Aspose.Cells for Node.js via C++. Пожалуйста, используйте метод [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) для этой цели.

## **Добавление словесного искусства текста с встроенными стилями**
В следующем образце кода добавляются тексты Word Art с различными встроенными стилями. Пожалуйста, проверьте [выходной файл Excel](5115470.xlsx), созданный с помощью этого кода. Так выглядит [выходной файл Excel](5115470.xlsx) в Microsoft Excel.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add Word Art Text with Built-in Styles
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
