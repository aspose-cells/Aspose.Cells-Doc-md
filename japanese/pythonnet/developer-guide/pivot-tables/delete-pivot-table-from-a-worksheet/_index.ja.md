---
title: ワークシートからのピボットテーブルの削除
type: docs
weight: 60
url: /ja/python-net/delete-pivot-table-from-a-worksheet/
description: ExcelワークシートのPivotTableを削除するPython via .NETのコード
keywords: Aspose.Cells for Python Excel、Excel Pythonライブラリ、Python via .NETワークシートからPivotTableを削除する方法、Python via .NETワークシートからPivotTableを削除する方法、Python via .NETでPivotTableを削除する方法、Python via .NETでPivotTableを削除する、PivotTableを削除する方法、PivotTableを削除する、PivotTableの削除、PivotTableの削除方法
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETでは、ワークシートからPivot Tableを削除または削除する機能が提供されます。ピボットテーブルオブジェクトまたはピボットテーブルの位置を使用してピボットテーブルを削除できます。ピボットテーブルオブジェクトを使用してピボットテーブルを削除するには[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)メソッドを使用し、ピボットテーブルのポジションでピボットテーブルオブジェクトを削除するには[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)メソッドを使用してください。

{{% /alert %}}

## **Aspose.Cells for Python Excelライブラリを使用したワークシートからピボットテーブルを削除する方法**

次のサンプルコードでは、ワークシートから2つのピボットテーブルを削除する方法が示されています。最初に[**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/)メソッドを使用してピボットテーブルを削除し、次に[**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)メソッドを使用してピボットテーブルを削除します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
