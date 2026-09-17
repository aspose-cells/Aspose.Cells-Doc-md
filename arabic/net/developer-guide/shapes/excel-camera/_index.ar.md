---
title: كاميرا Excel في Aspose.Cells for .NET
linktitle: كاميرا Excel في Aspose.Cells for .NET
description: تعلّم كيفية استخدام كاميرا Excel في Aspose.Cells for .NET لإنشاء صورة ديناميكية مرتبطة بنطاق خلايا يتم تحديثها مع البيانات المصدر وتحافظ على جميع تنسيقات المصدر.
keywords: Aspose.Cells, .NET, كاميرا Excel, صورة ديناميكية, صورة مرتبطة, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /ar/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

كاميرا Excel هي عنصر في ورقة العمل يعرض صورة حية لنطاق من الخلايا وتطفو على طبقة الرسم كصورة عادية. يدعم Aspose.Cells وضعين للإنشاء، صورة ديناميكية يتم تحديثها تلقائيًا كلما تغيرت البيانات المصدر، وصورة ثابتة تلتقط لقطة فورية واحدة للنطاق. يتناول هذا المقال كلا الأسلوبين حتى تتمكن من اختيار الأنسب لتخطيطك.

## What Is Excel Camera?
كاميرا Excel هي في الأساس كائن صورة مثبت في صف وعمود محددين على طبقة الرسم في ورقة العمل. على عكس الصورة العادية المُدرجة، ترتبط الكاميرا بنطاق مصدر من خلال صيغة بنمط A1 مثل `"A1:F10"`. كلما تغيرت أي خلية داخل هذا النطاق، يتم تحديث صورة الكاميرا تلقائيًا لتعكس المحتوى الجديد. تحافظ الكاميرا على التنسيق الكامل لمنطقة المصدر — الحدود، وألوان الخلفية، والخطوط، وتنسيقات الأرقام — بحيث يظهر كل ما هو مرئي داخل الخلايا داخل صورة الكاميرا أيضًا. هذا يجعل الكاميرا مفيدة بشكل خاص للوحات المعلومات، والملخصات، والأشرطة الجانبية، وتخطيطات التقارير حيث تريد معاينة مرئية لمنطقة بعيدة دون التمرير أو تكرار البيانات. ينطبق تحذيران: يجب عليك استدعاء `UpdateSelectedValue()` قبل حفظ المصنف، وسيتم تصدير الملف إلى HTML أو PDF، لأن هذه التنسيقات تعتمد على بيانات الصورة المضمنة بدلاً من إعادة الحساب المباشر.

## Method 1 — Add a Dynamic Camera Picture
الكاميرا الديناميكية هي الأسلوب الأكثر شيوعًا وهي الأقرب تطابقًا لأداة الكاميرا المدمجة في Excel. تعمل عن طريق إضافة صورة بدون محتوى صورة أولي، ثم تعيين `Formula` لها تشير إلى النطاق المصدر. بعد تعيين الصيغة، يعمل استدعاء `UpdateSelectedValue()` على تحديث بيانات الصورة المضمنة بحيث تتزامن مع الخلايا التي تعكسها. لا يتم تنفيذ الكاميرا من خلال فئة مخصصة — بل تُبنى بالكامل على نوع `Picture` القياسي.
واجهات برمجة التطبيقات الرئيسية هي:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — يضيف صورة مثبتة في الصف والعمود المحددين. يؤدي تمرير `null` لمعامل `stream` إلى إنشاء صورة فارغة تعمل كعنصر نائب للكاميرا الديناميكية. تُرجع الطريقة فهرس الصورة الجديدة.
- `worksheet.Pictures[index]` — وصول مفهرس لاسترداد `Picture` معين من المجموعة.
- `Picture.Formula` — خاصية نصية (get/set) تحمل المرجع بنمط A1 إلى نطاق المصدر الذي تعكسه الكاميرا، مثل `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — طريقة void تُحدّث بيانات الصورة المضمنة من الخلايا المشار إليها بواسطة `Formula`.

{{% alert color="primary" %}}
يجب استدعاء `UpdateSelectedValue()` قبل الحفظ عندما يكون الناتج HTML أو PDF؛ وإلا فلن يحتوي الملف المُصدَّر على بيانات الصورة وستظهر الكاميرا فارغة في الناتج المُقدَّم.
{{% /alert %}}

ينشئ الكود التالي مصنفًا، ويضيف صورة فارغة مثبتة في الصف 10 والعمود 6، ويربطها بنطاق المصدر `A1:F10` من خلال خاصية `Formula`، ويحدّث بيانات الصورة المضمنة، ويحفظ المصنف.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Method 2 — Add a Static Camera Picture
الكاميرا الثابتة هي في الأساس معاينة مُقدَّمة لمرة واحدة لنطاق من الخلايا. بدلاً من الحفاظ على رابط مباشر، تقوم بعرض النطاق إلى بايتات الصورة مرة واحدة، وتغليف هذه البايتات في `MemoryStream`، وإضافتها كصورة عادية. يتم بعد ذلك تثبيت محتوى الصورة وقت الإنشاء ولا يتم تحديثه تلقائيًا عند تغير خلايا المصدر.
واجهات برمجة التطبيقات الرئيسية هي:
- `Cells.CreateRange(string address)` — يبني كائن `Range` من عنوان بنمط A1 مثل `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — يعرض النطاق إلى بايتات الصورة. يؤدي تمرير `null` إلى استخدام خيارات العرض الافتراضية؛ توجد حمولات زائدة للتحكم الدقيق في الناتج.
- `new MemoryStream(byte[] buffer)` — يُغلِّف بايتات الصورة المُقدَّمة في `MemoryStream` يمكن تغذيتها إلى `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — يضيف الصورة مثبتة في الصف والعمود المحددين، وهذه المرة يمرر `MemoryStream` الناتج عن العرض.
ينشئ الكود التالي مصنفًا، ويبني `Range` لـ `A1:F10`، ويعرضه إلى بايتات صورة من خلال `Range.ToImage(null)`، ويُغلِّف البايتات في `MemoryStream`، ويضيف الصورة مثبتة في الصف 10 والعمود 6، ويحفظ المصنف.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choosing Between Dynamic and Static
- **الكاميرا الديناميكية:** يتم تحديثها عند كل إعادة حساب، وتدعم تصدير HTML وPDF بعد `UpdateSelectedValue()`، وتحافظ على سلوك الرابط المباشر طوال عمر الملف.
- **الكاميرا الثابتة:** عرض لمرة واحدة لا يتم تحديثه أبدًا، مفيد عندما تريد لقطة بصرية ثابتة مدمجة في وقت البناء بدلاً من انعكاس مباشر للبيانات.
يدعم Aspose.Cells كلًا من الكاميرا الديناميكية المُحدَّثة تلقائيًا المبنية على `Picture.Formula` بالإضافة إلى `UpdateSelectedValue()`، والكاميرا الثابتة ذات اللقطة الواحدة المبنية على `Range.ToImage` بالإضافة إلى `MemoryStream`. اختر الأسلوب الديناميكي عندما يحتاج الناتج إلى البقاء متزامنًا مع خلايا المصدر، واختر الأسلوب الثابت عندما تحتاج فقط إلى لقطة بصرية ثابتة في وقت البناء.

## Related Articles
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for .NET](/cells/ar/net/convert-sparkline-to-image-and-html/)
- [إدراج صورة في خلية](/cells/ar/net/inserting-an-image-into-a-cell/)
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for .NET](/cells/ar/net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}