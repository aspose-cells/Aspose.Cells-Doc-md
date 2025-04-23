---
title: عرض الإضافات Office أثناء تحويل إكسيل إلى PDF عبر Node.js باستخدام C++
linktitle: عرض إضافات Office أثناء تحويل Excel إلى صيغة PDF
type: docs
weight: 100
url: /ar/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **سيناريوهات الاستخدام المحتملة**

في السابق، لم تتمكن Aspose.Cells من عرض إضافات Office عند حفظ ملف إكسيل بصيغة PDF. الآن، تعرض Aspose.Cells الإضافة بشكل صحيح. لا يلزمك استخدام أي طريقة أو خاصية خاصة لعرض الإضافات Office في PDF الناتج. فقط احفظ ملف إكسيل بصيغة PDF، وسيتم عرض الإضافة.

## **تقديم الإضافات المكتبية أثناء تحويل Excel إلى PDF**

الكود التالي يحفظ [ملف Excel النموذجي](60489769.xlsx) الذي يحتوي على إضافات Office، يرجى الاطلاع على [ملف PDF الناتج مع الإصدار السابق 17.11](60489770.pdf) و[ملف PDF الناتج مع الإصدار الأحدث 17.12 وما بعد](60489771.pdf). الملف السابق يكون PDF الناتج فارغًا، لكن النسخة الأحدث تظهر الإضافة.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
