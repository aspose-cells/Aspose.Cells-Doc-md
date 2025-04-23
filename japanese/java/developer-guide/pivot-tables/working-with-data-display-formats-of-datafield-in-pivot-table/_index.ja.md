---
title: ピボットテーブルでのデータフィールドの表示形式を操作する
type: docs
weight: 150
url: /ja/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cellsは、データフィールドのすべての表示形式をサポートしています。

{{% /alert %}}

## **「最小から最大への順位付け」と「最大から最小への順位付け」表示形式オプション**

Aspose.Cells は、ピボットフィールドの表示形式オプションを設定する機能を提供しています。このために、API は [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) プロパティを提供します。最大から最小へのランクを行うには、[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) プロパティを [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST) に設定できます。次のコードスニペットは、表示形式オプションを設定する方法を示しています。

サンプルソースと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[ソースエクセルファイル](PivotTableSample.xlsx)

[出力エクセルファイル](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
