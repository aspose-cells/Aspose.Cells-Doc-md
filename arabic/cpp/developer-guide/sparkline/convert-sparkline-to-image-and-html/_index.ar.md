---
title: تحويل سباركلاين إلى صورة وHTML في Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: تعلّم كيفية عرض سباركلاين Aspose.Cells كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بالسباركلاين إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, C++, سباركلاين, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, عرض سباركلاين, تحويل سباركلاين إلى صورة, تصدير سباركلاين إلى HTML
type: docs
weight: 120
url: /ar/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
السباركلاين (Sparklines) هي رسوم بيانية مصغّرة تُوضع داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل سباركلاين كصورة مستقلة (لتضمينها في خلية أخرى أو تقرير خارجي) وأيضًا تصدير ورقة العمل الغنية بالسباركلاين بالكامل إلى HTML لتوزيعها عبر المتصفح. خاصية `Cell.EmbeddedImage` المستخدمة في هذه المقالة متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **المقدمة**

تُعدّ السباركلاين طريقة مدمجة لتصور الاتجاهات مباشرة داخل ورقة العمل. في حين يراها مستخدمو Excel في مكانها، تتطلب العديد من سيناريوهات العمل الفعلية أن تغادر السباركلاين الخلية — على سبيل المثال، ليتم تضمينها في خلية مختلفة كصورة ثابتة، أو إرفاقها برسالة بريد إلكتروني آلية، أو عرضها كجزء من تقرير HTML منشور على الويب.

يدعم Aspose.Cells كلتا العمليتين. تُخرج طريقة `Sparkline.ToImage` سباركلاين فرديًا إلى تيار (stream)، ويمكن تعيين البايتات الناتجة إلى `Cell.EmbeddedImage` بحيث تُخزَّن الصورة داخل خلية واحدة من المصنف. وبشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بالكامل — بكل سباركلاين — إلى ملف HTML مستقل بذاته. تتناول هذه المقالة سير العملين من البداية إلى النهاية.

## **سير العمل 1 — عرض السباركلاين كصور وتضمينها في الخلايا**

في سير العمل هذا، ستقوم ببناء ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وإرفاق ثلاث مجموعات سباركلاين مختلفة (Line وColumn وStacked/Win-Loss) بهذا النطاق، وعرض كل مجموعة كصورة PNG، وكتابة بايتات PNG هذه في خلايا مجاورة كصور مضمّنة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كلٍّ من السباركلاين الحيّة ونظيراتها من الصور المعروضة.

### **تعليمات خطوة بخطوة**

1. حدد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع لأول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم رقمية عينة (مثل المبيعات اليومية أو قراءات درجة الحرارة).
4. أضف ثلاث كائنات `SparklineGroup` إلى ورقة العمل باستدعاء `worksheet.SparklineGroups.Add(...)`:
   - مجموعة من النوع `SparklineType.Line` مُثبّتة عند `F1`، مع نطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.Column` مُثبّتة عند `G1`، مع نطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.Stacked` (win/loss) مُثبّتة عند `H1`، مع نطاق البيانات `A1:E1`.
