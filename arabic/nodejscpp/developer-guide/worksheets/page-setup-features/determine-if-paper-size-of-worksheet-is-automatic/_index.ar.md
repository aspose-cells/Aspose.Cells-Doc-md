---
title: تحديد إذا ما كانت حجم الورق لورقة العمل تلقائي باستخدام Node.js عبر C++
linktitle: تحديد ما إذا كان حجم الورق للورقة التفاعلي
type: docs
weight: 90
url: /ar/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: يشرح هذا المقال كيفية استخدام واجهة برمجة تطبيقات Node.js مع إضافات C++ لتحديد ما إذا كان حجم الورق لورقة عمل معين مضبوطًا على تلقائي برمجياً.
keywords: تحديد إذا كان حجم الورق لورقة العمل تلقائي Node.js عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

غالبًا ما يكون حجم الورق لورقة العمل تلقائيًا. عندما يكون تلقائيًا، غالبًا يكون مضبوطًا على *Letter*. أحيانًا يحدد المستخدم حجم الورق لورقة العمل حسب متطلباته. في هذه الحالة، فإن حجم الورق ليس تلقائيًا. يمكنك معرفة ما إذا كان حجم الورق لورقة العمل تلقائيًا أو لا باستخدام الخاصية [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--).

## **تحديد ما إذا كان حجم الورق للورقة تلقائي**

الشيفرة العينية المعطاة أدناه تحمل الملفات الإكسل التاليتين

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ثم ابحث عما إذا كان حجم الورق لأول ورقة فيهما تلقائيًا أم لا. في Microsoft Excel، يمكنك التحقق ما إذا كان حجم الورق تلقائيًا أو لا من خلال نافذة إعداد الصفحة كما هو موضح في هذه لقطة الشاشة.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **مخرجات الوحدة**

هذا هو إخراج وحدة التحكم للشيفرة العينية أعلاه عند تنفيذها مع ملفات Excel العينية المعطاة.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
