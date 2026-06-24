---
title: تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: تعرّف على كيفية عرض شرارات Aspose.Cells كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بالشرارات إلى HTML باستخدام HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, عرض sparkline, تحويل sparkline إلى صورة, تصدير sparkline إلى HTML
type: docs
weight: 120
url: /ar/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
الشرارات هي رسوم بيانية صغيرة الحجم تُوضع داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل شرارة كصورة مستقلة (لتضمينها في خلية أخرى أو في تقرير خارجي) وأيضًا تصدير ورقة العمل بأكملها الغنية بالشرارات إلى HTML للتوزيع عبر المتصفح. خاصية `Cell.embedded_image` المستخدمة في هذه المقالة متوفرة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **مقدمة**

تُعد الشرارات طريقة موجزة لتصور الاتجاهات مباشرة داخل ورقة العمل. بينما يراها مستخدمو Excel في مكانها، تتطلب العديد من السيناريوهات العملية أن تغادر الشرارة الخلية — على سبيل المثال، ليتم تضمينها في خلية مختلفة كصورة ثابتة، أو إرفاقها برسالة بريد إلكتروني آلية، أو عرضها كجزء من تقرير HTML منشور على الويب.

يدعم Aspose.Cells كلتا العمليتين. تُحوِّل الطريقة `Sparkline.to_image` شرارة فردية إلى تيار، ويمكن تعيين البايتات الناتجة إلى `Cell.embedded_image` بحيث تُخزَّن الصورة داخل خلية واحدة من المصنف. بشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك الشرارات — إلى ملف HTML مستقل بذاته. تستعرض هذه المقالة سيرَي العمل بشكل كامل.

## **سير العمل 1 — عرض الشرارات كصور وتضمينها في الخلايا**

في سير العمل هذا، ستقوم بإنشاء ورقة عمل تحتوي على نطاق صغير من القيم المصدرية، وإرفاق ثلاث مجموعات شرارات مختلفة (خطية، عمودية، ومكدسة/فوز-خسارة) بهذا النطاق، وعرض كل مجموعة كصورة PNG، وكتابة بايتات PNG هذه في الخلايا المجاورة كصور مضمنة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كل من الشرارات الحية وصورها المعروضة.

### **إرشادات خطوة بخطوة**

1. حدد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم رقمية نموذجية (على سبيل المثال، المبيعات اليومية أو قراءات درجة الحرارة).
4. أضف ثلاث كائنات `SparklineGroup` إلى ورقة العمل باستدعاء `worksheet.sparkline_groups.add(...)`:
   - مجموعة `SparklineType.LINE` مُثبَّتة عند `F1`، بنطاق بيانات `A1:E1`.
   - مجموعة `SparklineType.COLUMN` مُثبَّتة عند `G1`، بنطاق بيانات `A1:E1`.
   - مجموعة `SparklineType.STACKED` (فوز/خسارة) مُثبَّتة عند `H1`، بنطاق بيانات `A1:E1`.
