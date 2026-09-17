---
title: تحويل Sparkline إلى صورة وHTML في Aspose.Cells for C++
linktitle: تحويل Sparkline إلى صورة وHTML في Aspose.Cells for C++
description: تعرّف على كيفية عرض Sparklines لـ Aspose.Cells كصور مستقلة لتضمينها في الخلايا، وتصدير أوراق العمل الغنية بـ Sparkline إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, عرض سباركلاين, تحويل سباركلاين إلى صورة, تصدير سباركلاين إلى HTML
type: docs
weight: 120
url: /ar/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
تُعد Sparklines رسومًا بيانيةً مصغّرةً تُوضع داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل Sparkline كصورة مستقلة (لتضمينها في خلية أخرى أو تقرير خارجي) كما يتيح تصدير ورقة العمل بأكملها الغنية بـ Sparkline إلى HTML للتوزيع عبر المتصفح. خاصية `Cell.EmbeddedImage` المستخدمة في هذه المقالة متاحة بدءًا من **Aspose.Cells 26.5 والإصدارات الأحدث**.

## **المقدمة**
تُعد Sparklines طريقةً مدمجةً لتصور الاتجاهات مباشرةً داخل ورقة العمل. وبينما يراها مستخدمو Excel في مكانها، تتطلب سيناريوهات واقعية عديدة أن تغادر Sparkline الخلية — على سبيل المثال، لتُدمج في خلية مختلفة كصورة ثابتة، أو تُرفق في رسالة بريد إلكتروني آلية، أو تُعرض كجزء من تقرير HTML منشور على الويب.
يدعم Aspose.Cells كلتا العمليتين. إذ تُحوّل الطريقة `Sparkline.ToImage` Sparkline فرديةً إلى مصفوفة بايتات من النوع `Vector<uint8_t>`، ويمكن تعيين البايتات الناتجة إلى `Cell.EmbeddedImage` بحيث تُخزَّن الصورة داخل خلية واحدة من المصنف. وبشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك الـ Sparklines — إلى ملف HTML مستقل بذاته. تستعرض هذه المقالة سيرَي العمل هذين من البداية إلى النهاية.

## **سير العمل 1 — عرض Sparklines كصور وتضمينها في الخلايا**
في سير العمل هذا، ستُنشئ ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وتُرفق ثلاث مجموعات Sparkline مختلفة (Line وColumn وStacked/Win-Loss) بهذا النطاق، وتُقدّم كل مجموعة كصورة PNG، وتكتب بايتات PNG تلك في الخلايا المجاورة كصور مُدمجة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كلٍّ من الـ Sparklines الحيّة ونظيراتها من الصور المُقدّمة.

### **التعليمات خطوة بخطوة**
1. حدّد دليل عمل وتأكّد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع لأول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم عددية نموذجية (مثل المبيعات اليومية أو قراءات درجة الحرارة).
4. أضف ثلاثة كائنات `SparklineGroup` إلى ورقة العمل باستدعاء `worksheet.SparklineGroups.Add(...)`:
   - مجموعة `SparklineType.Line` مُرساة في `F1`، ونطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.Column` مُرساة في `G1`، ونطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.Stacked` (win/loss) مُرساة في `H1`، ونطاق البيانات `A1:E1`.
5. أنشئ مثيلًا من `ImageOrPrintOptions` وعيّن خاصية `ImageType` إلى `ImageType.Png` بحيث تُقدّم كل Sparkline كصورة PNG شفافة.
6. لكل مجموعة من المجموعات الثلاث، اعرض الـ Sparkline الفردية باستخدام `group.Sparklines[0].ToImage(imageOptions)` — إذ يُعيد الاستدعاء بايتات الصورة مباشرةً من النوع `Vector<uint8_t>` — وعيّن المصفوفة إلى `worksheet.GetCells().Get("F2"].EmbeddedImage` و`worksheet.GetCells().Get("G2"].EmbeddedImage` و`worksheet.GetCells().Get("H2"].EmbeddedImage` على التوالي.
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

يُنتج الكود أعلاه مصنفًا تتكرر فيه كل تمثيل مرئي لـ Sparkline بشكلين: Sparkline حيّة أصلية مُرساة في الصف 1، وصورة PNG ثابتة مُدمجة مباشرةً في خلية مجاورة في الصف 2. ولأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعةً واحدةً مستقلةً بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المُدمجة. اعرض كل مجموعة Sparkline كصورة PNG — إذ تُعيد `Sparkline.ToImage(ImageOrPrintOptions)` بايتات الصورة مباشرةً من النوع `Vector<uint8_t>` — وعيّن المصفوفة إلى خاصية `EmbeddedImage` للخلية المستهدفة — فالتعيين هو ما يجعل الصورة جزءًا من المحتويات المخزَّنة للخلية.

