---
title: الحصول على قيمة النص للخلية مع وبدون تنسيق باستخدام Golang عبر C++
linktitle: الحصول على قيمة سلسلة الخلية
type: docs
weight: 240
url: /ar/go-cpp/get-cell-string-value-with-and-without-formatting/
description: تعلم كيفية الحصول على قيمة سلسلة الخلية مع وبدون تنسيق من خلال واجهة برمجة تطبيقات Aspose.Cells for C++.
keywords: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق، الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق، الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
---

{{% alert color="primary" %}}

 يوفر Aspose.Cells طريقة [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) التي يمكن استخدامها للحصول على قيمة النص للخلية مع أو بدون أي تنسيق. لنفترض أن لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض منزلتين عشريتين فقط. ستعرض بعد ذلك كـ 0.01 في Excel. يمكنك استرداد القيم النصية كـ 0.01 و كـ 0.012345 باستخدام الطريقة [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). يأخذ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) كقيمة enum والتي تتضمن القيم التالية:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

يشرح الكود المثال التالي استخدام الطريقة [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
