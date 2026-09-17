---
title: إدراج صورة في خلية
linktitle: إدراج صورة في خلية
description: Aspose.Cells for Python via Java هي مكتبة للعمل مع ملفات جداول البيانات. تشرح هذه المقالة كيفية ملاءمة صورة بدقة داخل خلية واحدة، سواء عن طريق وضع صورة عائمة فوق الخلية أو عن طريق تضمين الصورة مباشرة داخل الخلية.
keywords: Aspose.Cells، مكتبة Python عبر Java، جدول بيانات، إدراج صورة، تضمين صورة، صورة داخل خلية، ملاءمة صورة مع خلية، PictureCollection، EmbeddedImage
type: docs
weight: 80
url: /ar/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفّر Aspose.Cells طريقتين متميزتين لربط صورة بخلية واحدة. الصورة العائمة هي شكل على طبقة الرسم في ورقة العمل يغطي بصريًا نطاقًا من الخلايا، بينما تُخزَّن الصورة المضمّنة داخل الخلية نفسها وتتمدّد تلقائيًا لتلائم مساحة عرض الخلية. اختر الأسلوب الذي يتطابق بشكل أفضل مع متطلبات التخطيط لديك.

## **مقدمة**
تُعدّ ملاءمة صورة بدقة داخل خلية واحدة مطلبًا شائعًا عند تصميم جداول بيانات تعمل كتقارير بصرية، أو كتالوجات منتجات، أو أدلة موظفين، أو لوحات معلومات، أو قوائم جرد. وبدلًا من تمديد صورة عبر عدة خلايا أو وضعها بشكل غير محكم على ورقة العمل، قد ترغب في صورة نظيفة مرتبطة بالخلية وتظل محاذية للخلية التي تنتمي إليها.
يدعم Aspose.Cells هذا السيناريو بطريقتين متكاملتين:
- **الأسلوب 1 — وضع صورة عائمة فوق خلية.** أضف `Picture` إلى ورقة العمل، وعيّن `setPlacement` إلى `MOVE_AND_SIZE`، واضبط خلايا التثبيت (`setUpperLeftRow`، `setUpperLeftColumn`، `setLowerRightRow`، `setLowerRightColumn`) بحيث تغطي الصورة خلية واحدة بالضبط.
- **الأسلوب 2 — تضمين صورة مباشرة في خلية.** خصّص وحدات بايت الصورة إلى خاصية `setEmbeddedImage` للخلية. تتمدد الصورة تلقائيًا لتلائم مساحة عرض الخلية وتنتقل معها.
يتناول بقيّة هذه المقالة كلا الأسلوبين، ويشرح واجهات برمجة التطبيقات ذات الصلة، ويوضّح كيفية استخدامها في الكود.

## **الأسلوب 1: وضع صورة فوق خلية**
الصورة العائمة هي كائن `Picture` يعيش على طبقة الرسم في ورقة العمل. وعلى الرغم من أنها ليست جزءًا من أي خلية واحدة، إلا أنها مُثبَّتة على نطاق من الخلايا. تحدّد خلايا التثبيت الخاصة بالصورة — الزاويتان العلوية اليسرى والسفلية اليمنى — امتدادها البصري على ورقة العمل. افتراضيًا، تمتد الصورة المُضافة حديثًا عبر عدة خلايا.
لجعل الصورة العائمة تغطي **خلية واحدة بالضبط**، تحتاج إلى:
1. إضافة الصورة باستخدام `Worksheet.getPictures().add(int row, int column, InputStream stream)`، الذي يُثبّت الصورة الجديدة على الخلية المحددة.
2. تعيين خصائص التثبيت الأربعة بحيث يتطابق المستطيل المحيط للصورة مع الخلية الهدف.
3. تعيين `Picture.setPlacement` إلى `PlacementType.MOVE_AND_SIZE` بحيث تتحرك الصورة وتُعيد تحجيمها مع الخلية الأصلية عند قيام المستخدم بتغيير عرض العمود أو ارتفاع الصف.

### **تثبيت الصورة على خلية واحدة**
يتم تعريف تثبيت الصورة من خلال أربع خصائص تعتمد على المؤشرات ذات الأساس الصفري:
- `setUpperLeftRow` — مؤشر الصف للحافة العلوية للصورة.
- `setUpperLeftColumn` — مؤشر العمود للحافة اليسرى للصورة.
- `setLowerRightRow` — مؤشر الصف للحافة السفلية للصورة. لجعل الحافة السفلية للصورة تقع في أسفل الصف `r`، عيّن هذا إلى `r + 1`.
- `setLowerRightColumn` — مؤشر العمود للحافة اليمنى للصورة. لجعل الحافة اليمنى للصورة تقع في يمين العمود `c`، عيّن هذا إلى `c + 1`.

{{% alert color="primary" %}}
مؤشرات الصفوف والأعمدة في Aspose.Cells **مبنية على الأساس الصفري**. الخلية C6 لها مؤشر صف 5 ومؤشر عمود 2. تُعدّ أخطاء الفهرسة بمقدار واحد (off-by-one) في تثبيت الزاوية السفلية اليمنى المصدر الأكثر شيوعًا لظهور الصور متداخلة في خلية مجاورة.

