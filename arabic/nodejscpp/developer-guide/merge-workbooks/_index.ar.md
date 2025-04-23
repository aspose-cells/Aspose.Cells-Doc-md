---
title: دمج عدة كتب عمل في كتاب واحد مع Node.js عبر C++
linktitle: مدمج السجل
type: docs
weight: 66
url: /ar/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: تعلم كيف تدمج عدة كتب عمل في كتاب واحد باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

 في بعض الأحيان، تحتاج إلى دمج كتب عمل تحتوي على محتوى متنوع مثل الصور والرسوم البيانية والبيانات في كتاب واحد. يدعم Aspose.Cells for Node.js via C++ هذه الميزة. يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم ودمج كتب العمل ببضع أسطر بسيطة من الكود باستخدام Aspose.Cells.

{{% /alert %}}

## **دمج أسجل العمل مع الصور والرسوم البيانية**

 يدمج رمز المثال كتابي عمل في كتاب واحد باستخدام Aspose.Cells for Node.js via C++. يقوم الرمز بتحميل كتب العمل المصدرية، واستخدام طريقة [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) لدمجها، وحفظ ملف الكتاب الناتج.

### **السجلات المصدر**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **مصنفات الإخراج**

- [combined.xlsx](5473095.xlsx)

### **لقطات الشاشة**

أدناه تظهر لقطات من المصنفات الأصلية والمخرّجة.

{{% alert color="primary" %}}

يمكنك استخدام أي مصنف أصلي. هذه الصور مجرد لأغراض توضيحية.

{{% /alert %}}

**الورقة العمل الأولى لمصنف الرسوم البيانية - مكدسة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**الورقة العمل الثانية لمصنف الرسوم البيانية - خطية** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**الورقة العمل الأولى لمصنف الصور - صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**كل الورقات الثلاثة في مصنف الدمج - مكدسة، خطية، صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **مواضيع متقدمة**
- [دمج الورقات المتعددة في ورقة عمل واحدة](/cells/ar/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [دمج الملفات](/cells/ar/nodejs-cpp/merge-files/)

