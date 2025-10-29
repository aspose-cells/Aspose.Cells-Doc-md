---
title: نسخ السباركلين عن طريق تحديد مدى البيانات وموقع مجموعة السبوركلين باستخدام Golang عبر C++
linktitle: نسخ Sparkline عن طريق تحديد نطاق البيانات والموقع
type: docs
weight: 300
url: /ar/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: تعلم كيفية نسخ sparklines عن طريق تحديد نطاق البيانات والموقع باستخدام Aspose.Cells for C++.
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

يوفر Aspose.Cells طريقة `SparklineCollection.Add(dataRange, row, column)` لتحديد نطاق البيانات وموقع مجموعة Sparkline. يقوم الكود النموذجي التالي بتحميل ملف Excel المصدر كما هو موضح في الصورة أعلاه، ثم يصل إلى أول مجموعة Sparkline ويضيف نطاقات البيانات والمواقع في المجموعة. أخيراً، يكتب ملف Excel الناتج على القرص والذي يظهر أيضًا في الصورة أعلاه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
