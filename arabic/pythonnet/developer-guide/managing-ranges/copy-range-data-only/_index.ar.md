---
title: نسخ بيانات النطاق فقط
type: docs
weight: 600
url: /ar/python-net/copy-range-data-only/
description: يصف هذا المقال كيفية نسخ مجموعة بيانات فقط باستخدام مكتبة Aspose.Cells لـ Python via .NET.
keywords: مكتبة Python Excel ، Python كيفية نسخ مجموعة البيانات فقط ، Python كيفية نسخ مجموعة البيانات فقط بمكتبة الإكسل الخاصة ببيثون.
---

{{% alert color="primary" %}}

في بعض الأحيان ، قد تحتاج إلى نسخ البيانات من نطاق خلايا إلى آخر ، مع نسخ البيانات فقط وليس النسق. تُقدم Aspose.Cells لـ Python via .NET هذه الميزة.

يقدم هذا المقال رمزًا عينيًا يستخدم Aspose.Cells لـ Python via .NET لنسخ مجموعة من البيانات.

{{% /alert %}}

يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إنشاء [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. إنشاء [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object باستخدام سمات التنسيق المحددة.
1. تطبيق تنسيق النمط على النطاق.
1. إنشاء نطاق آخر من الخلايا.
1. نسخ بيانات النطاق الأول إلى هذا النطاق الثاني.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataOnly-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
