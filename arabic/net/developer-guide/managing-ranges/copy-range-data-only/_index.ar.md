---
title: نسخ بيانات النطاق فقط
type: docs
weight: 600
url: /ar/net/copy-range-data-only/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى نسخ البيانات من نطاق خلايا إلى آخر، نسخ البيانات فقط، دون التنسيق. تقدم Aspose.Cells هذه الميزة.

تقدم هذه المقالة كود عينة تستخدم Aspose.Cells لنسخ نطاق البيانات.

{{% /alert %}}

يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إنشاء [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. إنشاء [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object باستخدام سمات التنسيق المحددة.
1. تطبيق تنسيق النمط على النطاق.
1. إنشاء نطاق آخر من الخلايا.
1. نسخ بيانات النطاق الأول إلى هذا النطاق الثاني.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