{{% alert color="primary" %}}
نظرًا لأن كل مجموعة Sparkline مُرساة في خلية واحدة، يمكنك الوصول إليها عبر المُفهرس `group.Sparklines[0]` بدلاً من العدّ بـ `foreach`. يحافظ ذلك على قصر كود العرض ويطابق النمط المعتاد وهو "Sparkline واحدة لكل خلية مُرساة". يتطلب تخزين بايتات الصورة عبر `Cell.EmbeddedImage` الإصدار Aspose.Cells 26.5 أو أحدث.

## **سير العمل 2 — تصدير ورقة عمل Sparkline إلى HTML**
بمجرد أن يحتوي المصنف على Sparklines حيّة (وبشكل اختياري، نظائرها من الصور المُدمجة)، يمكن نشر ورقة العمل بأكملها على الويب بحفظها بصيغة HTML. يكشف صنف `HtmlSaveOptions` عن الأدوات التي تحتاجها للتحكم في هذا التصدير؛ في سير العمل هذا، ستُعيد استخدام ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 وتحوله إلى مستند HTML نظيف بصفحة واحدة.

### **التعليمات خطوة بخطوة**
1. تأكّد من توفر ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 على القرص في دليل العمل لديك.
2. حمّل هذا الملف في مثيل `Workbook` جديد.
3. أنشئ مثيلًا من `HtmlSaveOptions` وعيّن خاصية `ExportActiveWorksheetOnly` إلى `true` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
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

يأخذ الكود أعلاه المصنف الغني بـ Sparklines من سير العمل 1 ويحوله إلى ملف HTML قابل للنقل. تُحفظ Sparklines كصور SVG مضمّنة أو PNG داخل HTML المُولّد، بحسب وضع التصدير، بحيث يمكن للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. وبتعيين `ExportActiveWorksheetOnly` إلى `true`، تتجنب النشر العَرَضي للأوراق المخفية أو البيانات المساعدة — إذ تُصدَّر فقط ورقة العمل المرئية حاليًا للمستخدم.

{{% alert color="primary" %}}
يقدّم صنف `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `ExportHiddenWorksheet` و`ExportImagesAsBase64` و`Encoding`. اضبطها حسب الحاجة وفقًا لهدف النشر لديك.

## **ملخص واجهات برمجة التطبيقات**
تعتمد سيرَا العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.
- يُستخدم `SparklineGroup` ووصول المجموعة `worksheet.SparklineGroups` للإعلان عن النوع (Line أو Column أو Stacked) ونطاق البيانات والخلية المُرساة لكل مجموعة Sparkline. في هذه المقالة، تُرسى كل مجموعة في خلية واحدة، لذا يُمكن الوصول إلى المجموعة عبر `worksheet.SparklineGroups[i]`.
- يُعيد `Sparkline` والمُفهرس `group.Sparklines[0]` الـ Sparkline الفردية داخل المجموعة. ولأن كل مجموعة في المثال تحتوي على Sparkline واحدة بالضبط، فلا حاجة إلى حلقة `foreach`.
- تُعد `Sparkline.ToImage(ImageOrPrintOptions)` طريقة العرض التي تُعيد صورة الـ Sparkline مباشرةً كمصفوفة بايتات من النوع `Vector<uint8_t>`.
- تقصر `HtmlSaveOptions.ExportActiveWorksheetOnly` (من النوع `bool`) تصدير HTML على ورقة العمل النشطة. وهي واحدة من أكثر الخصائص شيوعًا في `HtmlSaveOptions` عند إنشاء تقارير بصفحة واحدة.
- تعيش `ImageOrPrintOptions.ImageType` في فضاء الأسماء `Aspose.Cells.Drawing` وتختار صيغة الصورة (مثلًا `ImageType.Png`) المُستخدمة عند العرض بـ `ToImage` وعند طباعة أوراق العمل إلى صور.

## **مقالات ذات صلة**
- [Sparklines في Aspose.Cells for C++](/cells/ar/cpp/sparkline/)
- [إدراج صورة داخل خلية](/cells/ar/cpp/inserting-an-image-into-a-cell/)
- [عرض مصفوفة الخلية الواحدة في SmartMarker | Aspose.Cells for C++](/cells/ar/cpp/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}