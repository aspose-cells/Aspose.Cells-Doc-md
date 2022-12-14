---
title: تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل
type: docs
weight: 100
url: /ar/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

تشرح هذه المقالة كيفية تطبيق Subtotal على البيانات وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل.

 يمكنك تطبيق Subtotal على البيانات باستخدام[**ورقة العمل Cells المجموع الفرعي ()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) طريقة. يأخذ المعلمات التالية.

- **CellArea** - النطاق المطلوب تطبيق الإجمالي الفرعي عليه
- **مجموعة من** - الحقل المطلوب التجميع حسبه ، كإزاحة عدد صحيح قائم على الصفر
- **دور** - دالة المجموع الفرعي.
- **TotalList** - مصفوفة من إزاحات المجال الصفرية ، تشير إلى الحقول التي تضاف إليها المجاميع الفرعية.
- **يحل محل** - يشير إلى ما إذا كان سيتم استبدال المجاميع الفرعية الحالية
- **فواصل الصفحة** - يشير إلى ما إذا كان سيتم إضافة فاصل صفحة بين المجموعات
- **ملخص البيانات أدناه** - يشير إلى ما إذا كان يجب إضافة ملخص أدناه البيانات.

 أيضًا ، يمكنك التحكم في اتجاه المخطط التفصيلي**صفوف التلخيص أدناه التفاصيل** كما هو موضح في لقطة الشاشة التالية باستخدام خاصية Worksheet.Outline.SummaryRowBelow. يمكنك فتح هذا الإعداد في Microsoft Excel باستخدام**البيانات> المخطط التفصيلي> الإعدادات**

![ما يجب القيام به: image_بديل_نص](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## صور من ملفات المصدر والمخرجات

تُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم في نموذج التعليمات البرمجية أدناه والذي يحتوي على بعض البيانات في العمودين A و B.

![ما يجب القيام به: image_بديل_نص](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تُظهر لقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة نموذج التعليمات البرمجية. كما ترى ، تم تطبيق الإجمالي الفرعي على النطاق A2: B11 واتجاه المخطط التفصيلي هو صفوف التلخيص أدناه بالتفصيل.

![ما يجب القيام به: image_بديل_نص](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# كود لتطبيق المجموع الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي

فيما يلي نموذج التعليمات البرمجية لتحقيق الإخراج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
