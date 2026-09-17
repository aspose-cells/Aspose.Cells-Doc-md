---
title: إدراج صورة في خلية
linktitle: إدراج صورة في خلية
description: Aspose.Cells هي مكتبة Python للعمل مع ملفات جداول البيانات. توضح هذه المقالة كيفية ضبط صورة بدقة لتناسب خلية واحدة، إما عن طريق وضع صورة عائمة فوق الخلية أو عن طريق تضمين الصورة مباشرة داخل الخلية.
keywords: Aspose.Cells, مكتبة Python, جدول بيانات, إدراج صورة, تضمين صورة, صورة في خلية, ضبط الصورة للخلية, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ar/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells طريقتين متميزتين لربط صورة بخلية واحدة. الصورة العائمة هي شكل على طبقة الرسم في ورقة العمل يغطي بصريًا نطاقًا من الخلايا، بينما تُخزَّن الصورة المضمنة داخل الخلية نفسها وتتدرج تلقائيًا لتناسب منطقة عرض الخلية. اختر الطريقة الأنسب لمتطلبات التخطيط لديك.

## **مقدمة**
يُعدّ ضبط صورة بدقة لتناسب خلية واحدة مطلبًا شائعًا عند تصميم جداول بيانات تعمل كتقارير مرئية أو كتالوجات منتجات أو سجلات موظفين أو لوحات معلومات أو قوائم جرد. بدلًا من تمديد الصورة عبر عدة خلايا أو وضعها بشكل غير محكم على ورقة العمل، قد ترغب في صورة نظيفة مرتبطة بخلية تبقى محاذية مع الخلية المالكة لها.
يدعم Aspose.Cells هذا السيناريو بطريقتين متكاملتين:
- **النهج 1 — وضع صورة عائمة فوق خلية.** أضف `Picture` إلى ورقة العمل، واضبط `placement` على `MOVE_AND_SIZE`، وعدّل خلايا الإرساء (`upper_left_row`، `upper_left_column`، `lower_right_row`، `lower_right_column`) بحيث تغطي الصورة خلية واحدة تمامًا.
- **النهج 2 — تضمين صورة مباشرة في خلية.** خصّص وحدات بايت الصورة إلى خاصية `embedded_image` للخلية. تتدرج الصورة تلقائيًا لتناسب منطقة عرض الخلية وتنتقل مع الخلية.
تتناول بقية هذه المقالة كلا النهجين، وتشرح واجهات برمجة التطبيقات ذات الصلة، وتوضح كيفية استخدامهما في الكود.

## **النهج 1: وضع صورة فوق خلية**
الصورة العائمة هي كائن `Picture` يعيش على طبقة الرسم في ورقة العمل. وعلى الرغم من أنها ليست جزءًا من أي خلية واحدة، إلا أنها مُرتبطة بنطاق من الخلايا. تحدد خلايا الإرساء الخاصة بالصورة — زواياها العلوية اليسرى والسفلية اليمنى — نطاقها المرئي على ورقة العمل. افتراضيًا، تمتد الصورة المضافة حديثًا عبر عدة خلايا.
لجعل الصورة العائمة تغطي **خلية واحدة بالضبط**، يلزم:
1. إضافة الصورة باستخدام `Worksheet.pictures.add(row, column, stream)`، مما يربط الصورة الجديدة بالخلية المحددة.
2. تعيين خصائص الإرساء الأربع بحيث يتطابق المستطيل المحيط بالصورة مع الخلية المستهدفة.
3. تعيين `Picture.placement` على `PlacementType.MOVE_AND_SIZE` بحيث تتحرك الصورة وتعيد تحجيمها مع الخلية الأساسية عند قيام المستخدم بتغيير عرض العمود أو ارتفاع الصف.

### **ربط الصورة بخلية واحدة**
يُحدَّد إرساء الصورة بأربع خصائص ذات فهرس يبدأ من الصفر:
- `Picture.upper_left_row` — فهرس الصف للحافة العلوية للصورة.
- `Picture.upper_left_column` — فهرس العمود للحافة اليسرى للصورة.
- `Picture.lower_right_row` — فهرس الصف للحافة السفلية للصورة. لجعل الحافة السفلية للصورة تقع في أسفل الصف `r`، اضبط هذه القيمة على `r + 1`.
- `Picture.lower_right_column` — فهرس العمود للحافة اليمنى للصورة. لجعل الحافة اليمنى للصورة تقع في يمين العمود `c`، اضبط هذه القيمة على `c + 1`.

{{% alert color="primary" %}}
فهارس الصفوف والأعمدة في Aspose.Cells **تبدأ من الصفر**. الخلية C6 لها فهرس صف 5 وفهرس عمود 2. تُعدّ أخطاء الانحراف بمقدار واحد في إرساء الزاوية السفلية اليمنى السبب الأكثر شيوعًا لظهور صور تبدو متداخلة مع خلية مجاورة.

