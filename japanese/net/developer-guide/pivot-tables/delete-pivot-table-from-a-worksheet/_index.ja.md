---
title: ワークシートからのピボットテーブルの削除
type: docs
weight: 60
url: /ja/net/delete-pivot-table-from-a-worksheet/
description: Excelワークシートのピボットテーブルを削除するためのC#コード
keywords: C#でピボットテーブルをワークシートから削除する, C#でExcelのピボットテーブルを削除する, C#でピボットテーブルを削除する方法, ピボットテーブルを削除するC#, ピボットテーブルをExcelから削除するC#, C#でピボットテーブルを削除, C#でピボットテーブルを削除, ピボットテーブルを削除, ピボットテーブルの削除方法
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークシートからピボットテーブルを削除する機能が提供されています。ピボットテーブルオブジェクトやピボットテーブルの位置を使用して削除できます。

{{% /alert %}}

次のサンプルコードでは、ワークシートから2つのピボットテーブルを削除する方法が示されています。最初に[**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove)メソッドを使用してピボットテーブルを削除し、次に[**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)メソッドを使用してピボットテーブルを削除します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
