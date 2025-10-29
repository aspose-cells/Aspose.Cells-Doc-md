---
title: البحث عما إذا كانت ورقة العمل عبارة عن ورقة حوار باستخدام Node.js عبر C++
linktitle: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 90
url: /ar/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: تقدم هذه المقالة تعليمات ورمزًا نماذجياً لتحديد برمجياً ما إذا كانت ورقة عمل إكسل هي ورقة حوار باستخدام Aspose.Cells for Node.js via C++.
keywords: البحث عن نوع حوار ورقة العمل في إكسل باستخدام Node.js عبر C++، ورقة حوار في ورقة العمل Node.js عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

ورقة الحوار هي تنسيق قديم من الورقة تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة بواسطة إصدار أقدم من مايكروسوفت إكسل، مثل 2003، كما هو موضح في لقطة الشاشة هذه. يمكن أيضًا إدراجها باستخدام VBA في الإصدارات الأحدث، مثل مايكروسوفت إكسل 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة ما إذا كانت الورقة ورقة حوار أو نوع آخر من الأوراق باستخدام خاصية [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) المقدمة من Aspose.Cells for Node.js via C++. إذا عادت قيمة تعداد [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype)، فهذا يدل على أنك تتعامل مع ورقة حوار.

## **العثور على ورقة العمل هل هي ورقة حوار**

الرمز النموذجي التالي يحمل [ملف إكسل العيني](64716820.xlsx) الذي يحتوي على ورقة حوار. يفحص الخاصية [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--)، يقارنها مع [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype)، ثم يطبع الرسالة. يرجى الاطلاع على مخرجات وحدة التحكم للرمز النموذجي أدناه للمساعدة.

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **مخرجات الوحدة**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
