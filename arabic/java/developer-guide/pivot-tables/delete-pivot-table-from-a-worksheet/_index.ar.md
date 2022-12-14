---
title: حذف Pivot Table من ورقة عمل
type: docs
weight: 50
url: /ar/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 يوفر Aspose.Cells خاصية لحذف أو إزالة Pivot Table من ورقة العمل. يمكنك حذف الجدول المحوري باستخدام كائن الجدول المحوري أو موضع الجدول المحوري. الرجاء استخدام[**Worksheet.getPivotTables (). remove ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) ) طريقة لحذف الجدول المحوري باستخدام كائن الجدول المحوري و[**Worksheet.getPivotTables (). removeAt ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)طريقة لحذف كائن جدول محوري باستخدام موضعه داخل مجموعة الجدول المحوري.

{{% /alert %}}

## **مثال**

 نموذج التعليمات البرمجية التالي يحذف جدولين محوريين من ورقة العمل. أولاً ، يزيل الجدول المحوري باستخدام[**Worksheet.getPivotTables (). remove ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) ثم يقوم بإزالة الجدول المحوري باستخدام[**Worksheet.getPivotTables (). removeAt ()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) طريقة

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
