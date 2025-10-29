---
title: تطبيق subtotal وتغيير اتجاه صفوف الملخص التوضيحي أدناه التفاصيل باستخدام جولانج عبر C++
linktitle: تطبيق الإجمالي الجزئي وتغيير اتجاه الصفوف الجملية تحت البيانات الدقيقة
type: docs
weight: 100
url: /ar/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: تعلم كيفية تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط أدناه التفاصيل باستخدام API رقم Aspose.Cells for C++.
keywords: تطبيق الإجمالي الجزئي، إضافة الإجمالي الجزئي، تغيير اتجاه صفوف الملخص الإطاري أدناه، تغيير اتجاه أعمدة الملخص الإطاري إلى اليمين من التفاصيل، إنشاء الإجمالي الجزئي وتغيير اتجاه صفوف الملخص التفصيلي.
---

{{% alert color="primary" %}}

 ستشرح هذه المقالة كيفية تطبيق الإجمالي الفرعي على البيانات وتغيير اتجاه صفوف ملخص المخطط أدناه التفاصيل.

 يمكنك تطبيق الإجمالي الفرعي على البيانات باستخدام طريقة [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/). وتقبل المعلمات التالية:

- **منطقة الخلية** - النطاق الذي سيتم تطبيق الإجمالي عليه
- **التجميع حسب** - الحقل الذي يتم التجميع حسبه، كتعويض صفري مبني
- **الوظيفة** - الوظيفة الإجمالي
- **قائمة الإجمالي** - مصفوفة من الحقول المبنية على التعويض الصفري، تشير إلى الحقول التي يتم إضافة الإجمالي لها
- **استبدال** - يشير إلى ما إذا كنت ترغب في استبدال الإجمالي الفرعي الحالي
- **فواصل الصفحة** - يشير إلى ما إذا كنت ستضيف فاصل صفحة بين المجموعات
- **ملخص أدناه البيانات** - يشير إلى ما إذا كنت ستضيف ملخصًا أسفل البيانات.

أيضًا، يمكنك التحكم في اتجاه **ملخص الصفوف أسفل التفاصيل** للمخطط باستخدام خاصية `Worksheet.Outline.SummaryRowBelow`. يمكنك فتح إعدادات هذا في Microsoft Excel باستخدام **البيانات > المخطط > الإعدادات**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## صور ملفات المصدر والإخراج

تظهر اللقطة الشاشية التالية ملف Excel الأصلي المستخدم في الشفرة المثالية أدناه والذي يحتوي على بعض البيانات في الأعمدة A و B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تظهر اللقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود النموذجي. كما ترون، تم تطبيق الإجمالي إلى النطاق A2:B11 واتجاه المخطط هو صفوف ملخص أدناه للتفاصيل.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## كود C++ لتطبيق الإجمالي الفرعي وتغيير اتجاه الصفوف الملخصة للمخطط

إليك الشيفرة المثالية لتحقيق الإخراج كما هو موضح أعلاه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
