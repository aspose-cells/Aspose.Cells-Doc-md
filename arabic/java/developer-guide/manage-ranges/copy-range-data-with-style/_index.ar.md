---
title: نسخ بيانات النطاق بالنمط
type: docs
weight: 340
url: /ar/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[نسخ بيانات النطاق فقط](/cells/ar/java/copy-range-data-only/) شرح كيفية نسخ البيانات من نطاق من الخلايا إلى نطاق آخر. يمكن Aspose.Cells أيضًا نسخ نطاق كامل بالتنسيق. يشرح هذا المقال كيف.

{{% /alert %}} 
## **نسخ بيانات النطاق بالنمط**
يوفر Aspose.Cells مجموعة من الفئات والطرق للعمل مع النطاقات ، على سبيل المثال ،[createRange ()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [النمط](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [تطبيق نمط ()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\))، إلخ.

هذا المثال:

1. يقوم بإنشاء مصنف.
1. يملأ عددًا من الخلايا في ورقة العمل الأولى بالبيانات.
1. يخلق مجموعة.
1. ينشئ كائن نمط بسمات تنسيق محددة.
1. يطبق النمط على نطاق البيانات.
1. ينشئ نطاقًا ثانيًا من الخلايا.
1. ينسخ البيانات بالتنسيق من النطاق الأول إلى النطاق الثاني.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

