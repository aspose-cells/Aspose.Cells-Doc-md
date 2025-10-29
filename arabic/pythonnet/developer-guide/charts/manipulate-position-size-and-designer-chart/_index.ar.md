---
title: تلاعب بموقع الرسمة وحجمها وتصميم الرسم البياني
description: تعلم كيفية استخدام Aspose.Cells للبايثون via .NET للتلاعب بشكل فعال بموقع وحجم ومخطط الرسم في Microsoft Excel. سيرينا دليلنا كيفية تعديل هذه الخصائص لتحسين التنسيق والتصور.
keywords: Aspose.Cells للبايثون via .NET، الموقع، الحجم، مخطط المصمم، Microsoft Excel، التخطيط، التصور.
type: docs
weight: 45
url: /ar/python-net/manipulate-position-size-and-designer-chart/
---

## **الموقع والحجم للرسم البياني**
في بعض الأحيان، ترغب في تغيير موضع أو حجم الرسم البياني الجديد أو الحالي داخل ورقة العمل. يوفر Aspose.Cells للبايثون via .NET الخاصية [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) لتحقيق ذلك. يمكنك استخدام خصائصه الفرعية لإعادة حجم الرسم البياني باستخدام ارتفاع وعرض جديدين أو إعادة وضعه باستخدام إحداثيات X و Y الجديدة.
### **التحكم في موقع الرسم البياني وحجمه**
لاستخدام هذه الخصائص وتغيير موقع الرسم البياني (إحداثيات X و Y) أو حجمه (ارتفاع وعرض):

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

الشرح التالي يوضح استخدام تلك الواجهات البرمجية، حيث يحمل ملف عمل موجود يحتوي على رسم بياني في ورقته الأولى. ثم يعيد تحديد حجم وموقع الرسم البياني باستخدام Aspose.Cells للبايثون via .NET.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **تلاعب الرسوم البيانية للمصمم**
هناك أوقات تحتاج فيها إلى التلاعب أو تعديل رسومات بيانية في ملفات قوالب المصمم. يدعم Aspose.Cells للبايثون via .NET تمامًا التلاعب بمحتويات وعناصر الرسومات البيانية للمصمم. يمكن الاحتفاظ بالبيانات، محتويات الرسم، صورة الخلفية، والتنسيقات بدقة.
### **تلاعب الرسوم البيانية لملفات القوالب المصممة**
لتلاعب الرسوم البيانية لملفات القالب المصممة، استخدم واجهة برمجة التطبيق للرسم البياني. على سبيل المثال، يمكنك استخدام خاصية Worksheet.Charts للحصول على مجموعة الرسوم البيانية الحالية في ملف القالب.
#### **إنشاء رسم بياني**
المثال التالي يوضح كيفية إنشاء رسم بياني هرمي. سوف نقوم بتلاعب بهذا الرسم لاحقًا.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **تلاعب الرسم البياني**
المثال التالي يوضح كيفية تلاعب الرسم البياني الحالي. في هذا المثال، نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. في الناتج المولد، لاحظ أن تسمية التاريخ لأحد نقاط البيانات تم تعيينها إلى 'المملكة المتحدة، 30 ألف'.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **تلاعب رسم بياني الخط في القالب المصمم**
في هذا المثال، سنقوم بتلاعب رسم بياني خطي. سنضيف بعض سلاسل البيانات إلى الرسم البياني الحالي وتغيير ألوان خطوطها.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
