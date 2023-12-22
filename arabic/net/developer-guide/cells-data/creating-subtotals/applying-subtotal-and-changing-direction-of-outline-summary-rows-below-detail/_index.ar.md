---
title: تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل
type: docs
weight: 100
url: /ar/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: تعرف على كيفية تطبيق الإجمالي الفرعي وتغيير اتجاه ملخص المخطط التفصيلي الصفوف أدناه التفاصيل باستخدام Aspose.Cells for .NET API.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

تشرح هذه المقالة كيفية تطبيق الإجمالي الفرعي على البيانات وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل.

 يمكنك تطبيق المجموع الفرعي على البيانات باستخدام[**ورقة عمل.Cells.المجموع الفرعي()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) طريقة. يستغرق المعلمات التالية.

- **منطقة الخلية** - النطاق الذي سيتم تطبيق المجموع الفرعي عليه
- **مجموعة من** - الحقل المراد التجميع حسبه، كإزاحة عدد صحيح قائم على الصفر
- **وظيفة** - الدالة المجموع الفرعي.
- **TotalList** مصفوفة من إزاحات الحقول المستندة إلى الصفر، تشير إلى الحقول التي تتم إضافة الإجماليات الفرعية إليها.
- **يستبدل** - يشير إلى ما إذا كان سيتم استبدال المجاميع الفرعية الحالية
- **فواصل الصفحة** - يشير إلى ما إذا كان سيتم إضافة فاصل الصفحات بين المجموعات
- **ملخص أدناه البيانات** - يشير إلى ما إذا كان سيتم إضافة ملخص أدناه للبيانات.

 كما يمكنك التحكم في اتجاه المخطط التفصيلي**صفوف التلخيص أدناه التفاصيل** كما هو موضح في لقطة الشاشة التالية باستخدام خاصية Worksheet.Outline.SummaryRowBelow. يمكنك فتح هذا الإعداد في Microsoft Excel باستخدام**البيانات > المخطط التفصيلي > الإعدادات**

![ما يجب القيام به:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  صور لملفات المصدر والإخراج

تعرض لقطة الشاشة التالية ملف Excel المصدر المستخدم في نموذج التعليمات البرمجية أدناه والذي يحتوي على بعض البيانات في العمودين A وB.

![ما يجب القيام به:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تعرض لقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة نموذج التعليمات البرمجية. كما ترون، تم تطبيق الإجمالي الفرعي على النطاق A2:B11 واتجاه المخطط التفصيلي هو صفوف التلخيص أسفل التفاصيل.

![ما يجب القيام به:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## كود C# لتطبيق المجموع الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي

إليك نموذج التعليمات البرمجية لتحقيق الإخراج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
