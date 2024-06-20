---
title: إعادة استخدام كائنات النمط
type: docs
weight: 60
url: /ar/java/reusing-style-objects/
---

{{% alert color="primary" %}}

يمكن إعادة استخدام كائنات النمط لتوفير الذاكرة وزيادة سرعة تنفيذ البرنامج.

{{% /alert %}}

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

يمكن أيضًا تحقيق نفس العملية كما هو موضح أعلاه على النحو التالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

نظرًا لأن أساليب [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) و [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) تستخدم الكثير من الذاكرة وتكون فعالة، تمت إزالة الخاصية القديمة *Cell.getStyle()* التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار *Aspose.Cells 7.1.0*.

{{% /alert %}}
