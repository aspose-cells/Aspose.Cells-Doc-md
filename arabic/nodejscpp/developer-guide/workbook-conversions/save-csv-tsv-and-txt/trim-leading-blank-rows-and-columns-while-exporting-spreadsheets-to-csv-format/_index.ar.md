---
title: قص الصفوف والأعمدة الفارغة الأولية عند تصدير جداول البيانات إلى تنسيق CSV باستخدام Node.js عبر C++
linktitle: تقليم الصفوف والأعمدة الفارغة الرائدة أثناء تصدير الجداول الجدولية إلى تنسيق CSV
type: docs
weight: 100
url: /ar/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: اعرف كيفية قص الصفوف والأعمدة الفارغة الأولية عند تصدير جداول البيانات إلى تنسيق CSV باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف Excel أو CSV الخاص بك على أعمدة أو صفوف فارغة رئيسية. على سبيل المثال، تأمل هذا السطر

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

افتراضيًا، لا تقوم Aspose.Cells for Node.js via C++ بإهمال الأعمدة والصفوف الفارغة الأولية عند الحفظ، ولكن إذا كنت تريد إزالتها كما يفعل Microsoft Excel، فإن Aspose.Cells يوفر خاصية [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--). يرجى ضبطها على **true** ثم سيتم إهمال جميع الصفوف والأعمدة الفارغة الأولية عند الحفظ.

{{% alert color="primary" %}}

قبل إصدار Aspose.Cells for Node.js via C++ 20.4، كانت القيمة الافتراضية لـ [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) هي **false**. منذ إصدار 20.4، القيمة الافتراضية لـ [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) هي **true**.

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

يحمّل الرمز النموذجي التالي ملف Excel [المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين في البداية. يحفظ الملف بصيغة CSV بدون تغييرات ثم يضبط خاصية [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) على **true** ويحفظه مرة أخرى. تظهر الصورة ملف Excel المصدر، وملف CSV الناتج بدون القص، وملف CSV الناتج مع القص.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
