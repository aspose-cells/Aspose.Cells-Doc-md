---
title: الوصول إلى صندوق النص باستخدام الاسم مع Node.js عبر C++
linktitle: الوصول إلى مربع النص من خلال الاسم
type: docs
weight: 230
url: /ar/nodejs-cpp/access-the-text-box-by-the-name/
description: تعلم كيفية الوصول إلى صندوق نص بالاسم من المجموعة في Aspose.Cells for Node.js via C++. 
---

## الوصول إلى مربع النص بالاسم

في السابق، كان يتم الوصول إلى صناديق النص بالترتيب من مجموعة [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--)، لكن الآن يمكنك الوصول أيضًا إلى صندوق النص بالاسم من هذه المجموعة. هذه طريقة مريحة وسريعة للوصول إلى صندوق النص إذا كنت تعرف اسمه بالفعل.

الكود المصدري التالي يقوم أولاً بإنشاء مربع نص وتعيين نص واسم له. ثم في الأسطر التالية، نقوم بالوصول إلى نفس مربع النص باستخدام اسمه وطباعة نصه.

### رمز Node.js للوصول إلى صندوق النص بالاسم

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
