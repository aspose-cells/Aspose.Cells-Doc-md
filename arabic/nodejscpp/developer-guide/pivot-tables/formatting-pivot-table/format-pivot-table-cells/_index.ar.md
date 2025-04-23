---
title: تنسيق خلايا جدول البيانات المحورية
type: docs
weight: 30
url: /ar/nodejs-cpp/format-pivot-table-cells/
description: كيفية تنسيق خلايا جدول Pivot باستخدام Aspose.Cells for Node.js via C++.
keywords: تنسيق خلايا جدول الدوران
---

{{% alert color="primary" %}}

في بعض الأحيان، تريد تنسيق خلايا جدول Pivot. على سبيل المثال، تريد تطبيق لون خلفية على خلايا جدول Pivot. يوفر Aspose.Cells for Node.js via C++ طريقتين [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) و [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-)، يمكن استخدامهما لهذا الغرض.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) تطبق النمط على جدول المحور بأكمله بينما [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) يطبق النمط على خلية واحدة في جدول المحور.

{{% /alert %}}
الشيفرة النموذجية التالية تحمل [ملف Excel النموذجي](pivot_format.xlsx) الذي يحتوي على جدولين محوريين، وتحقق عملية تنسيق جدول المحور بأكمله وتنسيق الخلايا الفردية في جدول المحور.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormatPivotTableCells-1.js" >}}

## مقالات ذات صلة

- [تنسيق جدول الجدول المحوري](/cells/ar/nodejs-cpp/formatting-pivot-table/)
- [العمل مع تنسيقات عرض البيانات لحقل البيانات في الجدول المحوري](/cells/ar/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
