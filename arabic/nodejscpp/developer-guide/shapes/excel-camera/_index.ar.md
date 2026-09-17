---
title: كاميرا Excel في Aspose.Cells for Node.js via C++
linktitle: كاميرا Excel في Aspose.Cells for Node.js via C++
description: تعرّف على كيفية استخدام كاميرا Excel في Aspose.Cells for Node.js via C++ لإنشاء صورة ديناميكية مرتبطة بنطاق خلايا تتحدّث مع البيانات المصدر وتحافظ على جميع تنسيقات المصدر.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, كاميرا Excel, صورة ديناميكية, صورة مرتبطة, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /ar/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

كاميرا Excel هي كائن ضمن ورقة العمل يعرض صورة حية لنطاق من الخلايا ويطفو على طبقة الرسم كصورة عادية. يدعم Aspose.Cells وضعي إنشاء، صورة ديناميكية تتحدّث تلقائيًا عند تغيير البيانات المصدر، وصورة ثابتة تلتقط لقطة لمرة واحدة للنطاق. تستعرض هذه المقالة الأسلوبين معًا حتى تتمكن من اختيار الأنسب لتخطيطك.

## ما هي كاميرا Excel؟
تُعدّ كاميرا Excel في جوهرها كائن صورة مُثبَّتًا عند صف وعمود محددين على طبقة الرسم في ورقة العمل. وعلى عكس الصورة المُدرَجة العادية، ترتبط الكاميرا بنطاق مصدر عبر صيغة بنمط A1 مثل `"A1:F10"`. كلما تغيّرت أي خلية داخل ذلك النطاق، تتجدّد صورة الكاميرا تلقائيًا لتعكس المحتوى الجديد. تحافظ الكاميرا على كامل تنسيقات المنطقة المصدر — الحدود، ألوان الخلفية، الخطوط، تنسيقات الأرقام — لذا يظهر كل ما هو مرئي داخل الخلايا داخل صورة الكاميرا أيضًا. وهذا يجعل الكاميرا مفيدة بشكل خاص في لوحات المعلومات، الملخصات، الألواح الجانبية، وتخطيطات التقارير حيث تريد معاينة مرئية لمنطقة بعيدة دون الحاجة إلى التمرير أو تكرار البيانات. هناك ملاحظتان مهمتان: يجب استدعاء `updateSelectedValue()` قبل حفظ المصنف، وسيتم تصدير الملف إلى HTML أو PDF، لأن تلك التنسيقات تعتمد على بيانات الصورة المُضمَّنة بدلاً من إعادة الحساب الحي.

## الطريقة الأولى — إضافة صورة كاميرا ديناميكية
تمثّل الكاميرا الديناميكية الأسلوب الأكثر شيوعًا وهو الأقرب إلى أداة الكاميرا المدمجة في Excel. تعمل عبر إضافة صورة دون محتوى صوروي أولي، ثم تعيين صيغة `Formula` لها تُشير إلى النطاق المصدر. بعد تعيين الصيغة، يقوم استدعاء `updateSelectedValue()` بتحديث بيانات الصورة المُضمَّنة لتكون متزامنة مع الخلايا التي تعكسها. لا تُنفَّذ الكاميرا عبر فئة مخصصة — بل تُبنى بالكامل على النوع القياسي `Picture`.
واجهات API الأساسية هي:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — تُضيف صورة مُثبَّتة عند الصف والعمود المُحدَّدين. يؤدي تمرير `null` إلى معامل `stream` إلى إنشاء صورة فارغة تعمل كعنصر نائب للكاميرا الديناميكية. تُعيد هذه الطريقة فهرس الصورة الجديدة.
- `pictures.get(index)` — تسترجع صورة `Picture` محددة من المجموعة بحسب الفهرس.
- `Picture.formula` — خاصية نصية (get/set) تحمل مرجع نمط A1 للنطاق المصدر الذي تعكسه الكاميرا، مثل `"A1:F10"`.
- `Picture.updateSelectedValue()` — طريقة بلا قيمة مُعادة تُحدِّث بيانات الصورة المُضمَّنة من الخلايا المُشار إليها بواسطة `formula`.

