---
title: استخدام وظيفة FormulaText في Aspose.Cells for Node.js via C++
linktitle: استخدام وظيفة FormulaText في Aspose.Cells
description: تقدم هذه المقالة شرحًا عن كيفية استخدام وظيفة FormulaText في مكتبة Aspose.Cells لمعالجة الصيغ في مايكروسوفت إكسل. تعلم كيفية الحصول على نص الصيغة وتعيينه وحفظ ملفات إكسل المعدلة باستخدام Node.js عبر C++.
keywords: Aspose.Cells، إكسل، وظائف FormulaText Node.js عبر C++
type: docs
weight: 60
url: /ar/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

صيغة FormulaText هي وظيفة في إكسل 2013 وما بعدها. غير مدعومة في الإصدارات السابقة مثل إكسل 2010 أو 2007 وما إلى ذلك. كما يوحي الاسم، تطبع نص الصيغة الموجودة في خلية معينة. ستوضح لك هذه المقالة كيفية الاستفادة من هذه الوظيفة باستخدام Aspose.Cells for Node.js via C++.

{{% /alert %}} 

يعرض المثال التالي استخدام FormulaText مع الرقم Aspose.Cells for Node.js via C++. الكود يكتب أولا معادلة في الخلية A1 ثم يطبع نص المعادلة باستخدام FormulaText في الخلية A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
