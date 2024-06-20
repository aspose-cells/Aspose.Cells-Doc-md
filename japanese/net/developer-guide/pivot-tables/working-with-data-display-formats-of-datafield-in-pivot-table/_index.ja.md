---
title: ピボットテーブルでのデータフィールドの表示形式を操作する
type: docs
weight: 140
url: /ja/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cellsは、データフィールドのすべての表示形式をサポートしています。

{{% /alert %}}

## **「最小から最大への順位付け」と「最大から最小への順位付け」表示形式オプション**

ASpose.Cellsは、ピボットフィールドの表示形式オプションを設定する機能を提供しています。このためのAPIは[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/properties/datadisplayformat)プロパティを提供しています。最大から最小への順位付けを行うには、[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/properties/datadisplayformat)プロパティを[**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat)に設定できます。次のコードスニペットは、表示形式オプションの設定方法を示しています。

サンプルソースと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[ソースExcelファイル](101089332.xlsx)

[出力Excelファイル](101089333.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
