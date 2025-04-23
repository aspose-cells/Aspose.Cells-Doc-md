---
title: حذف جدول الدوران من ورقة العمل
type: docs
weight: 50
url: /ar/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

توفر Aspose.Cells ميزة لحذف أو إزالة جدول محوري من ورقة عمل. يمكنك حذف الجدول المحوري باستخدام كائن الجدول المحوري أو موضع الجدول المحوري. يرجى استخدام الطريقة [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) لحذف الجدول المحوري باستخدام كائن الجدول المحوري و [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-) لحذف كائن جدول محوري باستخدام موضعه داخل مجموعة الجدول المحوري.

{{% /alert %}}

## **مثال**

تقوم الشفرة النموذجية التالية بحذف جدولي محوريين من ورقة العمل. أولاً، يزيل الجدول المحوري باستخدام [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) ومن ثم يزيل الجدول المحوري باستخدام [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
