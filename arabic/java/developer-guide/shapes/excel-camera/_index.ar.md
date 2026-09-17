---
title: كاميرا إكسل في Aspose.Cells for Java
description: تعلّم كيفية استخدام كاميرا إكسل في Aspose.Cells for Java لإنشاء صورة ديناميكية مرتبطة بنطاق خلايا تتحدّث مع البيانات المصدرية وتحافظ على جميع التنسيقات الأصلية.
linktitle: كاميرا إكسل
keywords: Aspose.Cells, Java, كاميرا إكسل, صورة ديناميكية, صورة مرتبطة, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /ar/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

كاميرا إكسل هي كائن في ورقة العمل يعرض صورة حية لنطاق من الخلايا وتطفو فوق طبقة الرسم مثل أي صورة عادية. يدعم Aspose.Cells وضعَي إنشاء، صورة ديناميكية تتحدّث تلقائيًا عند تغيُّر البيانات المصدرية، وصورة ثابتة تلتقط لقطة فورية للنطاق. تتناول هذه المقالة الطريقتَين لتختار الأنسب لتخطيطك.

## ما هي كاميرا إكسل؟
كاميرا إكسل هي في جوهرها كائن صورة مُثبَّت على صف وعمود محددَين على طبقة الرسم في ورقة العمل. وعلى عكس الصورة المُدرَجة العادية، ترتبط الكاميرا بنطاق مصدر من خلال صيغة بنمط A1 مثل `"A1:F10"`. كلما تغيّرت أي خلية داخل هذا النطاق، تتجدّد صورة الكاميرا تلقائيًا لتعكس المحتوى الجديد. تحافظ الكاميرا على التنسيق الكامل للمنطقة المصدرية، الحدود، ألوان الخلفية، الخطوط، وتنسيقات الأرقام، لذا يظهر كل ما هو مرئي داخل الخلايا داخل صورة الكاميرا أيضًا. وهذا يجعل الكاميرا مفيدة بشكل خاص في لوحات المعلومات، الملخصات، الأشرطة الجانبية، وتخطيطات التقارير حيث تريد معاينة مرئية لمنطقة بعيدة دون الحاجة إلى التمرير أو تكرار البيانات. هناك تحفّظان: يجب استدعاء `updateSelectedValue()` قبل حفظ المصنف، وسيُصدَّر الملف إلى HTML أو PDF، لأن هذه التنسيقات تعتمد على بيانات الصورة المُضمَّنة بدلاً من إعادة الحساب الحي.

## الطريقة الأولى — إضافة صورة كاميرا ديناميكية
الكاميرا الديناميكية هي النهج الأكثر شيوعًا والأقرب إلى أداة الكاميرا المدمجة في إكسل. تعمل عن طريق إضافة صورة بدون محتوى صوروي أوّلي، ثم تعيين صيغة `Formula` لها تُشير إلى النطاق المصدر. بعد تعيين الصيغة، يُحدِّث استدعاء `updateSelectedValue()` بيانات الصورة المُضمَّنة لتكون متزامنة مع الخلايا التي تعكسها. لا تُنفَّذ الكاميرا من خلال فئة مخصصة، بل تُبنى بالكامل على النوع القياسي `Picture`.
واجهات برمجة التطبيقات الأساسية هي:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — تُضيف صورة مُثبَّتة عند الصف والعمود المُحدَّدَين. تمرير `null` للمعامل `stream` ينشئ صورة فارغة تعمل كعنصر نائب لكاميرا ديناميكية. تُعيد هذه الطريقة فهرس الصورة الجديدة.
- `worksheet.getPictures().get(index)` — وصول بواسطة الفهرس لاسترجاع `Picture` محدد من المجموعة.
- `Picture.setFormula(String value)` — تُعيِّن المرجع بنمط A1 إلى النطاق المصدر الذي تعكسه الكاميرا، مثل `"A1:F10"`.
- `Picture.updateSelectedValue()` — طريقة بدون قيمة مُعادة تُحدِّث بيانات الصورة المُضمَّنة من الخلايا المُشار إليها بواسطة `Formula`.

