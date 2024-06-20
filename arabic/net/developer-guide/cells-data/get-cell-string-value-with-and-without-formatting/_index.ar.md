---
title: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
type: docs
weight: 240
url: /ar/net/get-cell-string-value-with-and-without-formatting/
description: تعلم كيفية الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق، الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق، الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
---

{{% alert color="primary" %}}

توفر Aspose.Cells طريقة [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) التي يمكن استخدامها للحصول على قيمة سلسلة الخلية مع أو بدون أي تنسيق. فمثلاً، إذا كانت لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض رقمين عشريين فقط. وسيتم عرضها على Excel بقيمة 0.01. يمكنك الحصول على القيم السلسلة بكلتا الطريقتين، 0.01 وكما هي، 0.012345 باستخدام الطريقة [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue). تأخذ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) التعداد كمعلمة وتحتوي على القيم التالية

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

يشرح الكود المثال التالي استخدام الطريقة [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