### **التحكم في سلوك الوضع**
`getPlacement` هو enum من نوع `PlacementType` يتحكم في كيفية تصرف الصورة عند قيام المستخدم بتغيير حجم الصف أو العمود الواقع تحتها. القيمة الموصى بها لصورة خلية واحدة هي `PlacementType.MOVE_AND_SIZE`، التي تتسبب في تحرك الصورة وإعادة تحجيمها مع خليتها الأصلية، محافظةً بذلك على الملاءمة الدقيقة.

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح واحدًا موجودًا).
2. الوصول إلى `Worksheet` الهدف من `workbook.getWorksheets().get(0)`.
3. افتح ملف الصورة من القرص في `InputStream` (عادةً `FileInputStream`) بحيث يُغلق التدفق بشكل صحيح.
4. استدعِ `worksheet.getPictures().add(5, 2, stream)` لإضافة صورة مُثبَّتة على الخلية C6. والتقط مرجع `Picture` المُعاد.
5. عيّن إحداثيات التثبيت الأربعة بحيث تغطي الصورة الخلية C6 فقط: `setUpperLeftRow(5)`، `setUpperLeftColumn(2)`، `setLowerRightRow(6)`، `setLowerRightColumn(3)`.
6. عيّن `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` للحفاظ على محاذاة الصورة مع C6 عند تغيير حجم العمود أو الصف.
7. اختياريًا، أضف نصًا نموذجيًا إلى الخلايا المحيطة لإثبات أن الخلية C6 وحدها تحتوي على الصورة.
8. احفظ المصنف على القرص كملف `.xlsx`.
يوضّح الكود التالي الأسلوب بالكامل.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **الأسلوب 2: تضمين صورة مباشرة في خلية**
يكشف Aspose.Cells أيضًا عن آلية أبسط للصور المرتبطة بالخلايا: خاصية `Cell.setEmbeddedImage`. يؤدي تعيين وحدات بايت الصورة على هذه الخاصية إلى إرفاق الصورة بالخلية نفسها، كما لو كانت محتوى مضمّنًا.

### **كيف تعمل الصور المضمّنة**
- تُخزَّن الصورة كجزء من محتوى الخلية بدلاً من أن تكون شكلًا على طبقة الرسم.
- تتمدد الصورة تلقائيًا لتتلاءم مع الحدود المعروضة للخلية. لا حاجة إلى إحداثيات تثبيت أو إعدادات وضع.
- تظل الخلية خلية حقيقية بعنوان حقيقي يمكن الاشارة إليه بواسطة الصيغ، أو فرزها كجزء من صف، أو استخدامها في عمليات أخرى على مستوى الخلية.
يجعل هذا `Cell.setEmbeddedImage` الخيار الأكثر إيجازًا عندما يكون هدفك ببساطة "صورة تعيش داخل هذه الخلية".

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح واحدًا موجودًا).
2. الوصول إلى `Worksheet` الهدف من `workbook.getWorksheets().get(0)`.
3. اقرأ ملف الصورة من القرص في مصفوفة `byte[]` (على سبيل المثال، باستخدام استدعاء `Files.readAllBytes` من `java.nio.file.Files`).
4. احصل على مرجع للخلية الهدف — إما من خلال `worksheet.getCells().get("C6")` أو `worksheet.getCells().get(5, 2)`.
5. خصّص مصفوفة البايتات إلى خاصية `setEmbeddedImage` للخلية.
6. اختياريًا، اضبط ارتفاع الصف وعرض العمود للصف والعمود الهدف لمنح الصورة المضمّنة مظهرًا أكثر بروزًا.
7. احفظ المصنف على القرص كملف `.xlsx`.
يوضّح الكود التالي الأسلوب بالكامل.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **اختيار الأسلوب المناسب**
يُنتج كلا الأسلوبين صورة تلائم داخل خلية واحدة، لكنهما يختلفان في كيفية تخزين الصورة وكيفية تصرفها:
- **استخدم صورة عائمة (الأسلوب 1) عندما:**
  - تحتاج إلى تحكم أدق في الوضع، أو الطبقات، أو المحاذاة مع كائنات الرسم الأخرى.
  - تريد أن تتصرف الصورة كشكل يمكن تحديده، أو إعادة ترتيبه، أو تجميعه مع أشكال أخرى.
  - تحتاج إلى توافق قديم مع كود يعمل بالفعل مع `PictureCollection`.
  - تحتاج إلى حساب إحداثيات التثبيت ديناميكيًا بناءً على تخطيط ورقة العمل.
- **استخدم صورة مضمّنة (الأسلوب 2) عندما:**
  - تريد أبسط إدراج ممكن لصورة في خلية.
  - يجب أن تنتقل الصورة مع الخلية مثل أي محتوى آخر للخلية.
  - لا تحتاج إلى معالجة الصورة كشكل.
{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="python" >}}