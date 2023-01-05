---
title: معالجة حجم المركز ومخطط المصمم
type: docs
weight: 45
url: /ar/net/manipulate-position-size-and-designer-chart/
---
## **موضع الرسم البياني وحجمه**
 في بعض الأحيان ، تريد تغيير موضع أو حجم المخطط الجديد أو الموجود داخل ورقة العمل. يوفر Aspose.Cells ملف[رسم بياني](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) خاصية لتحقيق ذلك. يمكنك استخدام خصائصه الفرعية لتغيير حجم المخطط بجديد**ارتفاع** و**العرض** أو إعادة وضعه مع جديد** X ** و**Y ** إحداثيات.
### **التحكم في موضع الرسم البياني وحجمه**
لتغيير موضع الرسم البياني (إحداثيات س ، ص) أو حجمه (ارتفاع ، عرض) ، استخدم هذه الخصائص:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [رسم بياني. مخطط رسم. ارتفاع](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

يوضح المثال التالي استخدام واجهات برمجة التطبيقات أعلاه ، حيث يقوم بتحميل المصنف الحالي الذي يحتوي على مخطط في ورقة العمل الأولى الخاصة به. ثم يقوم بإعادة تحجيم الرسم البياني وإعادة وضعه باستخدام Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **معالجة مخططات المصمم**
هناك أوقات تحتاج فيها إلى معالجة المخططات أو تعديلها في ملفات قالب المصمم. Aspose.Cells يدعم بشكل كامل معالجة محتويات وعناصر مخطط المصمم. يمكن الاحتفاظ بالبيانات ومحتويات المخطط وصورة الخلفية والتنسيقات بدقة.
### **معالجة مخططات المصمم في ملفات القوالب**
لمعالجة مخططات المصمم في ملفات القوالب ، استخدم مخطط API. على سبيل المثال ، يمكنك استخدام الخاصية Worksheet.Charts للحصول على مجموعة المخططات الموجودة في ملف القالب.
#### **إنشاء مخطط**
يوضح المثال التالي كيفية إنشاء مخطط هرمي. سوف نتعامل مع هذا المخطط لاحقًا.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **التلاعب في الرسم البياني**
يوضح المثال التالي كيفية التعامل مع المخطط الحالي. في هذا المثال ، نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. في الإخراج الذي تم إنشاؤه ، لاحظ أنه تم تعيين تسمية التاريخ لنقطة بيانات واحدة على "المملكة المتحدة ، 30 ألف".



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **معالجة مخطط خطي في قالب المصمم**
في هذا المثال ، سنتعامل مع مخطط خطي. سنضيف بعض سلاسل البيانات إلى المخطط الحالي ونغير ألوان خطها.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