5. أنشئ مثيلًا من `ImageOrPrintOptions` وعيّن خاصية `image_type` إلى `ImageType.PNG` بحيث تُعرض كل شرارة كصورة PNG شفافة.
6. لكل مجموعة من المجموعات الثلاث، اعرض الشرارة الفردية باستخدام `group.sparklines[0].to_image(byte_array_output_stream, image_options)`، ثم حوّل `ByteArrayOutputStream` إلى `byte[]` (أو اقرأ `to_byte_array()` الخاص بها إلى Python `bytes`)، وعيّن البايتات إلى `worksheet.cells["F2"].embedded_image`، و`worksheet.cells["G2"].embedded_image`، و`worksheet.cells["H2"].embedded_image` على التوالي.
7. احفظ المصنف باسم `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# تعبئة بيانات عينة في الخلايا A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# إضافة مجموعة مؤشرات سطرية من نوع خط مثبتة في F1 (العمود 5، الصف 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# إضافة مجموعة مؤشرات سطرية من نوع عمود مثبتة في G1 (العمود 6، الصف 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# إضافة مجموعة مؤشرات سطرية من نوع فوز/خسارة (مكدسة) مثبتة في H1 (العمود 7، الصف 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# تكوين خيارات الصورة للإخراج بصيغة PNG
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# تحويل المؤشر السطري الخطي إلى صورة وتضمينها في الخلية F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# تحويل المؤشر السطري العمودي إلى صورة وتضمينها في الخلية G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# تحويل المؤشر السطري فوز/خسارة إلى صورة وتضمينها في الخلية H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# حفظ المصنف على القرص
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

ينتج عن الكود أعلاه مصنفًا يتم فيه تكرار كل تمثيل بصري لشرارة في شكلين: الشرارة الحية الأصلية المُثبَّتة عند الصف 1، وصورة PNG ثابتة مضمنة مباشرةً في خلية مجاورة في الصف 2. نظرًا لأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المضمنة. اعرض كل مجموعة شرارات كصورة PNG، وحول `ByteArrayOutputStream` إلى `byte[]` (أو استخدم `to_byte_array()` للحصول على كائن Python `bytes`)، وعيّن المصفوفة إلى خاصية `embedded_image` للخلية المستهدفة — هذا التعيين هو ما يجعل الصورة جزءًا من المحتويات المخزَّنة للخلية.

{{% alert color="primary" %}}
نظرًا لأن كل مجموعة شرارات مُثبَّتة في خلية واحدة، يمكنك الوصول إليها من خلال المفهرس `group.sparklines[0]` بدلاً من التعداد باستخدام حلقة `for`. هذا يحافظ على قصر كود العرض ويتطابق مع النمط النموذجي "شرارة واحدة لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `Cell.embedded_image` إصدار Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة عمل الشرارات إلى HTML**

بمجرد أن يحتوي المصنف على شرارات حية (وصورًا مضمنة اختياريًا)، يمكن نشر ورقة العمل بأكملها على الويب بحفظها بتنسيق HTML. توفّر فئة `HtmlSaveOptions` خيارات التحكم اللازمة لهذا التصدير؛ في سير العمل هذا، ستعيد استخدام ملف `output_with_sparklines.xlsx` المُنشَأ في سير العمل 1 وتحوِّله إلى مستند HTML نظيف أحادي الصفحة.

### **إرشادات خطوة بخطوة**

1. تأكد من توفر ملف `output_with_sparklines.xlsx` المُنشَأ في سير العمل 1 على القرص في دليل العمل لديك.
2. حمّل هذا الملف في مثيل `Workbook` جديد.
3. أنشئ مثيلًا من `HtmlSaveOptions` وعيّن خاصية `export_active_worksheet_only` إلى `True` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
4. استدعِ `workbook.save("sparklines.html", html_options)` لكتابة مخرجات HTML على القرص.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

يأخذ الكود أعلاه المصنف الغني بالشرارات من سير العمل 1 ويحوِّله إلى ملف HTML محمول. تُحفظ الشرارات كصور SVG أو PNG مضمنة داخل HTML المُنشَأ، بناءً على وضع التصدير، حتى يتمكن المستخدمون النهائيون من عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال تعيين `export_active_worksheet_only` إلى `True`، تتجنب نشر الأوراق المخفية أو البيانات المساعدة عن طريق الخطأ — حيث يتم تصدير ورقة العمل المرئية حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
توفّر فئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `export_hidden_worksheet`، و`export_images_as_base64`، و`encoding`. اضبط هذه حسب الحاجة لهدف النشر لديك.
{{% /alert %}}

## **ملخص واجهة برمجة التطبيقات (API)**

تعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.

- تُستخدم `SparklineGroup` ووصول المجموعة `worksheet.sparkline_groups` للإعلان عن النوع (خطي، عمودي، مكدس)، ونطاق البيانات، والخلية المُثبِّتة لكل مجموعة شرارات. في هذه المقالة، تُثبَّت كل مجموعة في خلية واحدة، لذا يتم الوصول إلى المجموعة من خلال `worksheet.sparkline_groups[i]`.
- يُرجع `Sparkline` والمفهرس `group.sparklines[0]` الشرارة الفردية داخل المجموعة. نظرًا لأن كل مجموعة في المثال تحتوي على شرارة واحدة بالضبط، فلا حاجة إلى حلقة `for`.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة للشرارة في `OutputStream` مُمرَّر (مثل `ByteArrayOutputStream`). تُرجع هذه الطريقة `void`؛ وتقرأ البايتات من التيار بعد الاستدعاء.
- `Cell.embedded_image` هي خاصية من نوع `byte[]` تخزن صورة داخل خلية واحدة. وهي متوفرة في **Aspose.Cells 26.5 والإصدارات الأحدث** وهي الطريقة الموصى بها لإعادة إدخال شرارة معروضة بواسطة `to_image` إلى نفس المصنف.
- `HtmlSaveOptions.export_active_worksheet_only` (من نوع `bool`) يقصر تصدير HTML على ورقة العمل النشطة. وهي واحدة من أكثر الخصائص استخدامًا على `HtmlSaveOptions` عند إنشاء تقارير أحادية الصفحة.
- توجد `ImageOrPrintOptions.image_type` في مساحة الأسماء `com.aspose.cells.drawing` وتحدد تنسيق الصورة (على سبيل المثال، `ImageType.PNG`) المستخدم عند العرض باستخدام `to_image` وعند طباعة أوراق العمل كصور.

## **مقالات ذات صلة**

- [الشرارات في Aspose.Cells لـ Aspose.Cells for Python via Java](/cells/ar/python-java/sparkline/)
- [إدراج صورة في خلية](/cells/ar/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}