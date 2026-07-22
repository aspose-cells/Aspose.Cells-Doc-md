---
title: تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Node.js via Java
linktitle: Convert Sparkline to Image and HTML
description: تعرّف على كيفية عرض خطوط Aspose.Cells الصغيرة كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بخطوط Sparkline إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, عرض sparkline, تحويل sparkline إلى صورة, تصدير sparkline إلى HTML
type: docs
weight: 120
url: /ar/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
خطوط Sparkline هي رسوم بيانية مصغّرة موضوعة داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل خط sparkline كصورة مستقلة (لتضمينها في خلية أخرى أو في تقرير خارجي) وكذلك تصدير ورقة العمل بأكملها الغنية بخطوط Sparkline إلى HTML للتوزيع عبر المتصفح. الخاصية `Cell.EmbeddedImage` المستخدمة في هذه المقالة متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **المقدمة**

تمثل خطوط Sparkline طريقة مدمجة لتصور الاتجاهات مباشرة داخل ورقة العمل. بينما يراها مستخدمو Excel في مكانها، تتطلب العديد من السيناريوهات الواقعية أن يغادر خط sparkline الخلية — على سبيل المثال، ليتم تضمينه في خلية مختلفة كصورة ثابتة، أو إرفاقه برسالة بريد إلكتروني مؤتمتة، أو عرضه كجزء من تقرير HTML منشور على الويب.

يدعم Aspose.Cells كلتا هاتين العمليتين. تُخرج الطريقة `Sparkline.toImage` خط sparkline فرديًا إلى تدفق، ويمكن تعيين البايتات الناتجة إلى `Cell.EmbeddedImage` بحيث تُخزَّن الصورة داخل خلية واحدة من المصنف. وبشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك خطوط Sparkline — إلى ملف HTML مستقل بذاته. تتناول هذه المقالة سير العمل كليهما من البداية إلى النهاية.

## **سير العمل 1 — عرض خطوط Sparkline كصور وتضمينها في الخلايا**

في سير العمل هذا، ستُنشئ ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وتُرفق ثلاث مجموعات مختلفة من خطوط Sparkline (خطية، وأعمدة، ومكدسة/فوز-خسارة) بهذا النطاق، وتعرض كل مجموعة كملف PNG، وتكتب بايتات PNG هذه في الخلايا المجاورة كصور مُضمَّنة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على خطوط Sparkline الحية ونظيراتها من الصور المعروضة.

### **إرشادات خطوة بخطوة**

1. حدّد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم رقمية نموذجية (على سبيل المثال، مبيعات يومية أو قراءات درجة الحرارة).
4. أضف ثلاثة كائنات `SparklineGroup` إلى ورقة العمل عن طريق استدعاء `worksheet.sparklineGroups.add(...)`:
   - مجموعة `SparklineType.Line` مُثبَّتة عند `F1`، مع نطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.Column` مُثبَّتة عند `G1`، مع نطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.Stacked` (فوز/خسارة) مُثبَّتة عند `H1`، مع نطاق البيانات `A1:E1`.
5. أنشئ مثيلًا من `ImageOrPrintOptions` واضبط خاصية `ImageType` فيه على `ImageType.Png` بحيث يُعرض كل خط sparkline كملف PNG شفاف.
6. لكل مجموعة من المجموعات الثلاث، اعرض خط sparkline الفردي الخاص بها باستخدام `group.sparklines[0].toImage(outputStream, imageOptions)`، وحَوِّل الـ `ByteArrayOutputStream` إلى `byte[]`، وعيّن المصفوفة إلى `worksheet.cells.get("F2").setEmbeddedImage(...)`، و`worksheet.cells.get("G2").setEmbeddedImage(...)`، و`worksheet.cells.get("H2").setEmbeddedImage(...)` على التوالي.
7. احفظ المصنف باسم `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// تعبئة بيانات العينة في الخلايا A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// إضافة مجموعة شرارة خطية مثبتة عند F1 (العمود 5، الصف 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// إضافة مجموعة شرارة عمودية مثبتة عند G1 (العمود 6، الصف 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// إضافة مجموعة شرارة فوز/خسارة (مكدسة) مثبتة عند H1 (العمود 7، الصف 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// تكوين خيارات الصورة لإخراج PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// تحويل الشرارة الخطية إلى صورة وتضمينها في الخلية F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// تحويل الشرارة العمودية إلى صورة وتضمينها في الخلية G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// تحويل شرارة الفوز/الخسارة إلى صورة وتضمينها في الخلية H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// حفظ المصنف على القرص
workbook.save("output_with_sparklines.xlsx");
```

