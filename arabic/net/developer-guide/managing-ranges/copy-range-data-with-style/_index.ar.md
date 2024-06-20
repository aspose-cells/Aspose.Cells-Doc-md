---
title: نسخ بيانات النطاق مع النمط
type: docs
weight: 610
url: /ar/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[نسخ بيانات النطاق فقط](/cells/ar/net/copy-range-data-only/) شرح كيفية نسخ البيانات من نطاق الخلايا إلى نطاق آخر. عملية معينة، تم تطبيق مجموعة جديدة من الأنماط على الخلايا المنسوخة. يمكن لـ Aspose.Cells أيضًا نسخ النطاق بالكامل مع التنسيق. يشرح هذا المقال كيفية القيام بذلك.

{{% /alert %}}

توفر Aspose.Cells مجموعة من الفصول والأساليب للعمل مع النطاقات، على سبيل المثال، [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)، [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) و [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

هذا المثال:

1. ينشئ دفتر عمل.
1. يملأ عددًا من الخلايا في ورقة العمل الأولى بالبيانات.
1. ينشئ [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. ينشئ [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object مع سمات التنسيق المحددة.
1. يطبق النمط على نطاق البيانات.
1. ينشئ نطاق آخر من الخلايا.
1. ينسخ البيانات مع التنسيق من النطاق الأول إلى النطاق الثاني.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
