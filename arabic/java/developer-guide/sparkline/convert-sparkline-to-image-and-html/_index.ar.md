---
title: تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Java
linktitle: Convert Sparkline to Image and HTML
description: تعلم كيفية عرض خطوط المؤشر من Aspose.Cells كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بخطوط المؤشر إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /ar/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
خطوط المؤشر (Sparklines) هي رسوم بيانية مصغرة تُوضع داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل خط مؤشر كصورة مستقلة (لتضمينها في خلية أخرى أو تقرير خارجي) وأيضًا تصدير ورقة العمل بأكملها الغنية بخطوط المؤشر إلى HTML للتوزيع عبر المتصفح. الخاصية `Cell.EmbeddedImage` المستخدمة في هذا المقال متوفرة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **المقدمة**

تُعد خطوط المؤشر طريقة مدمجة لتصور الاتجاهات مباشرة داخل ورقة العمل. بينما يراها مستخدمو Excel في مكانها، تتطلب العديد من السيناريوهات العملية أن يغادر خط المؤشر الخلية — على سبيل المثال، ليتم تضمينه في خلية مختلفة كصورة ثابتة، أو إرفاقه ببريد إلكتروني آلي، أو عرضه كجزء من تقرير HTML منشور على الويب.

يدعم Aspose.Cells كلتا العمليتين. تقوم طريقة `Sparkline.toImage` بعرض خط مؤشر فردي إلى تيار (stream)، ويمكن تعيين البايتات الناتجة إلى `Cell.EmbeddedImage` (عبر `setEmbeddedImage`) بحيث تُخزَّن الصورة داخل خلية واحدة من المصنف. بشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بالكامل — بما في ذلك خطوط المؤشر — إلى ملف HTML مستقل بذاته. يستعرض هذا المقال كلا سير العمل من البداية إلى النهاية.

## **سير العمل 1 — عرض خطوط المؤشر كصور وتضمينها في الخلايا**

في سير العمل هذا، ستقوم ببناء ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وإرفاق ثلاث مجموعات مختلفة من خطوط المؤشر (Line وColumn وStacked/Win-Loss) بهذا النطاق، وعرض كل مجموعة كصورة PNG، وكتابة بايتات PNG هذه في خلايا مجاورة كصور مدمجة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كل من خطوط المؤشر الحية ونظيراتها من الصور المعروضة.

### **إرشادات خطوة بخطوة**

1. حدد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم رقمية عينة (على سبيل المثال، مبيعات يومية أو قراءات درجة الحرارة).
4. أضف ثلاث كائنات من `SparklineGroup` إلى ورقة العمل عن طريق استدعاء `worksheet.getSparklineGroups().add(...)`:
   - مجموعة من النوع `SparklineType.LINE` مثبتة عند `F1`، مع نطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.COLUMN` مثبتة عند `G1`، مع نطاق البيانات `A1:E1`.
   - مجموعة من النوع `SparklineType.STACKED` (فوز/خسارة) مثبتة عند `H1`، مع نطاق البيانات `A1:E1`.
5. أنشئ مثيلاً من `ImageOrPrintOptions` واستدعِ `setImageType(ImageType.PNG)` بحيث يتم عرض كل خط مؤشر كصورة PNG شفافة.
6. لكل مجموعة من المجموعات الثلاث، اعرض خط المؤشر الفردي الخاص بها باستخدام `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`، ثم حوِّل `ByteArrayOutputStream` إلى `byte[]`، وعيِّن المصفوفة عبر `worksheet.getCells().get("F2").setEmbeddedImage(...)`، و`worksheet.getCells().get("G2").setEmbeddedImage(...)`، و`worksheet.getCells().get("H2").setEmbeddedImage(...)` على التوالي.
7. استدعِ `workbook.save("output_with_sparklines.xlsx")` لحفظ المصنف على القرص.

```java
import com.aspose.cells.*;
import java.io.*;

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// تعبئة بيانات عينة في الخلايا من A1 إلى E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// إضافة مجموعة سباركلاين خطية مثبتة في F1 (العمود 5، الصف 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// إضافة مجموعة سباركلاين عمودية مثبتة في G1 (العمود 6، الصف 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// إضافة مجموعة سباركلاين فوز/خسارة (مكدسة) مثبتة في H1 (العمود 7، الصف 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// تكوين خيارات الصورة للإخراج بصيغة PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// تحويل سباركلاين الخط إلى صورة وتضمينها في الخلية F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// تحويل سباركلاين العمود إلى صورة وتضمينها في الخلية G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// تحويل سباركلاين الفوز/الخسارة إلى صورة وتضمينها في الخلية H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// حفظ المصنف على القرص
workbook.save("output_with_sparklines.xlsx");
```

ينتج عن الكود أعلاه مصنف يتم فيه تكرار كل تمثيل مرئي لخط مؤشر في شكلين: خط المؤشر الحي الأصلي المثبت عند الصف 1، وصورة PNG ثابتة مدمجة مباشرة في خلية مجاورة في الصف 2. ولأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المدمجة. اعرض كل مجموعة خطوط مؤشر كصورة PNG، ثم حوِّل `ByteArrayOutputStream` إلى `byte[]`، وعيِّن المصفوفة إلى الخاصية `EmbeddedImage` للخلية المستهدفة من خلال `setEmbeddedImage(byte[])` — هذا التعيين هو ما يجعل الصورة جزءًا من المحتويات المخزنة للخلية.

{{% alert color="primary" %}}
لأن كل مجموعة خطوط مؤشر مثبتة في خلية واحدة، يمكنك الوصول إليها من خلال المفهرس `group.getSparklines().get(0)` بدلاً من التعداد باستخدام حلقة `for`. يحافظ ذلك على قصر كود العرض ويتطابق مع النمط النموذجي "خط مؤشر واحد لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `Cell.EmbeddedImage` (المعينة من خلال `setEmbeddedImage`) الإصدار Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة عمل خطوط المؤشر إلى HTML**

بمجرد أن يحتوي المصنف على خطوط مؤشر حية (وصور مدمجة اختيارية)، يمكن نشر ورقة العمل بأكملها على الويب عن طريق حفظها بتنسيق HTML. يكشف صنف `HtmlSaveOptions` عن الإعدادات التي تحتاجها للتحكم في هذا التصدير؛ في سير العمل هذا، ستعيد استخدام ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 وتحوله إلى مستند HTML نظيف بصفحة واحدة.

### **إرشادات خطوة بخطوة**

1. تأكد من توفر ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 على القرص في دليل العمل الخاص بك.
2. حمِّل هذا الملف في مثيل `Workbook` جديد.
3. أنشئ مثيلاً من `HtmlSaveOptions` واستدعِ `setExportActiveWorksheetOnly(true)` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بالكامل.
4. استدعِ `workbook.save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

