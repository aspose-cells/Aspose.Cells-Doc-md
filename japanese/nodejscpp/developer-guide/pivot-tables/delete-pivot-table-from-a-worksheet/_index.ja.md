---
title: ワークシートからのピボットテーブルの削除
type: docs
weight: 60
url: /ja/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Excelワークシートからピボットテーブルを削除または除去するコード Aspose.Cells for Node.js via C++
keywords: Excel、Excel Node.jsライブラリ、ワークシートからピボットテーブルを削除、Excelでピボットテーブルを削除、Aspose.Cells for Node.js via C++を使ったピボットテーブルの削除、ピボットテーブルの削除、Excelからピボットテーブルを削除、ピボットテーブルの削除方法、Aspose.Cells for Node.js via C++でピボットテーブルを除去
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++は、ワークシートからピボットテーブルを削除または除去する機能を提供します。ピボットテーブルオブジェクトまたは位置を使用して削除できます。 [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-)メソッドを使用してピボットテーブルオブジェクトから削除し、[**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)メソッドを使用してピボットテーブルコレクション内の位置から削除してください。

{{% /alert %}}

## **Aspose.Cells for Node.js via C++を使ったワークシートからのピボットテーブル削除方法**

次のサンプルコードでは、ワークシートから2つのピボットテーブルを削除する方法が示されています。最初に[**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-)メソッドを使用してピボットテーブルを削除し、次に[**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)メソッドを使用してピボットテーブルを削除します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
