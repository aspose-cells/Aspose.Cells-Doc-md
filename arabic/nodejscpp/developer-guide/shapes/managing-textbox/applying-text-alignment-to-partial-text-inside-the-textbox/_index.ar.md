---
title: كيفية تطبيق/ضبط محاذاة النص داخل صندوق النص باستخدام Node.js عبر C++
linktitle: تطبيق / تعيين محاذاة النص لمربع النص
type: docs
weight: 20
url: /ar/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: كيفية تطبيق/ضبط محاذاة النص داخل صندوق النص في Aspose.Cells for Node.js via C++.
keywords: تطبيق/ضبط محاذاة النص داخل صندوق النص في ورقة العمل باستخدام Node.js عبر C++
---

يمكن لصناديق النص أن تعزز تعبيرية مستنداتنا ومخططاتنا، وتطبيق محاذاة مختلفة على أجزاء مختلفة من صندوق النص يمكن أن يساعد في تسليط الضوء على نقاط الاهتمام للقراء. لكن المحاذاة الافتراضية لصندوق النص لا تلبي جميع احتياجاتنا. لذلك، قد تحتاج إلى تعديل كل صندوق نص لتحقيق متطلباتك. إذا لم تمتلك الكثير من أدوات صناديق النص للتعديل، أنت محظوظ. وإذا كانت هناك العديد من صناديق النص للتعديل، أعتقد أنك ستواجه مشكلة. لا تقلق الآن، فإن [Aspose.Cells](https://products.aspose.com/cells/) يوفر واجهة برمجة تطبيقات لمساعدتك على القيام بذلك.

يطبق الكود النموذجي التالي تحديد محاذاة النص على مربع نص.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const shapes = workbook.getWorksheets().get(0).getShapes();

// add a TextBox
const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
shape.setText("This is a test.");

// set alignment
shape.setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
shape.setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Save the excel file.
workbook.save(path.join(dataDir, "result.xlsx"));
```

يمكنك أيضًا تغيير محاذاة النص داخل بعض النصوص بداخل شكل صندوق النص باستخدام نص HTML المناسب. يطبق الرمز المساعد التالي محاذاة النص على جزء من النص داخل صندوق النص.

[ملف المصدر](SampleTextboxExcel2016.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SampleTextboxExcel2016.xlsx");

// Initialize an object of the Workbook class to load the template file
const sourceWb = new AsposeCells.Workbook(sourceFilePath);

// Access the target textbox whose text is to be aligned
const sourceTextBox = sourceWb.getWorksheets().get(0).getShapes().get(0);

// Create an object of the target workbook
const destWb = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const _sheet = destWb.getWorksheets().get(0);

// Create new textbox
const _textBox = _sheet.getShapes().addShape(AsposeCells.MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

// Alternatively text box can be added using the following line as well
// const _textBox = _sheet.getShapes().addTextBox(1, 0, 1, 0, 200, 200);

// Use Html string from a template file textbox
_textBox.setHtmlText(sourceTextBox.getHtmlText());

// Save the workbook on disk
destWb.save("Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
