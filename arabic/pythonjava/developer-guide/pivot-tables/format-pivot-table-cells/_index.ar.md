---
title: تنسيق الجدول المحوري Cells
type: docs
weight: 20
url: /ar/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تريد تنسيق خلايا الجدول المحوري. على سبيل المثال ، تريد تطبيق لون الخلفية على خلايا الجدول المحوري. يوفر Aspose.Cells طريقتين[**PivotTable.formatAll ()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) و[**PivotTable.format ()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) ، والتي يمكنك استخدامها لهذا الغرض.

[**PivotTable.formatAll ()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) يطبق النمط على الجدول المحوري بأكمله أثناء[**PivotTable.format ()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) يطبق النمط على خلية مفردة من الجدول المحوري.

{{% /alert %}}

يقوم نموذج التعليمات البرمجية التالي بتنسيق الجدول المحوري بأكمله بلون أزرق فاتح ثم تنسيق صف الجدول الثاني باللون الأصفر.

**الجدول المحوري للإدخال قبل تنفيذ الكود**

![ما يجب القيام به: image_بديل_نص](format-pivot-table-cells_1.png)

**الجدول المحوري للإخراج بعد تنفيذ الكود**

![ما يجب القيام به: image_بديل_نص](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
