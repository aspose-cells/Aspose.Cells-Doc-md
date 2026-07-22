---
title: تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: تعلّم كيفية عرض خطوط Sparkline من Aspose.Cells كصور مستقلة لتضمينها في الخلايا وتصدير أوراق العمل الغنية بـ Sparkline إلى HTML باستخدام HtmlSaveOptions في Python via .NET.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, عرض sparkline, تحويل sparkline إلى صورة, تصدير sparkline إلى HTML
type: docs
weight: 120
url: /ar/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
خطوط Sparkline هي رسوم بيانية مصغّرة موضوعة داخل خلايا ورقة العمل. يتيح لك Aspose.Cells استخراج كل خط Sparkline كصورة مستقلة (لتضمينها في خلية أخرى أو تقرير خارجي) وأيضًا تصدير ورقة العمل بأكملها الغنية بـ Sparkline إلى HTML للتوزيع عبر المتصفح. الخاصية `cell.embedded_image` المستخدمة في هذه المقالة متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث**.
{{% /alert %}}

## **المقدمة**

تُعدّ خطوط Sparkline طريقة مدمجة لتصور الاتجاهات مباشرة داخل ورقة العمل. بينما يراها مستخدمو Excel في مكانها، تتطلب العديد من السيناريوهات الواقعية أن يغادر خط Sparkline الخلية — على سبيل المثال، ليتم تضمينه في خلية مختلفة كصورة ثابتة، أو إرفاقه برسالة بريد إلكتروني مؤتمتة، أو عرضه كجزء من تقرير HTML منشور على الويب.

يدعم Aspose.Cells كلتا العمليتين. تُحوّل الطريقة `sparkline.to_image` خط Sparkline فرديًا إلى تدفق بيانات، ويمكن تعيين البايتات الناتجة إلى `cell.embedded_image` بحيث يتم تخزين الصورة داخل خلية واحدة من المصنف. بشكل منفصل، يتيح لك `HtmlSaveOptions` تحويل المصنف بأكمله — بما في ذلك خطوط Sparkline — إلى ملف HTML مستقل بذاته. تتناول هذه المقالة سير العمل كلاهما بشكل كامل.

## **سير العمل 1 — عرض خطوط Sparkline كصور وتضمينها في الخلايا**

في سير العمل هذا، ستقوم ببناء ورقة عمل تحتوي على نطاق صغير من قيم المصدر، وإرفاق ثلاث مجموعات مختلفة من Sparkline (خطية، عمودية، ومكدسة/فوز-خسارة) بهذا النطاق، وعرض كل مجموعة كصورة PNG، وكتابة وحدات بايت PNG هذه في الخلايا المجاورة كصور مضمّنة. النتيجة النهائية هي ملف `.xlsx` واحد يحتوي على كل من خطوط Sparkline الحية وصورها المرسومة المقابلة لها.

### **تعليمات خطوة بخطوة**

