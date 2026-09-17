---
title: إدراج صورة في خلية
linktitle: إدراج صورة في خلية
description: Aspose.Cells for Java هي مكتبة للعمل مع ملفات جداول البيانات. يوضح هذا المقال كيفية احتواء صورة بدقة في خلية واحدة، إما عن طريق وضع صورة عائمة فوق الخلية أو عن طريق تضمين الصورة مباشرة في الخلية.
keywords: Aspose.Cells, مكتبة Java, جدول بيانات, إدراج صورة, تضمين صورة, صورة في خلية, احتواء الصورة في الخلية, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /ar/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells طريقتين متميزتين لربط صورة بخلية واحدة. الصورة العائمة هي شكل على طبقة الرسم في ورقة العمل يغطي بصريًا نطاقًا من الخلايا، بينما تُخزَّن الصورة المضمنة داخل الخلية نفسها وتتناسب تلقائيًا مع منطقة عرض الخلية. اختر الأسلوب الذي يناسب متطلبات التخطيط لديك.

## **مقدمة**
يُعدّ احتواء صورة بدقة في خلية واحدة متطلبًا شائعًا عند تصميم جداول بيانات تعمل كتقارير بصرية أو كتالوجات منتجات أو أدلة موظفين أو لوحات معلومات أو قوائم جرد. بدلًا من تمديد صورة عبر عدة خلايا أو وضعها بشكل فضفاض على ورقة العمل، قد ترغب في صورة نظيفة مرتبطة بخلية تظل متوائمة مع الخلية التي تحتويها.
يدعم Aspose.Cells هذا السيناريو بطريقتين متكاملتين:
- **الأسلوب 1 — وضع صورة عائمة فوق خلية.** أضف `Picture` إلى ورقة العمل، وعيّن `Placement` إلى `MOVE_AND_SIZE`، واضبط خلايا الربط (`getUpperLeftRow`، و`getUpperLeftColumn`، و`getLowerRightRow`، و`getLowerRightColumn`) بحيث تغطي الصورة خلية واحدة بالضبط.
- **الأسلوب 2 — تضمين صورة مباشرة في خلية.** خصّص وحدات بايت الصورة إلى أداة الضبط `getEmbeddedImage()` للخلية. تتناسب الصورة تلقائيًا مع منطقة عرض الخلية وتنتقل معها.
يتناول بقية هذا المقال كلا الأسلوبين، ويشرح واجهات API المعنية، ويوضح كيفية استخدامها في التعليمات البرمجية.

## **الأسلوب 1: وضع صورة فوق خلية**
الصورة العائمة هي كائن `Picture` يعيش على طبقة الرسم في ورقة العمل. وعلى الرغم من أنها ليست جزءًا من أي خلية واحدة، إلا أنها مرتبطة بنطاق من الخلايا. تحدد خلايا ربط الصورة — الزاويتان العلوية اليسرى والسفلية اليمنى — امتدادها البصري على ورقة العمل. بشكل افتراضي، تمتد الصورة المضافة حديثًا عبر عدة خلايا.
لجعل صورة عائمة تغطي **خلية واحدة بالضبط**، يلزم:
1. إضافة الصورة باستخدام `Worksheet.getPictures().add(int row, int column, InputStream stream)`، والذي يربط الصورة الجديدة بالخلية المحددة.
2. تعيين خصائص الربط الأربع بحيث يتطابق مستطيل الإحاطة الخاص بالصورة مع الخلية المستهدفة.
3. تعيين `Picture.setPlacement()` إلى `PlacementType.MOVE_AND_SIZE` حتى تتحرك الصورة وتُعيد تحجيمها مع الخلية الأساسية عند تغيير عرض العمود أو ارتفاع الصف بواسطة المستخدم.

### **ربط الصورة بخلية واحدة**
يُعرَّف ربط الصورة بأربع خصائص فهرسة تبدأ من الصفر:
- `Picture.getUpperLeftRow()` — فهرس صف الحافة العلوية للصورة.
- `Picture.getUpperLeftColumn()` — فهرس عمود الحافة اليسرى للصورة.
- `Picture.getLowerRightRow()` — فهرس صف الحافة السفلية للصورة. لجعل الحافة السفلية للصورة تقع في أسفل الصف `r`، عيّن هذه القيمة إلى `r + 1`.
- `Picture.getLowerRightColumn()` — فهرس عمود الحافة اليمنى للصورة. لجعل الحافة اليمنى للصورة تقع في يمين العمود `c`، عيّن هذه القيمة إلى `c + 1`.

{{% alert color="primary" %}}
فهارس الصفوف والأعمدة في Aspose.Cells **تبدأ من الصفر**. الخلية C6 لها فهرس صف 5 وفهرس عمود 2. تُعدّ أخطاء الانحراف بمقدار واحد في ربط الزاوية السفلية اليمنى المصدر الأكثر شيوعًا لظهور الصور وكأنها تتداخل مع خلية مجاورة.

