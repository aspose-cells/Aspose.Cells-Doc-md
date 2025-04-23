---
title: نسخ بيانات النطاق مع النمط
type: docs
weight: 340
url: /ar/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

شرح كيفية نسخ البيانات من نطاق خلايا إلى نطاق آخر. يمكن ل Aspose.Cells أيضًا نسخ نطاق مع التنسيق بأكمله. يشرح هذا المقال كيفية ذلك.

{{% /alert %}} 
## **نسخ بيانات النطاق بالتنسيق**
توفر Aspose.Cells مجموعة من الفئات والطرق للعمل مع النطاقات، على سبيل المثال، [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-)، [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)، [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-)، وغيرها.

هذا المثال:

1. ينشئ دفتر عمل.
1. يملأ عددًا من الخلايا في ورقة العمل الأولى بالبيانات.
1. إنشاء نطاق.
1. إنشاء كائن نمط مع سمات تنسيق محددة.
1. يطبق النمط على نطاق البيانات.
1. ينشئ نطاق آخر من الخلايا.
1. ينسخ البيانات مع التنسيق من النطاق الأول إلى النطاق الثاني.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

{{< app/cells/assistant language="java" >}}
