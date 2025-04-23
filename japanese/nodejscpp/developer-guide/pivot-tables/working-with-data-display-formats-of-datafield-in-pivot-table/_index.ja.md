---
title: ピボットテーブルでのデータフィールドの表示形式を操作する
type: docs
weight: 140
url: /ja/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++は、DataFieldのすべてのデータ表示形式をサポートしています。

{{% /alert %}}

## **「最小から最大への順位付け」と「最大から最小への順位付け」表示形式オプション**

ASpose.Cellsは、ピボットフィールドの表示形式オプションを設定する機能を提供しています。このためのAPIは[**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-)プロパティを提供しています。最大から最小への順位付けを行うには、[**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-)プロパティを[**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/)に設定できます。次のコードスニペットは、表示形式オプションの設定方法を示しています。

サンプルソースと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[ソースExcelファイル](101089332.xlsx)

[出力Excelファイル](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