5. أنشئ نسخة من `ImageOrPrintOptions` وعيّن خاصية `ImageType` إلى `ImageType.Png` بحيث يتم عرض كل سباركلاين كصورة PNG شفافة.
6. لكل مجموعة من المجموعات الثلاث، اعرض سباركلاين الفردي الخاص بها باستخدام `group.Sparklines[0].ToImage(memoryStream, imageOptions)`، ثم حوّل `MemoryStream` إلى `Vector<uint8_t>`، وعيّن المصفوفة إلى `worksheet.Cells["F2"].EmbeddedImage` و`worksheet.Cells["G2"].EmbeddedImage` و`worksheet.Cells["H2"].EmbeddedImage` على التوالي.
7. احفظ المصنف باسم `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

ينتج عن الكود أعلاه مصنفًا تتكرر فيه كل تمثيل بصري لسباركلاين في شكلين: السباركلاين الحي الأصلي المُثبّت عند الصف 1، وصورة PNG ثابتة مضمّنة مباشرة في خلية مجاورة عند الصف 2. ولأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها بالبريد الإلكتروني أو أرشفتها دون أن تنقطع مراجع الصور المضمّنة. اعرض كل مجموعة سباركلاين كصورة PNG، وحول `MemoryStream` إلى `Vector<uint8_t>`، وعيّن المصفوفة إلى خاصية `EmbeddedImage` في الخلية المستهدفة — فعملية الإسناد هي التي تجعل الصورة جزءًا من المحتويات المخزّنة للخلية.

{{% alert color="primary" %}}
نظرًا لأن كل مجموعة سباركلاين مُثبّتة في خلية واحدة، يمكنك الوصول إليها عبر المفهرس `group.Sparklines[0]` بدلاً من التعداد باستخدام `foreach`. هذا يُبقي كود العرض قصيرًا ويتطابق مع النمط الشائع "سباركلاين واحد لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `Cell.EmbeddedImage` إصدار Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة عمل السباركلاين إلى HTML**

بمجرد أن يحتوي المصنف على سباركلاين حيّة (وبشكل اختياري نظيراتها من الصور المضمّنة)، يمكن نشر ورقة العمل بالكامل على الويب بحفظها بتنسيق HTML. يكشف صنف `HtmlSaveOptions` عن الإعدادات التي تحتاج إليها للتحكم في هذا التصدير؛ في سير العمل هذا ستُعيد استخدام ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 وتحوله إلى مستند HTML نظيف ذي صفحة واحدة.

### **تعليمات خطوة بخطوة**

1. تأكد من توفر ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 على القرص في دليل العمل لديك.
2. حمّل هذا الملف في نسخة جديدة من `Workbook`.
3. أنشئ نسخة من `HtmlSaveOptions` وعيّن خاصية `ExportActiveWorksheetOnly` إلى `true` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بالكامل.
4. استدعِ `workbook.Save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

يأخذ الكود أعلاه المصنف الغني بالسباركلاين من سير العمل 1 ويحوّله إلى ملف HTML محمول. يتم الحفاظ على السباركلاين كصور SVG أو PNG مضمّنة داخل HTML المُنشأ، وذلك حسب وضع التصدير، بحيث يمكن للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال ضبط `ExportActiveWorksheetOnly` على `true`، تتجنب نشر أوراق مخفية أو بيانات مساعدة عن طريق الخطأ — حيث يتم تصدير ورقة العمل المرئية حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
يقدم صنف `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `ExportHiddenWorksheet` و`ExportImagesAsBase64` و`Encoding`. اضبطها حسب الحاجة بما يتناسب مع هدف النشر لديك.
{{% /alert %}}

## **ملخص واجهة برمجة التطبيقات**

يعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.

- يُستخدم `SparklineGroup` ووصول المجموعة `worksheet.SparklineGroups` للإعلان عن النوع (Line أو Column أو Stacked) ونطاق البيانات والخلية المُثبّتة لكل مجموعة سباركلاين. في هذه المقالة، كل مجموعة مُثبّتة في خلية واحدة، لذا يتم الوصول إلى المجموعة عبر `worksheet.SparklineGroups[i]`.
- يُرجع `Sparkline` والمفهرس `group.Sparklines[0]` السباركلاين الفردي داخل المجموعة. ولأن كل مجموعة في المثال تحتوي على سباركلاين واحد بالضبط، فلا حاجة إلى حلقة `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة للسباركلاين في `Stream` مُمرَّر. تُرجع الطريقة `void`؛ وتقرأ البايتات من التيار بعد الاستدعاء.
- `Cell.EmbeddedImage` هي خاصية من نوع `Vector<uint8_t>` تخزّن صورة داخل خلية واحدة. وهي متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث** وتُعدّ الطريقة الموصى بها لإرجاع سباركلاين تم عرضه بواسطة `ToImage` إلى نفس المصنف.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (من نوع `bool`) يقصر تصدير HTML على ورقة العمل النشطة. وهو أحد أكثر الخصائص استخدامًا في `HtmlSaveOptions` عند إنشاء تقارير ذات صفحة واحدة.
- توجد `ImageOrPrintOptions.ImageType` في مساحة الأسماء `Aspose.Cells.Drawing` وتختار تنسيق الصورة (مثل `ImageType.Png`) المستخدم عند العرض باستخدام `ToImage` وعند طباعة أوراق العمل إلى صور.

## **مقالات ذات صلة**

- [السباركلاين في Aspose.Cells for C++](/cells/ar/cpp/sparkline/)
- [إدراج صورة في خلية](/cells/ar/cpp/inserting-an-image-into-a-cell/)
- [عرض مصفوفة خلية واحدة من SmartMarker | Aspose.Cells for C++](/cells/ar/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}