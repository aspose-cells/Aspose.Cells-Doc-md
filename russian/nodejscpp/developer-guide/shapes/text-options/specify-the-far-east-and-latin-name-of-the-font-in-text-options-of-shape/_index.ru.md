---  
title: Укажите Восточноазиатское и латинское название шрифта в настройках текста фигуры с помощью Node.js через C++  
linktitle: Укажите Дальний Восток и латинское название шрифта в опциях текста формы  
type: docs  
weight: 1600  
url: /ru/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: Узнайте, как указывать Восточноазиатские и латинские названия шрифтов в настройках текста фигур, используя Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Иногда необходимо отображать текст на Восточноазиатском языке, например, японский, китайский, тайский и др. Aspose.Cells for Node.js via C++ предоставляет свойство [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--), которое можно использовать для указания названия шрифта Восточноазиатского языка. Кроме того, вы можете также указать латинское название шрифта, используя свойство [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--).  

## **Укажите Дальний Восток и латинское название шрифта в опциях текста формы**  

Следующий пример создает текстовое поле и добавляет внутри него японский текст. Затем указывается латинское и Восточноазиатское название шрифтов для текста и сохраняется рабочая книга как [выходной файл Excel](67338274.xlsx). Следующий скриншот показывает латинские и Восточноазиатские названия шрифтов выходного текстового поля в Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add textbox inside the worksheet.
const idx = ws.getTextBoxes().add(5, 5, 50, 200);
const tb = ws.getTextBoxes().get(idx);

// Set the text of the textbox.
tb.setText("こんにちは世界");

// Specify the Far East and Latin name of the font.
tb.getTextOptions().setLatinName("Comic Sans MS");
tb.getTextOptions().setFarEastName("KaiTi");

// Save the output Excel file.
wb.save("outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
