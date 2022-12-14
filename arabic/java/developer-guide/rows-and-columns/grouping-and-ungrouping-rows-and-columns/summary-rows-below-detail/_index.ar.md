---
title: تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل
type: docs
weight: 100
url: /ar/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

تشرح هذه المقالة كيفية تطبيق Subtotal على البيانات وتغيير اتجاه صفوف ملخص المخطط التفصيلي أسفل التفاصيل.

 يمكنك تطبيق Subtotal على البيانات باستخدام[**ورقة العمل Cells. المجموع الفرعي ()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) طريقة. يأخذ المعلمات التالية.

- **CellArea** - النطاق المطلوب تطبيق الإجمالي الفرعي عليه
- **مجموعة من** - الحقل المطلوب التجميع حسبه ، كإزاحة عدد صحيح قائم على الصفر
- **دور** - دالة المجموع الفرعي.
- **TotalList** - مصفوفة من إزاحات المجال الصفرية ، تشير إلى الحقول التي تضاف إليها المجاميع الفرعية.
- **يحل محل** - يشير إلى ما إذا كان سيتم استبدال المجاميع الفرعية الحالية
- **فواصل الصفحة** - يشير إلى ما إذا كان سيتم إضافة فاصل صفحة بين المجموعات
- **ملخص البيانات أدناه** - يشير إلى ما إذا كان يجب إضافة ملخص أدناه البيانات.

 أيضًا ، يمكنك التحكم في اتجاه المخطط التفصيلي**صفوف التلخيص أدناه التفاصيل** كما هو موضح في لقطة الشاشة التالية باستخدام[**Worksheet.getOutline (). SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) منشأه. يمكنك فتح هذا الإعداد في Microsoft Excel باستخدام**البيانات> المخطط التفصيلي> الإعدادات**

![ما يجب القيام به: image_بديل_نص](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## مثال

### لقطات تقارن بين ملفات المصدر والمخرجات

تُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم في نموذج التعليمات البرمجية أدناه والذي يحتوي على بعض البيانات في العمودين A و B.

![ما يجب القيام به: image_بديل_نص](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تُظهر لقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة نموذج التعليمات البرمجية. كما ترى ، تم تطبيق المجموع الفرعي على النطاق**أ 2: ب 11** واتجاه المخطط التفصيلي هو صفوف التلخيص أدناه التفاصيل.

![ما يجب القيام به: image_بديل_نص](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java كود لتطبيق المجموع الفرعي وتغيير اتجاه صفوف تلخيص المخطط التفصيلي أدناه بالتفصيل

فيما يلي نموذج التعليمات البرمجية لتحقيق الإخراج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
