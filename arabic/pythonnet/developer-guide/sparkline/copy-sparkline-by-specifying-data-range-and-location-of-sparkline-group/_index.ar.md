---
title: نسخة الشرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط
type: docs
weight: 300
url: /ar/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

يسمح إكسل من ميكروسوفت بنسخ سباركلين بواسطة تحديد نطاق البيانات وموقع مجموعة السباركلين. يدعم Aspose.Cells لبايثون via .NET هذه الميزة.

{{% /alert %}}

لنسخ الشرارة إلى خلايا أخرى في Microsoft Excel:

1. حدد الخلية التي تحتوي على الشرارة.
1. حدد **Edit Data** من **قسم Sparkline** من **tDesign** علامة التبويب.
1. حدد **Edit Group Location & Data**.
1. حدد نطاق البيانات والموقع.
1. انقر على **موافق**.

يوفر Aspose.Cells لبايثون via .NET طريقة SparklineCollection.Add(dataRange, row, column) لتحديد نطاق البيانات وموقع مجموعة السباركلين. يعرض رمز العينة التالي تحميل ملف إكسل المصدر كما هو موضح في لقطة الشاشة أعلاه، ثم الوصول إلى أول مجموعة سباركلين وإضافة نطاقات البيانات والمواقع في المجموعة. وأخيراً، يكتب ملف إكسل الناتج على القرص والذي يظهر أيضًا في لقطة الشاشة أعلاه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