{{% alert color="primary" %}}
يجب استدعاء `updateSelectedValue()` قبل الحفظ عندما يكون الناتج بتنسيق HTML أو PDF؛ وإلا فلن يحتوي الملف المُصدَّر على بيانات الصورة وستظهر الكاميرا فارغة في الناتج المُعالَج.
{{% /alert %}}

ينشئ الكود التالي مصنفًا، ويُضيف صورة فارغة مُثبَّتة عند الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` عبر خاصية `Formula`، ويُحدِّث بيانات الصورة المُضمَّنة، ويحفظ المصنف.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// الكاميرا الديناميكية: أضف صورة فارغة، اربطها عبر الصيغة بـ A1:F10، ثم حدّث
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## الطريقة الثانية — إضافة صورة كاميرا ثابتة
تمثّل الكاميرا الثابتة في جوهرها معاينة مُعالَجة لمرة واحدة لنطاق من الخلايا. وبدلًا من الحفاظ على رابط حي، تقوم بمعالجة النطاق إلى بايتات صورة مرة واحدة، وتُغلِّف تلك البايتات داخل `Buffer`، وتضيفها كصورة عادية. يتحدد محتوى الصورة عند لحظة الإنشاء ولا يتحدّث تلقائيًا عند تغيُّر خلايا المصدر.
واجهات API الأساسية هي:
- `Cells.createRange(address)` — تُنشئ كائن `Range` من عنوان بنمط A1 مثل `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — تُعالِج النطاق إلى بايتات صورة. يؤدي تمرير `null` إلى استخدام خيارات المعالجة الافتراضية؛ تتوفر صيغ أخرى للتحكم أكثر دقة في الناتج.
- `new Buffer(byte[] buffer)` — تُغلِّف بايتات الصورة المُعالَجة داخل `Buffer` يمكن تغذيته إلى `getPictures().add`.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — تُضيف الصورة مُثبَّتة عند الصف والعمود المُحدَّدين، مع تمرير `Buffer` الناتج عن المعالجة هذه المرة.
ينشئ الكود التالي مصنفًا، ويُنشئ `Range` للنطاق `A1:F10`، ويُعالجه إلى بايتات صورة عبر `range.toImage(null)`، ويُغلِّف البايتات داخل `Buffer`، ويُضيف الصورة مُثبَّتة عند الصف 10 والعمود 6، ويحفظ المصنف.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// الكاميرا الثابتة: إنشاء Range، تحويل إلى بايتات، تغليف في MemoryStream، إضافة كصورة
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## الاختيار بين الديناميكي والثابت
- **الكاميرا الديناميكية:** تتحدّث عند كل إعادة حساب، وتدعم تصدير HTML وPDF بعد `updateSelectedValue()`، وتحافظ على سلوك الربط الحي طوال عمر الملف.
- **الكاميرا الثابتة:** معالجة لمرة واحدة لا تتحدّث أبدًا، وهي مفيدة عندما تحتاج لقطة مرئية ثابتة مُضمَّنة عند البناء بدلًا من مرآة حيّة للبيانات.
يدعم Aspose.Cells كلًا من الكاميرا الديناميكية المُحدَّثة تلقائيًا المبنية على `Picture.formula` مع `updateSelectedValue()`، والكاميرا الثابتة لمرة واحدة المبنية على `Range.toImage` مع `Buffer`. اختر الأسلوب الديناميكي عندما يحتاج ناتجك إلى البقاء متزامنًا مع خلايا المصدر، واختر الأسلوب الثابت عندما تحتاج فقط إلى لقطة مرئية ثابتة عند البناء.

{{< app/cells/assistant language="nodejs-cpp" >}}