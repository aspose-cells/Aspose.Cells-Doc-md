---
title: نسخة الشرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط
type: docs
weight: 300
url: /ar/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

يسمح Microsoft Excel لك بنسخ شرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط. تدعم Aspose.Cells هذه الميزة.

{{% /alert %}}

لنسخ الشرارة إلى خلايا أخرى في Microsoft Excel:

1. حدد الخلية التي تحتوي على الشرارة.
1. حدد **Edit Data** من **قسم Sparkline** من **tDesign** علامة التبويب.
1. حدد **Edit Group Location & Data**.
1. حدد نطاق البيانات والموقع.
1. انقر على **موافق**.

يوفر Aspose.Cells طريقة SparklineCollection.Add(dataRange, row, column) لتحديد نطاق البيانات وموقع مجموعة الشرائط. يقوم الكود النموذجي التالي بتحميل ملف Excel المصدر كما هو مبين في اللقطة المرفقة أعلاه، ثم يصل إلى المجموعة الشرائية الأولى ويضيف نطاقات البيانات والمواقع في مجموعة الشرائط. وأخيرًا، يكتب ملف Excel الناتج على القرص الثابت كما هو مبين أيضًا في اللقطة المرفقة أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
