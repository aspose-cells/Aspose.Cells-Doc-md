---
title: تطبيق الإجمالي الجزئي وتغيير اتجاه الصفوف الجملية تحت البيانات الدقيقة
type: docs
weight: 100
url: /ar/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: تعلم كيفية تطبيق المجموع الفرعي وتغيير اتجاه صفوف الملخص التفصيلية أدناه باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: تطبيق الإجمالي الجزئي، إضافة الإجمالي الجزئي، تغيير اتجاه صفوف الملخص الإطاري أدناه، تغيير اتجاه أعمدة الملخص الإطاري إلى اليمين من التفاصيل، إنشاء الإجمالي الجزئي وتغيير اتجاه صفوف الملخص التفصيلي.
---

{{% alert color="primary" %}}

سيقوم هذا المقال بشرح كيفية تطبيق الإجمالي الجزئي على البيانات وتغيير اتجاه صفوف الملخص التفصيلي.

يمكنك تطبيق الإجمالي الجزئي على البيانات باستخدام الطريقة [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index). تأخذ المعلمات التالية.

- **منطقة الخلية** - النطاق الذي سيتم تطبيق الإجمالي عليه
- **التجميع حسب** - الحقل الذي يتم التجميع حسبه، كتعويض صفري مبني
- **الوظيفة** - الوظيفة الإجمالي
- **قائمة الإجمالي** - مصفوفة من الحقول المبنية على التعويض الصفري، تشير إلى الحقول التي يتم إضافة الإجمالي لها
- **تبديل** - يشير ما إذا كان يجب استبدال الإجمالي الحالي
- **PageBreaks** - يشير إلى ما إذا كان هناك فاصل صفحة بين المجموعات
- **ملخص أدنى البيانات** - يشير ما إذا كان يجب إضافة ملخص أدنى للبيانات.

بالإضافة إلى ذلك، يمكنك التحكم في اتجاه الصفوف المخططة أدناه للملخص كما هو موضح في اللقطة الشاشة التالية باستخدام خاصية Worksheet.Outline.SummaryRowBelow. يمكنك فتح هذا الإعداد في برنامج Microsoft Excel باستخدام Data > Outline > Settings

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## صور ملفات المصدر والإخراج

تظهر اللقطة الشاشية التالية ملف Excel الأصلي المستخدم في الشفرة المثالية أدناه والذي يحتوي على بعض البيانات في الأعمدة A و B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تظهر اللقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود النموذجي. كما ترون، تم تطبيق الإجمالي إلى النطاق A2:B11 واتجاه المخطط هو صفوف ملخص أدناه للتفاصيل.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## كود C# لتطبيق الإجمالي وتغيير اتجاه صفوف مخطط الملخص

إليك الشيفرة المثالية لتحقيق الإخراج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
