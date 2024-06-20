---
title: نسخ بيانات النطاق فقط
type: docs
weight: 330
url: /ar/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

أحيانًا، قد تحتاج إلى نسخ البيانات من نطاق خلايا إلى آخر، مع نسخ البيانات فقط، وليس التنسيق. تقدم Aspose.Cells هذه الميزة عن طريق توفير طريقة Range.copyData.

{{% /alert %}} 
## **نسخ بيانات النطاق فقط**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إنشاء نطاق.
1. إنشاء كائن نمط مع سمات تنسيق محددة.
1. تطبيق تنسيق النمط على النطاق.
1. إنشاء نطاق آخر من الخلايا.
1. نسخ بيانات النطاق الأول إلى هذا النطاق الثاني باستخدام طريقة Range.copyData.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
