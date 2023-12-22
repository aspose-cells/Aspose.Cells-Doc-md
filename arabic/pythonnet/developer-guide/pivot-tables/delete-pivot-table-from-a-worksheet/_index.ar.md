---
title: حذف الجدول المحوري من ورقة العمل
type: docs
weight: 60
url: /ar/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET كود لإزالة PivotTable لأوراق عمل Excel
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET يوفر ميزة حذف أو إزالة الجدول المحوري من ورقة العمل. يمكنك حذف الجدول المحوري باستخدام كائن الجدول المحوري أو موضع الجدول المحوري. الرجاء استخدام[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) طريقة لحذف الجدول المحوري باستخدام كائن الجدول المحوري و[**Worksheet.pivot_tables.remove_at(index، keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)طريقة لحذف كائن الجدول المحوري باستخدام موضعه داخل مجموعة الجدول المحوري.

{{% /alert %}}

 نموذج التعليمات البرمجية التالي يحذف جدولين محوريين من ورقة العمل. أولاً يقوم بإزالة الجدول المحوري باستخدام[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) الطريقة ثم يقوم بإزالة الجدول المحوري باستخدام[**Worksheet.pivot_tables.remove_at(index، keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) طريقة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
