---
title: نسخ بيانات النطاق فقط مع Golang عبر C++
linktitle: نسخ بيانات النطاق فقط
type: docs
weight: 600
url: /ar/go-cpp/copy-range-data-only/
description: تعلم كيفية نسخ بيانات النطاق فقط بدون التنسيق باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى نسخ البيانات من نطاق خلايا إلى آخر، نسخ البيانات فقط، دون التنسيق. تقدم Aspose.Cells هذه الميزة.

تقدم هذه المقالة كود عينة تستخدم Aspose.Cells لنسخ نطاق البيانات.

{{% /alert %}}

يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إنشاء [**Range**](https://reference.aspose.com/cells/go-cpp/range/).
1. إنشاء [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object باستخدام سمات التنسيق المحددة.
1. تطبيق تنسيق النمط على النطاق.
1. إنشاء نطاق آخر من الخلايا.
1. نسخ بيانات النطاق الأول إلى هذا النطاق الثاني.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataOnly.go" >}}
