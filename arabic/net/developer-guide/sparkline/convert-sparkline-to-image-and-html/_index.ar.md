---
title: تحويل سباركلاين إلى صورة وHTML في Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: تعلّم كيفية عرض سباركلاين Aspose.Cells كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بالسباركلاين إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, عرض سباركلاين, تحويل سباركلاين إلى صورة, تصدير سباركلاين إلى HTML
type: docs
weight: 120
url: /ar/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
السباركلاين هي رسوم بيانية صغيرة الحجم تُوضع داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل سباركلاين كصورة مستقلة (لتضمينها في خلية أخرى أو تقرير خارجي) وأيضًا تصدير ورقة العمل الغنية بالسباركلاين بأكملها إلى HTML للتوزيع عبر المتصفح. خاصية `Cell.EmbeddedImage` المستخدمة في هذه المقالة متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **المقدمة**

تُعد السباركلاين طريقة مدمجة لتصور الاتجاهات مباشرة داخل ورقة العمل. بينما يراها مستخدمو Excel في مكانها، تتطلب العديد من السيناريوهات العملية أن يغادر السباركلاين الخلية — على سبيل المثال، ليتم تضمينه في خلية مختلفة كصورة ثابتة، أو إرفاقه ببريد إلكتروني آلي، أو عرضه كجزء من تقرير HTML منشور على الويب.

يدعم Aspose.Cells كلتا العمليتين. تقوم طريقة `Sparkline.ToImage` بعرض سباركلاين فردي إلى تدفق بيانات (stream)، ويمكن تعيين البايتات الناتجة إلى `Cell.EmbeddedImage` بحيث يتم تخزين الصورة داخل خلية واحدة من المصنف. بشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك السباركلاين — إلى ملف HTML مستقل. تتناول هذه المقالة سير العمل هذين من البداية إلى النهاية.

## **سير العمل 1 — عرض السباركلاين كصور وتضمينها في الخلايا**

في سير العمل هذا، ستقوم ببناء ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وإرفاق ثلاث مجموعات مختلفة من السباركلاين (خط، عمود، ومكدس/فوز-خسارة) بهذا النطاق، وعرض كل مجموعة كملف PNG، وكتابة بايتات PNG هذه في خلايا مجاورة كصور مدمجة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كل من السباركلاين الحية ونظيراتها من الصور المعروضة.

### **تعليمات خطوة بخطوة**

1. حدد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع لأول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم رقمية نموذجية (على سبيل المثال، المبيعات اليومية أو قراءات درجة الحرارة).
4. أضف ثلاث كائنات `SparklineGroup` إلى ورقة العمل عن طريق استدعاء `worksheet.SparklineGroups.Add(...)`:
   - مجموعة من النوع `SparklineType.Line` مثبتة في `F1`، مع نطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.Column` مثبتة في `G1`، مع نطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.Stacked` (فوز/خسارة) مثبتة في `H1`، مع نطاق البيانات `A1:E1`.
5. أنشئ مثيلًا من `ImageOrPrintOptions` وعيّن `ImageType` الخاص به إلى `ImageType.Png` بحيث يتم عرض كل سباركلاين كملف PNG شفاف.
6. لكل مجموعة من المجموعات الثلاث، اعرض السباركلاين الوحيد باستخدام `group.Sparklines[0].ToImage(memoryStream, imageOptions)`، ثم حوّل `MemoryStream` إلى `byte[]`، وعيّن المصفوفة إلى `worksheet.Cells["F2"].EmbeddedImage`، و`worksheet.Cells["G2"].EmbeddedImage`، و`worksheet.Cells["H2"].EmbeddedImage` على التوالي.
7. احفظ المصنف باسم `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// تعبئة بيانات العينة في الخلايا A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// إضافة مجموعة خط مؤشر أداء مثبتة عند F1 (العمود 5، الصف 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// إضافة مجموعة عمود مؤشر أداء مثبتة عند G1 (العمود 6، الصف 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// إضافة مجموعة فوز/خسارة (مكدسة) لمؤشر أداء مثبتة عند H1 (العمود 7، الصف 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// تكوين خيارات الصورة لإخراج PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// تحويل خط مؤشر الأداء إلى صورة وتضمينها في الخلية F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// تحويل عمود مؤشر الأداء إلى صورة وتضمينها في الخلية G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// تحويل مؤشر أداء الفوز/الخسارة إلى صورة وتضمينها في الخلية H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// حفظ المصنف على القرص
workbook.Save("output_with_sparklines.xlsx");
```

