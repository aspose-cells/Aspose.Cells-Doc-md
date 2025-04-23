---
title: تلاعب بموقع الرسمة وحجمها وتصميم الرسم البياني
description: تعلم كيفية استخدام Aspose.Cells for .NET بشكل فعال للتحكم في موقع وحجم والرسم البياني في مايكروسوفت إكسل. سيقدم دليلنا كيفية ضبط هذه الخصائص لتحسين التخطيط والتصور.
keywords: Aspose.Cells for .NET، الموقع، الحجم، الرسم البياني المصمم، مايكروسوفت إكسل، التخطيط، التصور.
type: docs
weight: 45
url: /ar/net/manipulate-position-size-and-designer-chart/
---

## **الموقع والحجم للرسم البياني**
في بعض الأحيان، ترغب في تغيير موقع أو حجم الرسم البياني الجديد أو القائم داخل ورقة العمل. يوفر Aspose.Cells الخاصية [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) لتحقيق ذلك. يمكنك استخدام خصائصه الفرعية لإعادة تحجيم الرسم البياني بارتفاع وعرض جديدين أو إعادة توضيبه بإحداثيات **X** و **Y** جديدة.
### **التحكم في موقع الرسم البياني وحجمه**
لاستخدام هذه الخصائص وتغيير موقع الرسم البياني (إحداثيات X و Y) أو حجمه (ارتفاع وعرض):

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

المثال التالي يشرح استخدام الواجهات البرمجية التطبيقية المذكورة أعلاه، حيث يقوم بتحميل دفتر العمل الحالي الذي يحتوي على رسم بياني في ورقة العمل الأولى. ثم يقوم بتغيير حجم وموضع الرسم البياني باستخدام Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **تلاعب الرسوم البيانية للمصمم**
هناك أوقات عندما تحتاج إلى تلاعب أو تعديل الرسوم البيانية في ملفات القوالب المصممة. Aspose.Cells يدعم بشكل كامل تغير محتويات وعناصر الرسم البياني المصممة. يمكن الاحتفاظ بالبيانات ومحتويات الرسم البياني والصورة الخلفية والتنسيقات بدقة.
### **تلاعب الرسوم البيانية لملفات القوالب المصممة**
لتلاعب الرسوم البيانية لملفات القالب المصممة، استخدم واجهة برمجة التطبيق للرسم البياني. على سبيل المثال، يمكنك استخدام خاصية Worksheet.Charts للحصول على مجموعة الرسوم البيانية الحالية في ملف القالب.
#### **إنشاء رسم بياني**
المثال التالي يوضح كيفية إنشاء رسم بياني هرمي. سوف نقوم بتلاعب بهذا الرسم لاحقًا.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **تلاعب الرسم البياني**
المثال التالي يوضح كيفية تلاعب الرسم البياني الحالي. في هذا المثال، نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. في الناتج المولد، لاحظ أن تسمية التاريخ لأحد نقاط البيانات تم تعيينها إلى 'المملكة المتحدة، 30 ألف'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **تلاعب رسم بياني الخط في القالب المصمم**
في هذا المثال، سنقوم بتلاعب رسم بياني خطي. سنضيف بعض سلاسل البيانات إلى الرسم البياني الحالي وتغيير ألوان خطوطها.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
