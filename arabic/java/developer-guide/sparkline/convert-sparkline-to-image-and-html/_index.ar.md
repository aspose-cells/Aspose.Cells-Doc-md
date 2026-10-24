---
title: تحويل الخط المصغر إلى صورة وHTML في Aspose.Cells for Java
linktitle: تحويل الخط المصغر إلى صورة وHTML في Aspose.Cells for Java
description: تعلّم كيفية عرض الخطوط المصغرة في Aspose.Cells كصور مستقلة لتضمينها في الخلايا، وتصدير ورقة عمل تحتوي على خطوط مصغرة إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, Java, الخط المصغر, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, عرض الخط المصغر, تحويل الخط المصغر إلى صورة, تصدير الخط المصغر إلى HTML
type: docs
weight: 120
url: /ar/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
الخطوط المصغرة هي رسوم بيانية صغيرة موضوعة داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل خط مصغر كصورة مستقلة (للتضمين في خلية أخرى أو تقرير خارجي)، فضلًا عن تصدير ورقة العمل كاملةً، بما في ذلك الخطوط المصغرة، إلى HTML للتوزيع عبر الويب. تتوفر خاصية `Cell.EmbeddedImage` المستخدمة في هذه المقالة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **مقدمة**
تُعد الخطوط المصغرة وسيلة مدمجة لعرض الاتجاهات مباشرةً داخل ورقة العمل. ورغم أن مستخدمي Excel يرونها في مواضعها، تتطلب سيناريوهات واقعية كثيرة أن يخرج الخط المصغر من الخلية — على سبيل المثال، لتضمينه في خلية أخرى كصورة ثابتة، أو إرفاقه برسالة بريد إلكتروني آلية، أو عرضه ضمن تقرير HTML منشور على الويب.
تدعم Aspose.Cells هاتين العمليتين. تُنتج طريقة `Sparkline.toImage` صورة خط مصغر فردي في تدفق، ويمكن إسناد البايتات الناتجة إلى `Cell.EmbeddedImage` (عبر `setEmbeddedImage`) لتُخزن الصورة داخل خلية واحدة في المصنف. وفي مسار منفصل، تتيح `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك الخطوط المصغرة — إلى ملف HTML مكتفي بذاته. تشرح هذه المقالة مساري العمل من البداية إلى النهاية.

## **مسار العمل 1 — تحويل الخطوط المصغرة إلى صور وتضمينها في الخلايا**
في مسار العمل هذا، ستنشئ ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وتضيف ثلاث مجموعات مختلفة من الخطوط المصغرة (`Line`، `Column`، و`Stacked/Win-Loss`) مرتبطة بهذا النطاق، وتحوّل كل مجموعة إلى صورة PNG، ثم تكتب بايتات صور PNG في الخلايا المجاورة كصور مضمّنة. وستكون النتيجة ملف `.xlsx` واحدًا يحتوي على كل من الخطوط المصغرة الحية وصورها الثابتة المكافئة.

### **تعليمات خطوة بخطوة**
1. حدد مجلد عمل وتأكد من وجوده على القرص.
2. أنشئ كائن `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
3. املأ الخلايا `A1` إلى `E1` بخمس قيم رقمية نموذجية (مثل المبيعات اليومية أو قراءات درجة الحرارة).
4. أضف ثلاثة كائنات `SparklineGroup` إلى ورقة العمل عن طريق استدعاء `worksheet.getSparklineGroups().add(...)`:
   - مجموعة `SparklineType.LINE` مرستاة عند `F1`، مع نطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.COLUMN` مرستاة عند `G1`، مع نطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.STACKED` (فوز/خسارة) مرستاة عند `H1`، مع نطاق البيانات `A1:E1`.
5. أنشئ كائن `ImageOrPrintOptions` واستدعِ `setImageType(ImageType.PNG)` حتى يُعرض كل خط مصغر كصورة PNG شفافة.
6. استدعِ `workbook.save("output_with_sparklines.xlsx")` لحفظ المصنف على القرص.

```java
import com.aspose.cells.*;
import java.io.*;
// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// إدخال بيانات نموذجية في الخلايا A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// إضافة مجموعة خط شرارة مثبتة عند F1 (العمود 5، الصف 0)
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
// إضافة مجموعة أعمدة شرارة مثبتة عند G1 (العمود 6، الصف 0)
CellArea columnArea = CellArea.createCellArea(0, 6, 0, 6);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
// إضافة مجموعة شرارة الفوز/الخسارة (المكدسة) مثبتة عند H1 (العمود 7، الصف 0)
CellArea stackedArea = CellArea.createCellArea(0, 7, 0, 7);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
// configuring خيارات الصورة لإخراج PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);
// تحويل خط الشرارة إلى صورة وتضمينها في الخلية F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// تحويل عمود الشرارة إلى صورة وتضمينها في الخلية G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// تحويل شرارة الفوز/الخسارة إلى صورة وتضمينها في الخلية H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// حفظ المصنف على القرص
workbook.save("output_with_sparklines.xlsx");
```

