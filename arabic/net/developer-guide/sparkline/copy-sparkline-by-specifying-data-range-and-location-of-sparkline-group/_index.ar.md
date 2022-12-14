---
title: انسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline
type: docs
weight: 300
url: /ar/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft يسمح لك Excel بنسخ خط مؤشر بتحديد نطاق البيانات وموقع مجموعة خط المؤشر. Aspose.Cells يدعم هذه الميزة.

{{% /alert %}}

لنسخ خط مؤشر إلى خلايا أخرى في Microsoft Excel:

1. حدد الخلية التي تحتوي على خط المؤشر.
1.  يختار**تحرير البيانات** من**سباركلاين** قسم من**تصميم** التبويب.
1.  يختار**تحرير موقع المجموعة والبيانات**.
1. حدد نطاق البيانات والموقع.
1.  انقر**نعم**.

يوفر Aspose.Cells طريقة SparklineCollection.Add (نطاق البيانات ، الصف ، العمود) لتحديد نطاق بيانات مجموعة خط المؤشر وموقعها. يقوم نموذج التعليمات البرمجية التالي بتحميل ملف Excel المصدر كما هو موضح في لقطة الشاشة أعلاه ، ثم يصل إلى أول مجموعة خط مؤشر ويضيف نطاقات البيانات والمواقع في مجموعة خط المؤشر. أخيرًا ، يكتب ملف Excel الناتج على القرص والذي يظهر أيضًا في لقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
