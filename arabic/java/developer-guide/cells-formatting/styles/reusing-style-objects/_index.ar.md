---
title: إعادة استخدام كائنات النمط
type: docs
weight: 60
url: /ar/java/reusing-style-objects/
---
{{% alert color="primary" %}}

يمكن أن تؤدي إعادة استخدام كائنات النمط إلى توفير الذاكرة وجعل تنفيذ البرنامج أسرع.

{{% /alert %}}

لتطبيق بعض التنسيقات على نطاق كبير من الخلايا في ورقة عمل:

1. قم بإنشاء كائن نمط.
1. حدد السمات.
1. قم بتطبيق النمط على الخلايا الموجودة في النطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

يمكن أيضًا إنجاز نفس العملية التي تمت مناقشتها أعلاه على النحو التالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 بسبب ال[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) و[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) ) الأساليب التي تستخدم ذاكرة أقل بكثير وهي فعالة ، أقدم*Cell.getStyle ()* تمت إزالة الخاصية التي استهلكت الكثير من الذاكرة غير الضرورية مع إصدار*Aspose.Cells 7.1.0*.

{{% /alert %}}
