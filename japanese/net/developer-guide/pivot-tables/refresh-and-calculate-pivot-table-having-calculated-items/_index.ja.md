---
title: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 40
url: /ja/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cellsは今、計算項目を持つピボットテーブルを更新および計算する機能をサポートしています。この機能を実行するには通常通りに[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata)および[**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata)を使用してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

以下のサンプルコードは、"add"、"div"、"div2"などの3つの計算項目を持つピボットテーブルを含む[ソースエクセルファイル](5115238.xlsx)を読み込みます。最初にセルD2の値を20に変更し、Aspose.CellsのAPIを使用してピボットテーブルを更新および計算し、その結果をPDF形式で保存します。[出力PDF](5115229.pdf)の結果で、Aspose.Cellsが計算項目を持つピボットテーブルを成功裏に更新および計算したことが示されています。手動でセルD2に値20を入力し、Alt+F5ショートカットキーを使用するか、ピボットテーブルの更新ボタンをクリックしてMicrosoft Excelで検証できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
