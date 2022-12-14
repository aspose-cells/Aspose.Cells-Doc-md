---
title: حذف Pivot Table من ورقة عمل
type: docs
weight: 60
url: /ar/net/delete-pivot-table-from-a-worksheet/
description: كود C# لإزالة PivotTable لأوراق عمل Excel
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 يوفر Aspose.Cells خاصية لحذف Pivot Table أو إزالته من ورقة العمل. يمكنك حذف الجدول المحوري باستخدام كائن الجدول المحوري أو موضع الجدول المحوري. الرجاء استخدام[**Worksheet.PivotTables.Remove ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) طريقة لحذف الجدول المحوري باستخدام كائن الجدول المحوري و[**Worksheet.PivotTables.RemoveAt ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) طريقة لحذف كائن الجدول المحوري باستخدام موضعه داخل مجموعة الجدول المحوري.

{{% /alert %}}

 نموذج التعليمات البرمجية التالي يحذف جدولين محوريين من ورقة العمل. أولا يزيل الجدول المحوري باستخدام[**Worksheet.PivotTables.Remove ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) طريقة ثم يزيل الجدول المحوري باستخدام[**Worksheet.PivotTables.RemoveAt ()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) طريقة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