يُنتج الكود أعلاه مصنفًا يتم فيه تكرار كل تمثيل مرئي لخط sparkline في شكلين: خط sparkline الحي الأصلي المُثبَّت عند الصف 1، وصورة PNG ثابتة مُضمَّنة مباشرة في خلية مجاورة في الصف 2. نظرًا لأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المُضمَّنة. اعرض كل مجموعة sparkline كملف PNG، وحَوِّل الـ `ByteArrayOutputStream` إلى `byte[]`، وعيّن المصفوفة إلى خاصية `setEmbeddedImage` للخلية المستهدفة — هذا التعيين هو ما يجعل الصورة جزءًا من المحتويات المخزَّنة للخلية.

{{% alert color="primary" %}}
نظرًا لأن كل مجموعة sparkline مُثبَّتة في خلية واحدة، يمكنك الوصول إليها من خلال المفهرس `group.sparklines[0]` بدلاً من التعداد باستخدام `forEach`. يُبقي هذا كود العرض قصيرًا ويتطابق مع النمط النموذجي "خط sparkline واحد لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `Cell.EmbeddedImage` وجود Aspose.Cells 26.5 أو إصدارًا أحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة عمل Sparkline إلى HTML**

بمجرد أن يحتوي المصنف على خطوط sparkline حية (وصور مُضمَّنة اختيارية)، يمكن نشر ورقة العمل بأكملها على الويب عن طريق حفظها بتنسيق HTML. تُعرَض فئة `HtmlSaveOptions` أدوات التحكم التي تحتاجها للتحكم في هذا التصدير؛ في سير العمل هذا، ستُعيد استخدام ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 وتحَوِّله إلى مستند HTML نظيف من صفحة واحدة.

### **إرشادات خطوة بخطوة**

1. تأكد من توفر ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 على القرص في دليل العمل لديك.
2. حمِّل هذا الملف في مثيل `Workbook` جديد.
3. أنشئ مثيلًا من `HtmlSaveOptions` واضبط خاصية `ExportActiveWorksheetOnly` فيه على `true` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
4. استدعِ `workbook.save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

يأخذ الكود أعلاه المصنف الغني بخطوط sparkline من سير العمل 1 ويُحوِّله إلى ملف HTML قابل للنقل. تُحفظ خطوط Sparkline كرسومات SVG أو PNG مُضمَّنة داخل HTML المُولَّد، وفقًا لوضع التصدير، بحيث يمكن للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال ضبط `ExportActiveWorksheetOnly` على `true`، تتجنب نشر الأوراق المخفية أو البيانات المساعدة عن طريق الخطأ — حيث يتم تصدير ورقة العمل المعروضة حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
تُقدِّم فئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `ExportHiddenWorksheet`، و`ExportImagesAsBase64`، و`Encoding`. اضبط هذه حسب الحاجة وفقًا لهدف النشر لديك.
{{% /alert %}}

## **ملخص واجهة برمجة التطبيقات (API)**

يعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.

- تُستخدم `SparklineGroup` وواصف المجموعة `worksheet.sparklineGroups` للإعلان عن النوع (Line، Column، Stacked)، ونطاق البيانات، والخلية المُثبَّتة لكل مجموعة sparkline. في هذه المقالة، تُثبَّت كل مجموعة في خلية واحدة، لذا يتم الوصول إلى المجموعة من خلال `worksheet.sparklineGroups[i]`.
- يُرجع `Sparkline` والمفهرس `group.sparklines[0]` خط sparkline الفردي داخل المجموعة. نظرًا لأن كل مجموعة في المثال تحتوي على خط sparkline واحد بالضبط، فلا حاجة إلى حلقة `forEach`.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة لخط sparkline في `OutputStream` المُقدَّم. تُرجع الطريقة `void`؛ وتقرأ البايتات من التدفق بعد الاستدعاء.
- `Cell.EmbeddedImage` هي خاصية من نوع `byte[]` تُخزِّن صورة داخل خلية واحدة. وهي متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث**، وهي الطريقة الموصى بها لإرجاع خط sparkline تم عرضه بواسطة `toImage` إلى نفس المصنف.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (من نوع `boolean`) يقصر تصدير HTML على ورقة العمل النشطة. وهي واحدة من الخصائص الأكثر استخدامًا في `HtmlSaveOptions` عند إنشاء تقارير من صفحة واحدة.
- توجد `ImageOrPrintOptions.ImageType` في مساحة الأسماء `com.aspose.cells.drawing` وتختار تنسيق الصورة (على سبيل المثال، `ImageType.Png`) المستخدم عند العرض باستخدام `toImage` وعند طباعة أوراق العمل إلى صور.

## **مقالات ذات صلة**

- [Sparklines in Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/sparkline/)
- [Inserting an Image into a Cell](/cells/ar/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}