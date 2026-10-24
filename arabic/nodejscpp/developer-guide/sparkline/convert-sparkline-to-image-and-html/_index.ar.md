---
title: تحويل خط المؤشر إلى صورة وHTML في Aspose.Cells for Node.js via C++
linktitle: تحويل خط المؤشر إلى صورة وHTML في Aspose.Cells for Node.js via C++
description: تعلّم كيفية عرض خطوط المؤشر في Aspose.Cells كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بخطوط المؤشر إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via C++, خط المؤشر, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, عرض خط المؤشر, تحويل خط المؤشر إلى صورة, تصدير خط المؤشر إلى HTML
type: docs
weight: 120
url: /ar/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
خطوط المؤشر (Sparklines) هي رسوم بيانية مصغّرة تُوضع داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل خط مؤشر كصورة مستقلة (لتضمينها في خلية أخرى أو تقرير خارجي) وأيضًا تصدير ورقة العمل بأكملها الغنية بخطوط المؤشر إلى HTML للتوزيع عبر المتصفح. الخاصية `cell.embeddedImage` المستخدمة في هذه المقالة متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **Introduction**
تُعد خطوط المؤشر طريقة مدمجة لتصور الاتجاهات مباشرة داخل ورقة العمل. بينما يراها مستخدمو Excel في مكانها، تتطلب العديد من السيناريوهات الواقعية أن يغادر خط المؤشر الخلية — على سبيل المثال، ليتم تضمينه في خلية مختلفة كصورة ثابتة، أو إرفاقه ببريد إلكتروني تلقائي، أو عرضه كجزء من تقرير HTML منشور على الويب.
يدعم Aspose.Cells كلتا العمليتين. تقوم الطريقة `Sparkline.toImage` بعرض خط مؤشر فردي إلى تيار (stream)، ويمكن تعيين البايتات الناتجة إلى `cell.embeddedImage` بحيث تُخزَّن الصورة داخل خلية واحدة من المصنف. وبشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك خطوط المؤشر — إلى ملف HTML مستقل بذاته. تستعرض هذه المقالة سير العمل كليهما بشكل كامل.

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
في سير العمل هذا، ستقوم ببناء ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وإرفاق ثلاث مجموعات مختلفة من خطوط المؤشر (خطية، عمودية، ومكدسة/فوز-خسارة) بهذا النطاق، وعرض كل مجموعة كصورة PNG، وكتابة بايتات PNG هذه في الخلايا المجاورة كصور مضمنة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كل من خطوط المؤشر الحية ونظيراتها من الصور المعروضة.

### **Step-by-Step Instructions**
1. حدد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم رقمية نموذجية (على سبيل المثال، المبيعات اليومية أو قراءات درجة الحرارة).
4. أضف ثلاث كائنات من `SparklineGroup` إلى ورقة العمل عن طريق استدعاء `worksheet.sparklineGroups.add(...)`:
   - مجموعة من النوع `SparklineType.Line` مُثبَّتة عند `F1`، بنطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.Column` مُثبَّتة عند `G1`، بنطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.Stacked` (فوز/خسارة) مُثبَّتة عند `H1`، بنطاق البيانات `A1:E1`.
