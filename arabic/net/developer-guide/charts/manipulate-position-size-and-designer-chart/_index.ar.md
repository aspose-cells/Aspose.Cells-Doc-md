---
title: التعامل مع حجم المركز ومخطط المصمم
description: تعرف على كيفية استخدام Aspose.Cells for .NET للتعامل بشكل فعال مع الموضع والحجم ومخطط التصميم في Microsoft Excel. سيوضح دليلنا كيفية ضبط هذه الخصائص لتحسين التخطيط والتصور.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /ar/net/manipulate-position-size-and-designer-chart/
---
##  **موضع الرسم البياني وحجمه**
 في بعض الأحيان، تريد تغيير موضع أو حجم المخطط الجديد أو الموجود داخل ورقة العمل. Aspose.Cells يوفر[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) الملكية لتحقيق ذلك. يمكنك استخدام خصائصه الفرعية لإعادة حجم المخطط بأخرى جديدة**ارتفاع** و**عرض** أو إعادة وضعه مع الجديد**X** و **Y** الإحداثيات.
###  **التحكم في موضع الرسم البياني وحجمه**
لتغيير موضع المخطط (إحداثيات X وY) أو حجمه (الارتفاع والعرض)، استخدم الخصائص التالية:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

يشرح المثال التالي استخدام واجهات برمجة التطبيقات المذكورة أعلاه، ويقوم بتحميل المصنف الموجود الذي يحتوي على مخطط في ورقة العمل الأولى الخاصة به. ثم يقوم بإعادة حجم المخطط وإعادة وضعه باستخدام Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **التعامل مع مخططات المصمم**
هناك أوقات تحتاج فيها إلى معالجة المخططات أو تعديلها في ملفات قوالب المصمم. Aspose.Cells يدعم بشكل كامل معالجة محتويات وعناصر مخطط المصمم. يمكن الحفاظ على البيانات ومحتويات المخطط وصورة الخلفية والتنسيقات بدقة.
###  **التعامل مع مخططات المصمم في ملفات القالب**
لمعالجة مخططات المصمم في ملفات القالب، استخدم المخطط ذي الصلة API. على سبيل المثال، يمكنك استخدام خاصية Worksheet.Charts للحصول على مجموعة المخططات الموجودة في ملف القالب.
####  **إنشاء مخطط**
يوضح المثال التالي كيفية إنشاء مخطط هرمي. سوف نقوم بمعالجة هذا المخطط في وقت لاحق.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **التلاعب بالرسم البياني**
يوضح المثال التالي كيفية التعامل مع المخطط الموجود. في هذا المثال، نقوم بتعديل المخطط الذي تم إنشاؤه أعلاه. في المخرجات التي تم إنشاؤها، لاحظ أنه تم تعيين تسمية التاريخ لنقطة بيانات واحدة على "المملكة المتحدة، 30 كيلو بايت".



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **التعامل مع مخطط خطي في قالب المصمم**
في هذا المثال، سوف نقوم بمعالجة الرسم البياني الخطي. سنضيف بعض سلاسل البيانات إلى المخطط الحالي ونغير ألوان الخطوط الخاصة بها.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

