---  
title: حدد الاسم الشرقي الأقصى واللاتيني للخط في خيارات النص للشكل باستخدام Node.js عبر C++  
linktitle: تحديد اسم الشرق الأقصى واللاتيني للخط في خيارات النص للشكل  
type: docs  
weight: 1600  
url: /ar/nodejs-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/  
description: تعلم كيف تحدد أسماء خط الشرق الأقصى واللاتيني في خيارات النص للأشكال باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

أحيانًا ترغب في عرض النص بلغة شرق آسيوية مثل اليابانية، الصينية، التايلاندية، وغيرها. يوفر Aspose.Cells for Node.js via C++ خاصية [**TextOptions.getFarEastName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getFarEastName--) التي يمكن استخدامها لتحديد اسم الخط للغة الشرق الأقصى. بالإضافة إلى ذلك، يمكنك أيضًا تحديد اسم الخط اللاتيني باستخدام خاصية [**TextOptions.getLatinName()**](https://reference.aspose.com/cells/nodejs-cpp/textoptions/#getLatinName--).  

## **تحديد اسم الشرق الأقصى واللاتيني للخط في خيارات النص للشكل**  

يخلق الكود التالي مربع نص ويضيف فيه نصًا يابانيًا. ثم يحدد أسماء الخط اللاتيني وشرق آسيا للنص ويحفظ ملف العمل كملف إكسل الناتج. يظهر لقطة الشاشة أسماء الخطوط في مربع النص الناتج في إكسل.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **الكود المثالي**  

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

