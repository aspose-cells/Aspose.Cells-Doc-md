---
title: الحصول على قيمة سلسلة الخلية مع استراتيجية التنسيق
type: docs
weight: 240
url: /ar/python-net/get-cell-string-value-with-format-strategy/
description: تعلم كيفية الحصول على قيمة سلسلة الخلية مع وبدون تنسيق من خلال Aspose.Cells for Python via .NET API.
keywords: مكتبة Excel لـ Python، كيفية الحصول على قيمة سلسلة الخلية مع وبدون تنسيق باستخدام Python، كيفية استرداد قيمة سلسلة الخلية مع وبدون تنسيق باستخدام Python، الحصول على قيمة سلسلة الخلية مع وبدون تنسيق باستخدام Python
---

{{% alert color="primary" %}}

يوفر Aspose.Cells for Python via .NET طريقة [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) يمكن استخدامها للحصول على قيمة السلسلة للخلية مع أو بدون أي تنسيق. مثلاً، إذا كان لديك خلية بقيمة 0.012345 وقمت بتهيئتها لعرض رقمين عشريين فقط، سيتم عرضها كـ 0.01 في Excel. يمكنك الحصول على القيم النصية سواء كـ 0.01 أو كـ 0.012345 باستخدام الطريقة [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/). تأخذ العلامة التجارية [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) كقيمة معلمة ولديها القيم التالية

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

يشرح الكود المثال التالي استخدام الطريقة [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
