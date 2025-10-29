---
title: الحصول على قيمة سلسلة الخلية مع أو بدون تنسيق
type: docs
weight: 240
url: /ar/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: تعلّم كيفية الحصول على قيمة نصية خلوية مع وبدون تنسيق من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: احصل على قيمة النص من الخلية مع وبدون تنسيق Node.js عبر C++، استرجع قيمة النص من الخلية مع وبدون تنسيق Node.js عبر C++، احصل على قيمة النص من الخلية مع وبدون تنسيق Node.js عبر C++
---

{{% alert color="primary" %}}

تقدم Aspose.Cells طريقة [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) التي يمكن استخدامها للحصول على القيمة النصية للخلية مع أو بدون أي تنسيق. على سبيل المثال، لديك خلية بقيمة 0.012345 وقمت بتنسيقها لعرض خانتين عشريتين فقط، فستظهر كـ 0.01 في إكسل. يمكنك استرجاع القيم النصية كـ 0.01 وكـ 0.012345 باستخدام طريقة [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). تأخذ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) كقيمة من نوع enum لديه القيم التالية

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

يوضح رمز المثال التالي استخدام طريقة [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
