---
title: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 130
url: /ja/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cellsは、計算アイテムを持つピボットテーブルのリフレッシュと計算をサポートしています。この機能を実行するには、通常通り[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--)と[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--)を使用してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

以下のサンプルコードは、"add"、"div"、"div2"などの3つの計算アイテムを持つピボットテーブルを含む[ソースExcelファイル](5473428.xlsx)を読み込みます。まず、セル D2 の値を20に変更し、その後、Aspose.CellsのAPIを使用してピボットテーブルをリフレッシュおよび計算し、ワークブックをPDF形式で保存します。[出力PDF](5473431.pdf)の結果は、Aspose.Cellsが計算アイテムを持つピボットテーブルを正常にリフレッシュおよび計算したことを示しています。手動でセルD2に値20を入力し、Alt+F5ショートカットキーを使用するか、ピボットテーブルのリフレッシュボタンをクリックして、Microsoft Excelで検証できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
{{< app/cells/assistant language="java" >}}