### **التحكم في سلوك الوضع**
`Picture.placement` هو تعداد من نوع `PlacementType` يتحكم في كيفية تصرف الصورة عند قيام المستخدم بإعادة تحجيم الصف أو العمود الذي تحته. القيمة الموصى بها لصورة خلية واحدة هي `PlacementType.MOVE_AND_SIZE`، والتي تتسبب في تحرك الصورة وإعادة تحجيمها مع الخلية الأساسية الخاصة بها، محافظةً على التوافق الدقيق.

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح ملفًا موجودًا).
2. الوصول إلى `Worksheet` المستهدفة من `workbook.worksheets[0]`.
3. افتح ملف الصورة من القرص في تدفق ملف (أو كائن `BytesIO`) باستخدام كتلة `with` ليتم التخلص من التدفق بشكل صحيح.
4. استدعِ `worksheet.pictures.add(5, 2, stream)` لإضافة صورة مرتبطة بالخلية C6. التقط مرجع `Picture` المُعاد.
5. عيّن إحداثيات الإرساء الأربع بحيث تغطي الصورة الخلية C6 فقط: `upper_left_row = 5`، `upper_left_column = 2`، `lower_right_row = 6`، `lower_right_column = 3`.
6. عيّن `picture.placement = PlacementType.MOVE_AND_SIZE` للحفاظ على محاذاة الصورة مع C6 عند إعادة تحجيم العمود أو الصف.
7. اختياريًا، أضف نصًا نموذجيًا إلى الخلايا المحيطة لتوضيح أن الخلية C6 فقط هي التي تحتوي على الصورة.
8. احفظ المصنف على القرص كملف `.xlsx`.
يوضح الكود التالي النهج الكامل.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **النهج 2: تضمين صورة مباشرة في خلية**
يوفر Aspose.Cells أيضًا آلية أبسط للصور المرتبطة بالخلايا: خاصية `Cell.embedded_image`. يخصص تعيين وحدات بايت الصورة لهذه الخاصةية الصورة للخلية نفسها، كما لو كانت محتوى مضمّنًا.

### **كيف تعمل الصور المضمنة**
- تُخزَّن الصورة كجزء من محتوى الخلية بدلاً من كونها شكلًا على طبقة الرسم.
- تتدرج الصورة تلقائيًا لتناسب الحدود المعروضة للخلية. لا حاجة إلى إحداثيات إرساء أو إعدادات وضع.
- تظل الخلية خلية حقيقية بعنوان حقيقي يمكن الإشارة إليه بواسطة الصيغ، أو فرزها كجزء من صف، أو استخدامها في عمليات أخرى على مستوى الخلية.
يجعل هذا من `Cell.embedded_image` الخيار الأكثر إيجازًا عندما يكون هدفك ببساطة "صورة تعيش داخل هذه الخلية".

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح ملفًا موجودًا).
2. الوصول إلى `Worksheet` المستهدفة من `workbook.worksheets[0]`.
3. اقرأ ملف الصورة من القرص في كائن `bytes` (على سبيل المثال، بفتح الملف في الوضع الثنائي واستدعاء `.read()`).
4. احصل على مرجع للخلية المستهدفة — إما من خلال `worksheet.cells["C6"]` أو `worksheet.cells[5, 2]`.
5. خصّص كائن البايتات إلى خاصية `embedded_image` للخلية.
6. اختياريًا، اضبط ارتفاع الصف وعرض العمود للصف والعمود المستهدفين لإعطاء الصورة المضمنة مظهرًا أكثر بروزًا.
7. احفظ المصنف على القرص كملف `.xlsx`.
يوضح الكود التالي النهج الكامل.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **اختيار النهج المناسب**
يُنتج كلا النهجين صورة تناسب خلية واحدة، لكنهما يختلفان في كيفية تخزين الصورة وكيفية تصرفها:
- **استخدم صورة عائمة (النهج 1) عند:**
  - حاجتك إلى تحكم أدق في الوضع أو الطبقات أو المحاذاة مع كائنات الرسم الأخرى.
  - رغبتك في أن تتصرف الصورة كشكل يمكن تحديده أو إعادة ترتيبه أو تجميعه مع أشكال أخرى.
  - حاجتك إلى توافق قديم مع الكود الذي يعمل بالفعل مع مجموعات `pictures`.
  - حاجتك إلى حساب إحداثيات الإرساء ديناميكيًا بناءً على تخطيط ورقة العمل.
- **استخدم صورة مضمنة (النهج 2) عند:**
  - رغبتك في أبسط إدراج ممكن لصورة في خلية.
  - ضرورة انتقال الصورة مع الخلية مثل أي محتوى خلية آخر.
  - عدم حاجتك إلى معالجة الصورة كشكل.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for Python via .NET](/cells/ar/python-net/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET](/cells/ar/python-net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ar/python-net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Python via .NET](/cells/ar/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}