يأخذ الكود أعلاه المصنف الغني بخطوط المؤشر من سير العمل 1 ويحوِّله إلى ملف HTML محمول. تُحفظ خطوط المؤشر كصور SVG مدمجة أو PNG داخل HTML المُنشأ، اعتمادًا على وضع التصدير، حتى يتمكن المستخدمون النهائيون من عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال تعيين `ExportActiveWorksheetOnly` إلى `true` من خلال `setExportActiveWorksheetOnly(true)`، تتجنب النشر غير المقصود للأوراق المخفية أو البيانات المساعدة — يتم تصدير ورقة العمل المرئية حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
يقدم صنف `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `ExportHiddenWorksheet`، و`ExportImagesAsBase64`، و`Encoding`. اضبطها حسب الحاجة وفقًا لهدف النشر لديك.
{{% /alert %}}

## **ملخص واجهة برمجة التطبيقات (API)**

تعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.

- تُستخدم `SparklineGroup` ووصول المجموعة `worksheet.getSparklineGroups()` للإعلان عن النوع (Line، Column، Stacked)، ونطاق البيانات، والخلية المُثبِّتة لكل مجموعة خطوط مؤشر. في هذا المقال، تكون كل مجموعة مثبتة في خلية واحدة، لذلك يتم الوصول إلى المجموعة من خلال `worksheet.getSparklineGroups().get(i)`.
- يُرجع `Sparkline` والمفهرس `group.getSparklines().get(0)` خط المؤشر الفردي داخل المجموعة. لأن كل مجموعة في المثال تحتوي على خط مؤشر واحد بالضبط، فلا حاجة إلى حلقة `for`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة لخط المؤشر في `Stream` مزوَّد. تُرجع هذه الطريقة `void`؛ وتقرأ البايتات من التيار بعد الاستدعاء.
- `Cell.EmbeddedImage` هي خاصية من نوع `byte[]` (تُعيَّن عبر `cell.setEmbeddedImage(byte[])`) تخزِّن صورة داخل خلية واحدة. وهي متوفرة في **Aspose.Cells 26.5 والإصدارات الأحدث**، وهي الطريقة الموصى بها لإرجاع خط مؤشر تم عرضه بواسطة `toImage` إلى نفس المصنف.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` يقصر تصدير HTML على ورقة العمل النشطة. وهي واحدة من أكثر الخصائص استخدامًا في `HtmlSaveOptions` عند إنشاء تقارير ذات صفحة واحدة.
- توجد `ImageOrPrintOptions.setImageType(ImageType)` في حزمة `com.aspose.cells.drawing` وتحدد تنسيق الصورة (على سبيل المثال، `ImageType.PNG`) المستخدم عند العرض باستخدام `toImage` وعند طباعة أوراق العمل كصور.

## **مقالات ذات صلة**

- [Sparklines في Aspose.Cells for Aspose.Cells for Java](/cells/ar/java/sparkline/)
- [إدراج صورة في خلية](/cells/ar/java/inserting-an-image-into-a-cell/)
- [عرض مصفوفة الخلية الواحدة لـ SmartMarker | Aspose.Cells Java](/cells/ar/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}