### **التحكم في سلوك الموضع**
يُرجع `Picture.getPlacement()` تعدادًا من النوع `PlacementType` يتحكم في كيفية تصرف الصورة عندما يُعيد المستخدم ضبط الصف أو العمود الذي يقع تحتها. القيمة الموصى بها لصورة خلية واحدة هي `PlacementType.MOVE_AND_SIZE`، والتي تتسبب في تحرك الصورة وتغيير حجمها مع الخلية الأساسية، محافظةً على الاحتواء الدقيق.

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح ملفًا موجودًا).
2. يمكنك الوصول إلى `Worksheet` المستهدف من `workbook.getWorksheets().get(0)`.
3. افتح ملف الصورة من القرص في `InputStream` (مثل `FileInputStream`) باستخدام كتلة try-with-resources حتى يُغلق التدفق بشكل صحيح.
4. استدعِ `worksheet.getPictures().add(5, 2, stream)` لإضافة صورة مرتبطة بالخلية C6. احفظ مرجع `Picture` المُرجَع.
5. عيّن إحداثيات الربط الأربع بحيث تغطي الصورة الخلية C6 فقط: `setUpperLeftRow(5)`، و`setUpperLeftColumn(2)`، و`setLowerRightRow(6)`، و`setLowerRightColumn(3)`.
6. عيّن `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` لإبقاء الصورة متوائمة مع C6 عند تغيير حجم العمود أو الصف.
7. اختياريًا، أضف نصًا نموذجيًا إلى الخلايا المحيطة لإثبات أن الخلية C6 فقط هي التي تحتوي على الصورة.
8. احفظ المصنف على القرص كملف `.xlsx`.
تُظهر التعليمات البرمجية التالية الأسلوب الكامل.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **الأسلوب 2: تضمين صورة مباشرة في خلية**
يوفر Aspose.Cells أيضًا آلية أبسط للصور المرتبطة بالخلايا: الطريقة `Cell.setEmbeddedImage(byte[])`. يُلحق تعيين وحدات بايت الصورة بهذه الخاصية الصورة بالخلية نفسها، كما لو كانت محتوى مضمّنًا.

### **كيف تعمل الصور المضمنة**
- تُخزَّن الصورة كجزء من محتوى الخلية وليس كشكل على طبقة الرسم.
- تتناسب الصورة تلقائيًا مع حدود الخلية المعروضة. لا حاجة إلى إحداثيات ربط أو إعدادات موضع.
- تظل الخلية خلية حقيقية بعنوان حقيقي يمكن الإشارة إليه في الصيغ، أو فرزها كجزء من صف، أو استخدامها في عمليات على مستوى الخلية.
يجعل هذا من `setEmbeddedImage()` الخيار الأكثر إيجازًا عندما يكون هدفك ببساطة "صورة تعيش داخل هذه الخلية".

### **إرشادات خطوة بخطوة**
1. أنشئ `Workbook` جديدًا (أو افتح ملفًا موجودًا).
2. يمكنك الوصول إلى `Worksheet` المستهدف من `workbook.getWorksheets().get(0)`.
3. اقرأ ملف الصورة من القرص في مصفوفة `byte[]` (على سبيل المثال، بقراءة الملف عبر `Files.readAllBytes()` من `java.nio.file`).
4. احصل على مرجع إلى الخلية المستهدفة — إما من خلال `worksheet.getCells().get("C6")` أو `worksheet.getCells().get(5, 2)`.
5. خصّص مصفوفة البايتات إلى الخلية باستخدام `cell.setEmbeddedImage(bytes)`.
6. اختياريًا، اضبط ارتفاع الصف وعرض العمود الخاص بالصف والعمود المستهدفين لإعطاء الصورة المضمنة مظهرًا أكثر بروزًا.
7. احفظ المصنف على القرص كملف `.xlsx`.
تُظهر التعليمات البرمجية التالية الأسلوب الكامل.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// الحصول على الخلية المستهدفة C6
Cell cell = worksheet.getCells().get("C6");
// قراءة ملف الصورة في مصفوفة بايتات
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// تضمين الصورة مباشرة في الخلية
cell.setEmbeddedImage(imageData);
// اختيارياً ضبط ارتفاع الصف وعرض العمود لجعل الصورة المضمنة أكثر وضوحاً
worksheet.getCells().setColumnWidth(2, 30);   // العمود C (الفهرس 2)
worksheet.getCells().setRowHeight(5, 100);     // الصف 6 (الفهرس 5)
// حفظ المصنف الناتج كملف .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **اختيار الأسلوب المناسب**
يُنتج كلا الأسلوبين صورة تناسب خلية واحدة، لكنهما يختلفان في كيفية تخزين الصورة وكيفية تصرفها:
- **استخدم صورة عائمة (الأسلوب 1) عند:**
  - حاجتك إلى تحكم أدق في الموضع أو الترتيب الطبقي أو التواؤم مع عناصر الرسم الأخرى.
  - رغبتك في أن تتصرف الصورة كشكل يمكن تحديده أو إعادة ترتيبه أو تجميعه مع أشكال أخرى.
  - حاجتك إلى توافق قديم مع تعليمات برمجية تعمل بالفعل مع `PictureCollection`.
  - حاجتك إلى حساب إحداثيات الربط ديناميكيًا استنادًا إلى تخطيط ورقة العمل.
- **استخدم صورة مضمنة (الأسلوب 2) عند:**
  - رغبتك في أبسط إدراج ممكن لصورة في خلية.
  - ضرورة انتقال الصورة مع الخلية كأي محتوى آخر فيها.
  - عدم حاجتك إلى معالجة الصورة كشكل.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for Java](/cells/ar/java/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Java](/cells/ar/java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Java](/cells/ar/java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ar/java/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Java](/cells/ar/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}