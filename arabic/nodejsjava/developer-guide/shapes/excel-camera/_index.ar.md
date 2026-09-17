---
title: كاميرا Excel في Aspose.Cells for Node.js via Java
linktitle: كاميرا Excel في Aspose.Cells for Node.js via Java
description: تعرّف على كيفية استخدام كاميرا Excel في Aspose.Cells for Node.js via Java لإنشاء صورة ديناميكية مرتبطة بنطاق خلايا يتم تحديثها مع بيانات المصدر وتحافظ على جميع تنسيقات المصدر.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, كاميرا Excel, صورة ديناميكية, صورة مرتبطة, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /ar/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

كاميرا Excel هي كائن في ورقة العمل يعرض صورة حية لنطاق من الخلايا وتطفو على طبقة الرسم مثل أي صورة عادية. يدعم Aspose.Cells وضعين للإنشاء، صورة ديناميكية يتم تحديثها تلقائيًا كلما تغيرت بيانات المصدر، وصورة ثابتة تلتقط لقطة واحدة للنطاق. تتناول هذه المقالة كلا الأسلوبين حتى تتمكن من اختيار الأنسب لتخطيطك.

## ما هي كاميرا Excel؟
كاميرا Excel هي في الأساس كائن صورة مثبت على صف وعمود محددين على طبقة الرسم في ورقة العمل. وعلى عكس الصورة العادية المُدرجة، ترتبط الكاميرا بنطاق مصدر من خلال صيغة بنمط A1 مثل `"A1:F10"`. كلما تغيرت أي خلية داخل هذا النطاق، يتم تحديث صورة الكاميرا تلقائيًا لتعكس المحتوى الجديد. تحافظ الكاميرا على التنسيق الكامل لمنطقة المصدر — الحدود، وألوان الخلفية، والخطوط، وتنسيقات الأرقام — بحيث يظهر كل ما هو مرئي داخل الخلايا داخل صورة الكاميرا أيضًا. وهذا يجعل الكاميرا مفيدة بشكل خاص في لوحات المعلومات، والملخصات، والأشرطة الجانبية، وتخطيطات التقارير عندما تريد معاينة مرئية لمنطقة بعيدة دون الحاجة إلى التمرير أو تكرار البيانات. هناك ملاحظتان مهمتان: يجب عليك استدعاء `updateSelectedValue()` قبل حفظ المصنف، وسيتم تصدير الملف إلى HTML أو PDF، لأن هذه التنسيقات تعتمد على بيانات الصورة المضمنة بدلاً من إعادة الحساب الحي.

## الطريقة الأولى — إضافة صورة كاميرا ديناميكية
الكاميرا الديناميكية هي الأسلوب الأكثر شيوعًا وهي الأقرب تطابقًا لأداة الكاميرا المدمجة في Excel. تعمل عن طريق إضافة صورة بدون محتوى صورة أولي، ثم تعيين صيغة `Formula` لها تشير إلى نطاق المصدر. بعد تعيين الصيغة، يقوم استدعاء `updateSelectedValue()` بتحديث بيانات الصورة المضمنة بحيث تتزامن مع الخلايا التي تعكسها. لا يتم تنفيذ الكاميرا من خلال فئة مخصصة — بل تُبنى بالكامل على نوع `Picture` القياسي.
واجهات برمجة التطبيقات الرئيسية هي:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — تضيف صورة مثبتة عند الصف والعمود المحددين. يؤدي تمرير `null` لمعامل `stream` إلى إنشاء صورة فارغة تعمل كعنصر نائب للكاميرا الديناميكية. تُرجع الطريقة فهرس الصورة الجديدة.
- `worksheet.getPictures().get(index)` — الوصول عبر الفهرس لاسترجاع `Picture` محدد من المجموعة.
- `Picture.Formula` — خاصية نصية (`getFormula()`/`setFormula()`) تحمل المرجع بنمط A1 لنطاق المصدر الذي تعكسه الكاميرا، مثل `"A1:F10"`.
- `Picture.updateSelectedValue()` — طريقة بدون قيمة إرجاع تُحدّث بيانات الصورة المضمنة من الخلايا التي يشير إليها `Formula`.