ينتج عن الكود أعلاه مصنفًا يتم فيه تكرار كل تمثيل مرئي لسباركلاين في شكلين: السباركلاين الحي الأصلي المثبت في الصف 1، وصورة PNG ثابتة مدمجة مباشرة في خلية مجاورة في الصف 2. نظرًا لأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المدمجة. اعرض كل مجموعة سباركلاين كملف PNG، ثم حوّل `MemoryStream` إلى `byte[]`، وعيّن المصفوفة إلى خاصية `EmbeddedImage` للخلية المستهدفة — التعيين هو ما يجعل الصورة جزءًا من المحتويات المخزنة للخلية.

{{% alert color="primary" %}}
نظرًا لأن كل مجموعة سباركلاين مثبتة في خلية واحدة، يمكنك الوصول إليها من خلال المفهرس `group.Sparklines[0]` بدلاً من التعداد باستخدام `foreach`. هذا يحافظ على قصر كود العرض ويتطابق مع النمط المعتاد "سباركلاين واحد لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `Cell.EmbeddedImage` الإصدار Aspose.Cells 26.5 أو الأحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة عمل السباركلاين إلى HTML**

بمجرد أن يحتوي المصنف على سباركلاين حية (وبشكل اختياري نظائر صور مدمجة)، يمكن نشر ورقة العمل بأكملها على الويب عن طريق حفظها كملف HTML. يكشف فئة `HtmlSaveOptions` عن الخيارات التي تحتاجها للتحكم في هذا التصدير؛ في سير العمل هذا، ستعيد استخدام ملف `output_with_sparklines.xlsx` الذي تم إنتاجه في سير العمل 1 وتحوّله إلى مستند HTML نظيف أحادي الصفحة.

### **تعليمات خطوة بخطوة**

1. تأكد من أن ملف `output_with_sparklines.xlsx` الذي تم إنتاجه في سير العمل 1 متاح على القرص في دليل العمل الخاص بك.
2. حمّل هذا الملف في مثيل `Workbook` جديد.
3. أنشئ مثيلًا من `HtmlSaveOptions` وعيّن خاصية `ExportActiveWorksheetOnly` الخاصة به إلى `true` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
4. استدعِ `workbook.Save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

يأخذ الكود أعلاه المصنف الغني بالسباركلاين من سير العمل 1 ويحوّله إلى ملف HTML محمول. يتم الحفاظ على السباركلاين كرسومات SVG أو PNG مدمجة داخل HTML المُنشأ، اعتمادًا على وضع التصدير، بحيث يمكن للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال تعيين `ExportActiveWorksheetOnly` إلى `true`، تتجنب نشر الأوراق المخفية أو البيانات المساعدة عن طريق الخطأ — يتم تصدير ورقة العمل المرئية حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
توفر فئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `ExportHiddenWorksheet`، و`ExportImagesAsBase64`، و`Encoding`. اضبط هذه حسب الحاجة لهدف النشر الخاص بك.
{{% /alert %}}

## **ملخص واجهة برمجة التطبيقات**

تعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells API التي تعمل معًا.

- يتم استخدام `SparklineGroup` ووصول المجموعة `worksheet.SparklineGroups` للإعلان عن النوع (Line، Column، Stacked)، ونطاق البيانات، والخلية المُثبتة لكل مجموعة سباركلاين. في هذه المقالة، كل مجموعة مثبتة في خلية واحدة، لذا يتم الوصول إلى المجموعة من خلال `worksheet.SparklineGroups[i]`.
- يُرجع `Sparkline` والمفهرس `group.Sparklines[0]` السباركلاين الفردي داخل المجموعة. نظرًا لأن كل مجموعة في المثال تحتوي على سباركلاين واحد بالضبط، فلا حاجة إلى حلقة `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة للسباركلاين في `Stream` مُقدّم. تُرجع الطريقة `void`؛ وتقرأ البايتات من التدفق بعد الاستدعاء.
- `Cell.EmbeddedImage` هي خاصية من نوع `byte[]` تخزن صورة داخل خلية واحدة. وهي متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث** وهي الطريقة الموصى بها لإعادة السباركلاين المعروض بواسطة `ToImage` إلى نفس المصنف.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (من نوع `bool`) يقيد تصدير HTML بورقة العمل النشطة. وهي واحدة من الخصائص الأكثر استخدامًا على `HtmlSaveOptions` عند إنشاء تقارير أحادية الصفحة.
- `ImageOrPrintOptions.ImageType` توجد في مساحة الأسماء `Aspose.Cells.Drawing` وتختار تنسيق الصورة (على سبيل المثال، `ImageType.Png`) المستخدم عند العرض باستخدام `ToImage` وعند طباعة أوراق العمل إلى صور.

## **مقالات ذات صلة**

- [السباركلاين في Aspose.Cells for .NET](/cells/ar/net/sparkline/)
- [إدراج صورة في خلية](/cells/ar/net/inserting-an-image-into-a-cell/)
- [عرض مصفوفة خلية واحدة من SmartMarker | Aspose.Cells .NET](/cells/ar/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}