5. أنشئ مثيلًا من `ImageOrPrintOptions` واضبط `ImageType` الخاص به إلى `ImageType.Png` بحيث يتم عرض كل خط مؤشر كصورة PNG شفافة.
7. احفظ المصنف باسم `output_with_sparklines.xlsx`.

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Add a Line sparkline group anchored at F1 (column 5, row 0)
let lineArea = new AsposeCells.CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
// Add a Column sparkline group anchored at G1 (column 6, row 0)
let columnArea = new AsposeCells.CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
// Configure image options for PNG output
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);
// Convert the Line sparkline to image and embed it in cell F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));
// Convert the Column sparkline to image and embed it in cell G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));
// Convert the Win/Loss sparkline to image and embed it in cell H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));
// Save the workbook to disk
workbook.save("output_with_sparklines.xlsx");
```

ينتج عن الكود أعلاه مصنفًا تتكرر فيه كل تمثيل مرئي لخط المؤشر في شكلين: خط المؤشر الحي الأصلي المثبت عند الصف 1، وصورة PNG ثابتة مضمنة مباشرة في خلية مجاورة عند الصف 2. ولأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المضمنة. اعرض كل مجموعة خطوط مؤشر كصورة PNG، وحول التيار إلى `Buffer`، وعيّن المصفوفة إلى خاصية `embeddedImage` في الخلية المستهدفة — هذا التعيين هو ما يجعل الصورة جزءًا من المحتويات المخزنة للخلية.

{{% alert color="primary" %}}
نظرًا لأن كل مجموعة خطوط مؤشر مثبتة في خلية واحدة، يمكنك الوصول إليها من خلال المفهرس `group.sparklines[0]` بدلاً من التعداد باستخدام `forEach`. هذا يُبقي كود العرض قصيرًا ويتطابق مع النمط المعتاد "خط مؤشر واحد لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `cell.embeddedImage` إصدار Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
بمجرد أن يحتوي المصنف على خطوط مؤشر حية (وبشكل اختياري، نظائر الصور المضمنة)، يمكن نشر ورقة العمل بأكملها على الويب عن طريق حفظها بتنسيق HTML. يكشف الفئة `HtmlSaveOptions` عن المفاتيح التي تحتاجها للتحكم في هذا التصدير؛ في سير العمل هذا، ستعيد استخدام ملف `output_with_sparklines.xlsx` الناتج عن سير العمل 1 وتحوله إلى مستند HTML نظيف من صفحة واحدة.

### **Step-by-Step Instructions**
1. تأكد من توفر ملف `output_with_sparklines.xlsx` الناتج عن سير العمل 1 على القرص في دليل العمل لديك.
2. حمّل هذا الملف في مثيل `Workbook` جديد.
3. أنشئ مثيلًا من `HtmlSaveOptions` واضبط خاصية `exportActiveWorksheetOnly` على `true` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
4. استدعِ `workbook.save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

يأخذ الكود أعلاه المصنف الغني بخطوط المؤشر من سير العمل 1 ويحوله إلى ملف HTML محمول. يتم الحفاظ على خطوط المؤشر كصور SVG أو PNG داخلية داخل HTML المُنشأ، بناءً على وضع التصدير، بحيث يمكن للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال ضبط `exportActiveWorksheetOnly` على `true`، تتجنب نشر أوراق العمل المخفية أو البيانات المساعدة عن طريق الخطأ — حيث يتم تصدير ورقة العمل المرئية حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
يوفر الفئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `exportHiddenWorksheet`، و`exportImagesAsBase64`، و`encoding`. اضبط هذه حسب الحاجة لهدف النشر لديك.
{{% /alert %}}

## **API Summary**
يعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.
- تُستخدم `SparklineGroup` ووصول المجموعة `worksheet.sparklineGroups` للإعلان عن النوع (خطي، عمودي، مكدس)، ونطاق البيانات، والخلية المرساة لكل مجموعة خطوط مؤشر. في هذه المقالة، تكون كل مجموعة مثبتة في خلية واحدة، لذا يتم الوصول إلى المجموعة من خلال `worksheet.sparklineGroups[i]`.
- يُرجع `Sparkline` والمفهرس `group.sparklines[0]` خط المؤشر الفردي داخل المجموعة. نظرًا لأن كل مجموعة في المثال تحتوي على خط مؤشر واحد بالضبط، فلا حاجة إلى حلقة `forEach`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة لخط المؤشر في `Stream` مُمرَّر. تُرجع هذه الطريقة `void`؛ وتقرأ البايتات من التيار بعد الاستدعاء.
- `htmlSaveOptions.exportActiveWorksheetOnly` (من نوع `bool`) يقصر تصدير HTML على ورقة العمل النشطة. وهي واحدة من الخصائص الأكثر استخدامًا في `HtmlSaveOptions` عند إنشاء تقارير صفحة واحدة.
- توجد `imageOrPrintOptions.imageType` في مساحة الاسم `Aspose.Cells.Drawing` وتحدد تنسيق الصورة (على سبيل المثال، `ImageType.Png`) المستخدم عند العرض باستخدام `toImage` وعند طباعة أوراق العمل كصور.

## **Related Articles**
- [إدراج صورة في خلية](/cells/ar/nodejs-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="nodejs-cpp" >}}