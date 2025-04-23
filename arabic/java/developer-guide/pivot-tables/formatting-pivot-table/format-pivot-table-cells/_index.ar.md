---
title: تنسيق خلايا جدول البيانات المحورية
type: docs
weight: 20
url: /ar/java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

أحيانًا، ترغب في تهيئة خلايا الجدول المحوري. على سبيل المثال، ترغب في تطبيق لون خلفية على خلايا الجدول المحوري. توفر Aspose.Cells طريقتين [**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll-com.aspose.cells.Style-) و [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format-int-int-com.aspose.cells.Style-) يمكنك استخدامهما لهذا الغرض.

تطبق الطريقة [**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll-com.aspose.cells.Style-) النمط على الجدول المحوري بأكمله بينما تطبق الطريقة [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format-int-int-com.aspose.cells.Style-) النمط على خلية واحدة من الجدول المحوري.

{{% /alert %}}

الرمز البرمجي العيني يقوم باستخدام لون أزرق فاتح لتنسيق الجدول المحوري بأكمله ثم يقوم بتنسيق صف الجدول الثاني بلون أصفر.

**الجدول المحوري الذي تم إدخاله قبل تنفيذ الرمز**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**الجدول المحوري الناتج بعد تنفيذ الرمز**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
{{< app/cells/assistant language="java" >}}
