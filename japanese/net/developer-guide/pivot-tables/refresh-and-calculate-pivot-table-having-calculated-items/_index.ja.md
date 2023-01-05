---
title: 計算項目を含むピボット テーブルの更新と計算
type: docs
weight: 40
url: /ja/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells は、計算項目を持つピボット テーブルの更新と計算をサポートするようになりました。をご利用ください[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata)と[**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata)通常どおり、この機能を実行します。

{{% /alert %}}

## **計算項目を含むピボット テーブルの更新と計算**

次のサンプル コードは、[ソースエクセルファイル](5115238.xlsx)「add」、「div」、「div2」などの 3 つの計算項目を持つピボット テーブルが含まれています。最初にセル D2 の値を 20 に変更し、Aspose.Cells API を使用してピボット テーブルを更新して計算し、ワークブックを PDF 形式で保存します。での結果[出力 PDF](5115229.pdf)Aspose.Cells が、計算項目を含むピボット テーブルを更新して計算したことを示しています。 Microsoft Excel を使用してセル D2 に値 20 を手動で入力し、Alt+F5 ショートカット キーを使用してピボット テーブルを更新するか、ピボット テーブルの [更新] ボタンをクリックして確認できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
