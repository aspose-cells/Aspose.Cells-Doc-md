---
title: تنسيق خلايا جدول البيانات المحورية
type: docs
weight: 20
url: /ar/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

أحيانًا، ترغب في تهيئة خلايا الجدول المحوري. على سبيل المثال، ترغب في تطبيق لون خلفية على خلايا الجدول المحوري. توفر Aspose.Cells طريقتين [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) و [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) يمكنك استخدامهما لهذا الغرض.

تطبق الطريقة [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) النمط على الجدول المحوري بأكمله بينما تطبق الطريقة [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) النمط على خلية واحدة من الجدول المحوري.

{{% /alert %}}

الرمز البرمجي العيني يقوم باستخدام لون أزرق فاتح لتنسيق الجدول المحوري بأكمله ثم يقوم بتنسيق صف الجدول الثاني بلون أصفر.

**الجدول المحوري الذي تم إدخاله قبل تنفيذ الرمز**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**الجدول المحوري الناتج بعد تنفيذ الرمز**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
