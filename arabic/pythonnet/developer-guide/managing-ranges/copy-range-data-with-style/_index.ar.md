---
title: نسخ بيانات النطاق مع النمط
type: docs
weight: 610
url: /ar/python-net/copy-range-data-with-style/
description: يصف هذا المقال كيفية نسخ نطاق البيانات مع النمط باستخدام مكتبة Aspose.Cells لـ Python via .NET.
keywords: مكتبة Python Excel ، Python كيفية نسخ بيانات نطاق النمط فقط ، Python كيفية نسخ بيانات نطاق النمط فقط مع مكتبة إكسل بالبايثون.
---

{{% alert color="primary" %}}

[نسخ بيانات النطاق فقط](/cells/ar/python-net/copy-range-data-only/) شرح كيفية نسخ البيانات من نطاق الخلايا إلى نطاق آخر. على وجه الخصوص ، يعالج تطبيق مجموعة جديدة من الأنماط للخلايا المنسوخة. يمكن لـ Aspose.Cells لـ Python via .NET أيضًا نسخ نطاق كامل مع التنسيق. يشرح هذا المقال كيفية ذلك.

{{% /alert %}}

توفر Aspose.Cells لـ Python via .NET مجموعة من الفئات والأساليب للعمل مع النطاقات ، على سبيل المثال ، [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)، [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) و [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

هذا المثال:

1. ينشئ دفتر عمل.
1. يملأ عددًا من الخلايا في ورقة العمل الأولى بالبيانات.
1. ينشئ [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. ينشئ [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object مع سمات التنسيق المحددة.
1. يطبق النمط على نطاق البيانات.
1. ينشئ نطاق آخر من الخلايا.
1. ينسخ البيانات مع التنسيق من النطاق الأول إلى النطاق الثاني.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