{{% alert color="primary" %}}
يجب استدعاء `updateSelectedValue()` قبل الحفظ عندما يكون الناتج HTML أو PDF، وإلا فلن يحتوي الملف المُصدَّر على بيانات الصورة وستظهر الكاميرا فارغة في الناتج المُنشأ.
{{% /alert %}}

يُنشئ الكود التالي مصنفًا، ويُضيف صورة فارغة مُثبَّتة عند الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` من خلال `setFormula`، ويُحدِّث بيانات الصورة المُضمَّنة، ثم يحفظ المصنف.

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// الكاميرا الديناميكية: أضف صورة فارغة، اربطها عبر الصيغة بـ A1:F10، ثم قم بالتحديث
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## الطريقة الثانية — إضافة صورة كاميرا ثابتة
الكاميرا الثابتة هي في جوهرها معاينة مُنشأة مرة واحدة لنطاق من الخلايا. وبدلًا من الحفاظ على رابط حي، تُحوِّل النطاق إلى وحدات بايت صورة مرة واحدة، وتُغلِّف هذه الوحدات في `ByteArrayInputStream`، ثم تُضيفها كصورة عادية. يكون محتوى الصورة ثابتًا عند لحظة الإنشاء ولا يتجدّد تلقائيًا عند تغيُّر خلايا المصدر.
واجهات برمجة التطبيقات الأساسية هي:
- `Cells.createRange(String address)` — تبني كائن `Range` من عنوان بنمط A1 مثل `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — تُحوِّل النطاق إلى وحدات بايت صورة. تمرير `null` يستخدم خيارات العرض الافتراضية؛ توجد حمولات إضافية للتحكم بشكل أدق في الناتج.
- `new ByteArrayInputStream(byte[] buffer)` — تُغلِّف وحدات بايت الصورة المُنشأة في `ByteArrayInputStream` يمكن تمريرها إلى `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — تُضيف الصورة مُثبَّتة عند الصف والعمود المُحدَّدَين، وتمرِّر هذه المرة `ByteArrayInputStream` الناتج من عملية العرض.
يُنشئ الكود التالي مصنفًا، ويبني `Range` للنطاق `A1:F10`، ويُحوِّله إلى وحدات بايت صورة من خلال `Range.toImage(null)`، ويُغلِّف الوحدات في `ByteArrayInputStream`، ويُضيف الصورة مُثبَّتة عند الصف 10 والعمود 6، ثم يحفظ المصنف.

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// كاميرا ثابتة: بناء Range، تحويل إلى بايتات، تغليف في ByteArrayInputStream، إضافة كصورة
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## الاختيار بين الديناميكية والثابتة
- **الكاميرا الديناميكية:** تتحدّث عند كل إعادة حساب، وتدعم تصدير HTML وPDF بعد `updateSelectedValue()`، وتحافظ على سلوك الرابط الحي طوال عمر الملف.
- **الكاميرا الثابتة:** عرض يحدث مرة واحدة ولا يتحدّث أبدًا، وهي مفيدة عندما تريد لقطة بصرية ثابتة مُضمَّنة وقت البناء بدلاً من مرآة حيّة للبيانات.
يدعم Aspose.Cells كلًا من الكاميرا الديناميكية ذات التحديث التلقائي المبنية على `Picture.Formula` بالإضافة إلى `updateSelectedValue()`، والكاميرا الثابتة أحادية اللقطة المبنية على `Range.toImage` بالإضافة إلى `ByteArrayInputStream`. اختر النهج الديناميكي عندما يحتاج الناتج إلى البقاء متزامنًا مع خلايا المصدر، واختر النهج الثابت عندما تحتاج فقط إلى لقطة بصرية ثابتة وقت البناء.

## مقالات ذات صلة
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Java](/cells/ar/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}