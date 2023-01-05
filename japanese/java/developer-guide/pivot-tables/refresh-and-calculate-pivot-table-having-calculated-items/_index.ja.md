---
title: 計算項目を含むピボット テーブルの更新と計算
type: docs
weight: 130
url: /ja/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells は、計算項目を持つピボット テーブルの更新と計算をサポートするようになりました。使ってください[**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ） と[**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) 通常どおり、この機能を実行します。

{{% /alert %}}

## **計算項目を含むピボット テーブルの更新と計算**

次のサンプル コードは、[ソースエクセルファイル](5473428.xlsx)「add」、「div」、「div2」などの 3 つの計算項目を持つピボット テーブルが含まれています。最初にセル D2 の値を 20 に変更し、Aspose.Cells API を使用してピボット テーブルを更新して計算し、ワークブックを PDF 形式で保存します。での結果[出力 PDF](5473431.pdf)Aspose.Cells が、計算項目を含むピボット テーブルを更新して計算したことを示しています。 Microsoft Excel を使用してセル D2 に値 20 を手動で入力し、Alt+F5 ショートカット キーを使用してピボット テーブルを更新するか、ピボット テーブルの [更新] ボタンをクリックして確認できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
