---
title: كاميرا Excel في Aspose.Cells for Python via Java
linktitle: كاميرا Excel في Aspose.Cells for Python via Java
description: تعلّم كيفية استخدام كاميرا Excel في Aspose.Cells for Python via Java لإنشاء صورة ديناميكية مرتبطة بنطاق خلايا يتم تحديثها مع البيانات المصدر وتحافظ على جميع تنسيقات المصدر.
keywords: Aspose.Cells, Python via Java, كاميرا Excel, صورة ديناميكية, صورة مرتبطة, Picture.formula, updateSelectedValue, createRange, toImage, byte[] array
type: docs
weight: 90
url: /ar/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

كاميرا Excel هي كائن في ورقة العمل يعرض صورة حية لنطاق من الخلايا وتطفو على طبقة الرسم كصورة عادية. يدعم Aspose.Cells for Python via Java وضعين للإنشاء، صورة ديناميكية يتم تحديثها تلقائيًا عند تغيير البيانات المصدر وصورة ثابتة تلتقط لقطة واحدة للنطاق. تستعرض هذه المقالة كلا الأسلوبين حتى تتمكن من اختيار الأنسب لتخطيطك.

## ما هي كاميرا Excel؟
كاميرا Excel هي في الأساس كائن صورة مثبت على صف وعمود محددين على طبقة الرسم في ورقة العمل. على عكس الصورة العادية المُدرجة، ترتبط الكاميرا بنطاق مصدر من خلال صيغة بنمط A1 مثل `"A1:F10"`. عند تغيير أي خلية داخل هذا النطاق، يتم تحديث صورة الكاميرا تلقائيًا لتعكس المحتوى الجديد. تحافظ الكاميرا على التنسيق الكامل لمنطقة المصدر — الحدود، ألوان الخلفية، الخطوط، وتنسيقات الأرقام — بحيث يظهر كل ما هو مرئي داخل الخلايا داخل صورة الكاميرا أيضًا. هذا يجعل الكاميرا مفيدة بشكل خاص للوحات المعلومات، الملخصات، اللوحات الجانبية، وتخطيطات التقارير حيث تريد معاينة مرئية لمنطقة بعيدة دون التمرير أو تكرار البيانات. هناك ملاحظتان مهمتان: يجب استدعاء `updateSelectedValue()` قبل حفظ المصنف، وسيتم تصدير الملف إلى HTML أو PDF، لأن هذه التنسيقات تعتمد على بيانات الصورة المُضمنة بدلاً من إعادة الحساب الحي.

## الطريقة الأولى — إضافة صورة كاميرا ديناميكية
الكاميرا الديناميكية هي الأسلوب الأكثر شيوعًا وهي الأقرب إلى أداة الكاميرا المدمجة في Excel. تعمل عن طريق إضافة صورة بدون محتوى صورة أولي، ثم تعيين صيغة لها تُشير إلى النطاق المصدر. بعد تعيين الصيغة، يُحدّث استدعاء `updateSelectedValue()` بيانات الصورة المُضمنة بحيث تتزامن مع الخلايا التي تعكسها. لا يتم تنفيذ الكاميرا من خلال فئة مخصصة — بل تُبنى بالكامل على نوع `Picture` القياسي.
واجهات برمجة التطبيقات الأساسية هي:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — تُضيف صورة مثبتة عند الصف والعمود المحددين. تمرير `None` لمعامل `stream` ينشئ صورة فارغة تعمل كعنصر نائب للكاميرا الديناميكية. تُرجع الطريقة فهرس الصورة الجديدة.
- `worksheet.getPictures().get(index)` — أداة وصول لاسترجاع `Picture` محددة من المجموعة.
- `Picture.getFormula()` / `Picture.setFormula()` — الحصول/تعيين مرجع بنمط A1 إلى نطاق المصدر الذي تعكسه الكاميرا، مثل `"A1:F10"`.
- `Picture.updateSelectedValue()` — طريقة بدون قيمة مُرجعة تُحدّث بيانات الصورة المُضمنة من الخلايا المُشار إليها بواسطة الصيغة.

{{% alert color="primary" %}}
يجب استدعاء `updateSelectedValue()` قبل الحفظ عندما يكون الناتج HTML أو PDF؛ وإلا فلن يحتوي الملف المُصدّر على بيانات الصورة وستظهر الكاميرا فارغة في الناتج المعروض.
{{% /alert %}}

ينشئ الكود التالي مصنفًا، ويُضيف صورة فارغة مثبتة عند الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` من خلال طريقة `setFormula`، ويُحدّث بيانات الصورة المُضمنة، ويحفظ المصنف.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# الكاميرا الديناميكية: أضف صورة فارغة، اربطها عبر الصيغة بـ A1:F10، ثم حدّث
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## الطريقة الثانية — إضافة صورة كاميرا ثابتة
الكاميرا الثابتة هي في الأساس معاينة مُصوّرة مرة واحدة لنطاق من الخلايا. بدلاً من الحفاظ على رابط حي، تقوم بتصيير النطاق إلى بايتات صورة مرة واحدة، وتُلف تلك البايتات في `byte[]` array، وتُضيفها كصورة عادية. يتم تثبيت محتوى الصورة عند لحظة الإنشاء ولا يتم تحديثه تلقائيًا عند تغيير خلايا المصدر.
واجهات برمجة التطبيقات الأساسية هي:
- `Cells.createRange(String address)` — تُنشئ كائن `Range` من عنوان بنمط A1 مثل `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — تُصيّر النطاق إلى بايتات صورة. تمرير `None` يستخدم خيارات التصيير الافتراضية؛ توجد حمولات زائدة للتحكم الدقيق في الناتج.
- `byte[] array(byte[] buffer)` — تُلف بايتات الصورة المُصوّرة في `byte[] array` يمكن إدخالها إلى `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — تُضيف الصورة مثبتة عند الصف والعمود المحددين، وهذه المرة تمرير `byte[] array` الناتج عن التصيير.
ينشئ الكود التالي مصنفًا، ويُنشئ `Range` للنطاق `A1:F10`، ويُصيّره إلى بايتات صورة من خلال `Range.toImage(None)`، ويُلف البايتات في `byte[]` array، ويُضيف الصورة مثبتة عند الصف 10 والعمود 6، ويحفظ المصنف.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# الكاميرا الثابتة: بناء النطاق، التحويل إلى بايتات، التفاف في ByteArrayInputStream، الإضافة كصورة
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## الاختيار بين الديناميكي والثابت
- **كاميرا ديناميكية:** يتم تحديثها عند كل إعادة حساب، تدعم تصدير HTML وPDF بعد `updateSelectedValue()`، وتحافظ على سلوك الرابط الحي طوال عمر الملف.
- **كاميرا ثابتة:** تصيير لمرة واحدة لا يتم تحديثها أبدًا، مفيدة عندما تريد لقطة بصرية ثابتة مُضمنة في وقت البناء بدلاً من مرآة حية للبيانات.
يدعم Aspose.Cells for Python via Java كلًا من الكاميرا الديناميكية ذات التحديث التلقائي المبنية على `setFormula` بالإضافة إلى `updateSelectedValue()` والكاميرا الثابتة ذات اللقطة الواحدة المبنية على `toImage` بالإضافة إلى `byte[] array`. اختر الأسلوب الديناميكي عندما يحتاج ناتجك إلى البقاء متزامنًا مع خلايا المصدر، واختر الأسلوب الثابت عندما تحتاج فقط إلى لقطة بصرية ثابتة في وقت البناء.

{{< app/cells/assistant language="python" >}}