1. حدد دليل عمل وتأكد من وجوده على القرص.
2. أنشئ `Workbook` جديدًا واحصل على مرجع إلى أول `Worksheet`.
3. املأ الخلايا من `A1` إلى `E1` بخمس قيم عددية نموذجية (على سبيل المثال، المبيعات اليومية أو قراءات درجات الحرارة).
4. أضف ثلاث كائنات `SparklineGroup` إلى ورقة العمل عن طريق استدعاء `worksheet.sparkline_groups.add(...)`:
   - مجموعة `SparklineType.LINE` مثبّتة عند `F1`، بنطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.COLUMN` مثبّتة عند `G1`، بنطاق البيانات `A1:E1`.
   - مجموعة `SparklineType.STACKED` (فوز/خسارة) مثبّتة عند `H1`، بنطاق البيانات `A1:E1`.
5. أنشئ مثيلًا من `ImageOrPrintOptions` وعيّن `image_type` الخاص به إلى `ImageType.PNG` بحيث يتم عرض كل خط Sparkline كصورة PNG شفافة.
6. لكل مجموعة من المجموعات الثلاث، اعرض خط Sparkline الوحيد باستخدام `group.sparklines[0].to_image(memory_stream, image_options)`، ثم حوّل تدفق `BytesIO` إلى كائن `bytes`، وعيّن المصفوفة إلى `worksheet.cells["F2"].embedded_image`، و`worksheet.cells["G2"].embedded_image`، و`worksheet.cells["H2"].embedded_image` على التوالي.
7. احفظ المصنف باسم `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ملء بيانات عينة في الخلايا A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# إضافة مجموعة شرارات خطية مثبتة في F1 (العمود 5، الصف 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# إضافة مجموعة شرارات عمودية مثبتة في G1 (العمود 6، الصف 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# إضافة مجموعة شرارات فوز/خسارة (مكدسة) مثبتة في H1 (العمود 7، الصف 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# تكوين خيارات الصورة لإخراج PNG
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# تحويل الشرارة الخطية إلى صورة وتضمينها في الخلية F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# تحويل الشرارة العمودية إلى صورة وتضمينها في الخلية G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# تحويل شرارة الفوز/الخسارة إلى صورة وتضمينها في الخلية H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# حفظ المصنف على القرص
workbook.save("output_with_sparklines.xlsx")
```

ينتج عن الكود أعلاه مصنفًا يتم فيه تكرار كل تمثيل مرئي لخط Sparkline في شكلين: خط Sparkline الحي الأصلي المثبّت في الصف 1، وصورة PNG ثابتة مضمّنة مباشرة في خلية مجاورة في الصف 2. ولأن الصور تعيش داخل الملف نفسه، يظل المصنف قطعة واحدة مستقلة بذاتها يمكن إرسالها عبر البريد الإلكتروني أو أرشفتها دون كسر مراجع الصور المضمّنة. اعرض كل مجموعة Sparkline كصورة PNG، ثم حوّل تدفق `BytesIO` إلى كائن `bytes`، وعيّن البايتات إلى خاصية `embedded_image` للخلية المستهدفة — التعيين هو ما يجعل الصورة جزءًا من المحتويات المخزنة للخلية.

{{% alert color="primary" %}}
لأن كل مجموعة Sparkline مثبّتة في خلية واحدة، يمكنك الوصول إليها من خلال المفهرس `group.sparklines[0]` بدلاً من التعداد باستخدام حلقة `for`. يُبقي هذا كود العرض قصيرًا ويتطابق مع النمط النموذجي "خط Sparkline واحد لكل خلية تثبيت". يتطلب تخزين بايتات الصورة عبر `cell.embedded_image` إصدار Aspose.Cells 26.5 أو أحدث.
{{% /alert %}}

## **سير العمل 2 — تصدير ورقة عمل Sparkline إلى HTML**

بمجرد أن يحتوي المصنف على خطوط Sparkline حية (وصور مضمّنة اختيارية مقابلة)، يمكن نشر ورقة العمل بأكملها على الويب عن طريق حفظها بتنسيق HTML. تعرض فئة `HtmlSaveOptions` الأدوات التي تحتاجها للتحكم في هذا التصدير؛ في سير العمل هذا، ستعيد استخدام ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 وتحوله إلى مستند HTML نظيف ذو صفحة واحدة.

### **تعليمات خطوة بخطوة**

1. تأكد من أن ملف `output_with_sparklines.xlsx` الذي أنتجه سير العمل 1 متاح على القرص في دليل العمل الخاص بك.
2. حمّل هذا الملف في مثيل جديد من `Workbook`.
3. أنشئ مثيلًا من `HtmlSaveOptions` وعيّن خاصية `export_active_worksheet_only` الخاصة به إلى `True` بحيث يحتوي ملف HTML الناتج على ورقة العمل النشطة فقط بدلاً من المصنف بأكمله.
4. استدعِ `workbook.save("sparklines.html", html_options)` لكتابة مخرجات HTML على القرص.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

يأخذ الكود أعلاه المصنف الغني بـ Sparkline من سير العمل 1 ويحوّله إلى ملف HTML محمول. يتم الحفاظ على خطوط Sparkline كصور SVG أو PNG مضمّنة داخل HTML المُنشأ، اعتمادًا على وضع التصدير، بحيث يمكن للمستخدمين النهائيين عرض الاتجاهات في أي متصفح حديث دون الحاجة إلى تثبيت Excel. من خلال تعيين `export_active_worksheet_only` إلى `True`، تتجنب نشر الأوراق المخفية أو البيانات المساعدة عن طريق الخطأ — يتم تصدير ورقة العمل المرئية حاليًا للمستخدم فقط.

{{% alert color="primary" %}}
تقدم فئة `HtmlSaveOptions` خصائص إضافية لضبط المخرجات بدقة، مثل `export_hidden_worksheet`، و`export_images_as_base64`، و`encoding`. اضبط هذه حسب الحاجة لهدف النشر الخاص بك.
{{% /alert %}}

## **ملخص واجهة برمجة التطبيقات**

تعتمد سير العمل أعلاه على مجموعة صغيرة من واجهات Aspose.Cells التي تعمل معًا.

- تُستخدم `SparklineGroup` ووصول المجموعة `worksheet.sparkline_groups` للإعلان عن النوع (خطي، عمودي، مكدس)، ونطاق البيانات، والخلية المُثبّتة لكل مجموعة Sparkline. في هذه المقالة، كل مجموعة مثبّتة في خلية واحدة، لذا يتم الوصول إلى المجموعة من خلال `worksheet.sparkline_groups[i]`.
- يُرجع `Sparkline` والمفهرس `group.sparklines[0]` خط Sparkline الفردي داخل المجموعة. نظرًا لأن كل مجموعة في المثال تحتوي على خط Sparkline واحد فقط، فلا حاجة إلى حلقة `for`.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` هي طريقة العرض التي تكتب صورة لخط Sparkline في تدفق بيانات مُقدّم. تُرجع الطريقة `None`؛ يمكنك قراءة البايتات من التدفق بعد الاستدعاء.
- `cell.embedded_image` هي خاصية `bytes` تخزن صورة داخل خلية واحدة. وهي متاحة في **Aspose.Cells 26.5 والإصدارات الأحدث** وهي الطريقة الموصى بها لإعادة إدخال خط Sparkline المعروض بواسطة `to_image` في نفس المصنف.
- `html_save_options.export_active_worksheet_only` (من النوع `bool`) يقتصر تصدير HTML على ورقة العمل النشطة. وهي واحدة من أكثر الخصائص استخدامًا في `HtmlSaveOptions` عند إنشاء تقارير ذات صفحة واحدة.
- تقع `image_or_print_options.image_type` في مساحة الأسماء `aspose.cells.drawing` وتحدد تنسيق الصورة (على سبيل المثال، `ImageType.PNG`) المستخدم عند العرض باستخدام `to_image` وعند طباعة أوراق العمل كصور.

## **مقالات ذات صلة**

- [Sparklines in Aspose.Cells for Python via .NET](/cells/ar/python-net/sparkline/)
- [Inserting an Image into a Cell](/cells/ar/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/ar/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}