ينتج الكود أعلاه مصنفًا يحتوي على تمثيلين لكل خط مصغر: الخط المصغر الأصلي الموضَع في خلية ارتساء بالصف 1، وصورة PNG ثابتة مضمّنة مباشرةً في خلية مجاورة بالصف 2. ولأن الصور موجودة داخل الملف نفسه، يظل المصنف ملفًا واحدًا مكتفيًا بذاته يمكن إرساله بالبريد الإلكتروني أو أرشفته دون أن تصبح مراجع الصور المضمّنة غير صالحة. حوّل كل مجموعة من الخطوط المصغرة إلى صورة PNG، وحوّل `ByteArrayOutputStream` إلى `byte[]`، ثم أسند المصفوفة إلى الخاصية `EmbeddedImage` الخاصة بالخلية الهدف من خلال `setEmbeddedImage(byte[])`؛ فالإسناد هو ما يجعل الصورة جزءًا من المحتوى المخزن في الخلية.

{{% alert color="primary" %}}
لأن كل مجموعة من الخطوط المصغرة مرستاة عند خلية واحدة، يمكنك الوصول إليها عبر المُفهرس `group.getSparklines().get(0)` بدلاً من تعدادها باستخدام حلقة `for`. يجعل هذا الأمر كود العرض قصيرًا ويتوافق مع النمط المعتاد «خط مصغر واحد لكل خلية ارتساء». يتطلب تخزين بايتات الصورة عبر `Cell.EmbeddedImage` (التي يتم تعيينها من خلال `setEmbeddedImage`) Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **مسار العمل 2 — تصدير ورقة العمل التي تحتوي على الخطوط المصغرة إلى HTML**
بعد أن يحتوي المصنف على خطوط مصغرة حية (واختياريًا على صور ثابتة مضمّنة مقابلة لها)، يمكن نشر ورقة العمل بأكملها على الويب بحفظها بصيغة HTML. تتيح فئة `HtmlSaveOptions` التحكم في هذا التصدير؛ وفي مسار العمل هذا، ستعيد استخدام الملف `output_with_sparklines.xlsx` الذي أنشأه مسار العمل 1 لتحويله إلى مستند HTML نظيف من صفحة واحدة.

### **تعليمات خطوة بخطوة**
1. تأكد من توفر الملف `output_with_sparklines.xlsx` الذي أنشأه مسار العمل 1 على القرص في مجلد العمل.
2. حمّل هذا الملف في كائن `Workbook` جديد.
3. أنشئ كائن `HtmlSaveOptions` واستدعِ `setExportActiveWorksheetOnly(true)` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
4. استدعِ `workbook.save("sparklines.html", htmlOptions)` لكتابة مخرجات HTML على القرص.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

يحوّل الكود أعلاه مصنفًا يحتوي على خطوط مصغرة من مسار العمل 1 إلى ملف HTML قابل للنقل. تُحفظ الخطوط المصغرة داخل HTML الذي تم إنشاؤه في صورة تمثيلات SVG أو PNG مضمّنة، بحسب وضع التصدير، ما يتيح للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. وبضبط `ExportActiveWorksheetOnly` على `true` من خلال `setExportActiveWorksheetOnly(true)`، تتجنّب نشر الأوراق المخفية أو البيانات المساعدة عن طريق الخطأ؛ إذ لا يُصدَّر سوى ورقة العمل الظاهرة حاليًا للمستخدم.

{{% alert color="primary" %}}
تتيح فئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `ExportHiddenWorksheet` و`ExportImagesAsBase64` و`Encoding`. اضبطها بما يلائم هدف النشر لديك.
{{% /alert %}}

## **ملخص API**
تعتمد مسارات العمل أعلاه على مجموعة صغيرة من واجهات API في Aspose.Cells تعمل معًا.
- استُخدمت `SparklineGroup` عبر `worksheet.getSparklineGroups()` لتحديد النوع (`Line`، `Column`، `Stacked`)، ونطاق البيانات، وخلية الارتساء لكل مجموعة من الخطوط المصغرة. في هذه المقالة، تكون كل مجموعة مرستاة عند خلية واحدة، لذا يمكن الوصول إلى المجموعة من خلال `worksheet.getSparklineGroups().get(i)`.
- يمثّل `Sparkline` الخط المصغر الفردي داخل المجموعة، ويتيح الفهرس `group.getSparklines().get(0)` الوصول إليه. ولأن كل مجموعة في المثال تحتوي على خط مصغر واحد بالضبط، لا يلزم استخدام حلقة `for`.
- تُعد `Sparkline.toImage(Stream, ImageOrPrintOptions)` طريقة العرض التي تكتب صورة الخط المصغر في `Stream` المقدم. تعيد الطريقة `void`، وتُقرأ البايتات من التدفق بعد الاستدعاء.
- تحدّ `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` من تصدير HTML إلى ورقة العمل النشطة فقط. وهي من بين أكثر خصائص `HtmlSaveOptions` استخدامًا عند إنشاء تقارير من صفحة واحدة.
- تقع `ImageOrPrintOptions.setImageType(ImageType)` في حزمة `com.aspose.cells.drawing` وتحدد تنسيق الصورة (مثل `ImageType.PNG`) المستخدم عند العرض باستخدام `toImage` وعند طباعة أوراق العمل كصور.

## **مقالات ذات صلة**
- [إدراج صورة في خلية](/cells/ar/java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="java" >}}