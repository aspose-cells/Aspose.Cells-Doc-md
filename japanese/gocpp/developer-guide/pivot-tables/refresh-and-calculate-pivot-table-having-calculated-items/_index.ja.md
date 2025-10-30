---
title: GolangとC++を使用した計算項目を持つピボットテーブルの更新と計算
linktitle: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 40
url: /ja/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aspose.Cellsを使用してGolangとC++で計算項目を持つピボットテーブルを更新および計算
---

{{% alert color="primary" %}}

Aspose.Cellsは今、計算項目を持つピボットテーブルを更新および計算する機能をサポートしています。この機能を実行するには通常通りに[**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/)および[**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)を使用してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

 次のサンプルコードは、3つの計算アイテムを持つピボットテーブルを含むソースExcelファイル（5115238.xlsx）を読み込みます。まずセルD2の値を20に変更し、その後、Aspose.Cells APIを使ってピボットテーブルを更新と計算し、ワークブックをPDF形式で保存します。結果として、[出力PDF](5115229.pdf)には、Aspose.Cellsが計算アイテムを持つピボットテーブルを正しく更新と計算したことが示されています。Microsoft Excelを使って、手動でセルD2に20を入力し、Alt+F5ショートカットキーや、ピボットテーブルの更新ボタンをクリックして更新できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