{{% alert color="primary" %}}
يجب استدعاء `updateSelectedValue()` قبل الحفظ عندما يكون الناتج HTML أو PDF؛ وإلا فلن يحتوي الملف المُصدّر على بيانات الصورة وستظهر الكاميرا فارغة في الناتج المعروض.
{{% /alert %}}

يُنشئ الكود التالي مصنفًا، ويضيف صورة فارغة مثبتة عند الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` من خلال خاصية `Formula`، ويُحدّث بيانات الصورة المضمنة، ويحفظ المصنف.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// الكاميرا الديناميكية: أضف صورة فارغة، اربطها عبر الصيغة بـ A1:F10، ثم حدّثها
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## الطريقة الثانية — إضافة صورة كاميرا ثابتة
الكاميرا الثابتة هي في الأساس معاينة مُنشأة مرة واحدة لنطاق من الخلايا. وبدلًا من الحفاظ على رابط حي، تقوم بعرض النطاق إلى وحدات بايت للصورة مرة واحدة، وتغليف وحدات البايت هذه في `ByteArrayInputStream`، وإضافتها كصورة عادية. يتم بعد ذلك تثبيت محتوى الصورة عند لحظة الإنشاء ولا يتم تحديثه تلقائيًا عند تغير خلايا المصدر.
واجهات برمجة التطبيقات الرئيسية هي:
- `Cells.createRange(String address)` — تبني كائن `Range` من عنوان بنمط A1 مثل `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — يعرض النطاق إلى وحدات بايت للصورة. يؤدي تمرير `null` إلى استخدام خيارات العرض الافتراضية؛ توجد حمولات زائدة للتحكم الدقيق في الناتج.
- `new ByteArrayInputStream(byte[] buffer)` — يلف وحدات بايت الصورة المعروضة في `ByteArrayInputStream` يمكن تمريرها إلى `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — تضيف الصورة مثبتة عند الصف والعمود المحددين، وتمرر هذه المرة `ByteArrayInputStream` الناتج عن عملية العرض.
يُنشئ الكود التالي مصنفًا، ويُنشئ `Range` للنطاق `A1:F10`، ويعرضه إلى وحدات بايت للصورة من خلال `range.toImage(null)`، ويلف وحدات البايت في `ByteArrayInputStream`، ويضيف الصورة مثبتة عند الصف 10 والعمود 6، ويحفظ المصنف.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// كاميرا ثابتة: بناء Range، تحويله إلى بايتات، تغليفه في ByteArrayInputStream، إضافته كصورة
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## الاختيار بين الديناميكي والثابت
- **الكاميرا الديناميكية:** تُحدّث عند كل إعادة حساب، وتدعم تصدير HTML وPDF بعد `updateSelectedValue()`، وتحافظ على سلوك الرابط الحي طوال عمر الملف.
- **الكاميرا الثابتة:** عرض لمرة واحدة لا يتم تحديثه أبدًا، ومفيد عندما تريد لقطة مرئية ثابتة مضمنة في وقت الإنشاء بدلًا من انعكاس حي للبيانات.
يدعم Aspose.Cells كلًا من الكاميرا الديناميكية المُحدّثة تلقائيًا المبنية على `Picture.Formula` بالإضافة إلى `updateSelectedValue()`، والكاميرا الثابتة ذات اللقطة الواحدة المبنية على `Range.toImage` بالإضافة إلى `ByteArrayInputStream`. اختر الأسلوب الديناميكي عندما يحتاج الناتج إلى البقاء متزامنًا مع خلايا المصدر، واختر الأسلوب الثابت عندما تحتاج فقط إلى لقطة مرئية ثابتة في وقت الإنشاء.

{{< app/cells/assistant language="nodejs-java" >}}