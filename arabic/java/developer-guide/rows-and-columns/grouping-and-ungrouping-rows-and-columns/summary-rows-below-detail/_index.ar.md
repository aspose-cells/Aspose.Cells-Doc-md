---
title: تطبيق الإجمالي الجزئي وتغيير اتجاه الصفوف الجملية تحت البيانات الدقيقة
type: docs
weight: 100
url: /ar/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

سيقوم هذا المقال بشرح كيفية تطبيق الإجمالي الجزئي على البيانات وتغيير اتجاه صفوف الملخص التفصيلي.

يمكنك تطبيق الإجمالي الجزئي على البيانات باستخدام الطريقة [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])). تأخذ المعلمات التالية.

- **منطقة الخلية** - النطاق الذي سيتم تطبيق الإجمالي عليه
- **التجميع حسب** - الحقل الذي يتم التجميع حسبه، كتعويض صفري مبني
- **الوظيفة** - الوظيفة الإجمالي
- **قائمة الإجمالي** - مصفوفة من الحقول المبنية على التعويض الصفري، تشير إلى الحقول التي يتم إضافة الإجمالي لها
- **تبديل** - يشير ما إذا كان يجب استبدال الإجمالي الحالي
- **كسر الصفحات** - يشير ما إذا كان يجب إضافة فاصل صفحات بين المجموعات
- **ملخص أدنى البيانات** - يشير ما إذا كان يجب إضافة ملخص أدنى للبيانات.

أيضًا ، يمكنك التحكم في اتجاه الخطوط الإفقية ** الصفوف الإحصائية أدناه التفاصيل ** كما هو موضح في اللقطة الشاشية التالية باستخدام خاصية [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow). يمكنك فتح هذا الإعداد في Microsoft Excel باستخدام ** البيانات > مخطط > الإعدادات **.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## مثال

### لقطات الشاشة التي تقارن بين الملفات الأصلية والناتجة

تظهر اللقطة الشاشية التالية ملف Excel الأصلي المستخدم في الشفرة المثالية أدناه والذي يحتوي على بعض البيانات في الأعمدة A و B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تظهر اللقطة الشاشية التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الشفرة المثالية. كما ترون ، تم تطبيق إجمالي على النطاق ** A2:B11 ** وتوجيه المخطط هو الصفوف الإحصائية أدناه.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### شيفرة جافا لتطبيق الإجمالي وتغيير اتجاه خطوط ملخص الخطوط الأفقية أدناه

إليك الشيفرة المثالية لتحقيق الإخراج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
