---
title: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 40
url: /ja/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++は、計算項目を持つピボットテーブルの刷新と計算をサポートします。従って、通常通り [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) と [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--)を使ってこの機能を実行してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

次のサンプルコードは、[ソースExcelファイル](5115238.xlsx)をロードします。このファイルは、"add"、"div"、"div2"などの3つの計算項目を持つピボットテーブルを含みます。最初にセルD2の値を20に変更し、その後Aspose.Cells for Node.js via C++ APIを使ってピボットテーブルを更新・計算し、ワークブックをPDF形式で保存します。結果として、[出力PDF](5115229.pdf)は、Aspose.Cells for Node.js via C++が計算項目を持つピボットテーブルを正しく更新・計算したことを示しています。この操作をMicrosoft Excelで手動で行い、セルD2に20を入力してピボットテーブルを更新（Alt+F5キーまたはリフレッシュボタンをクリック）して検証できます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
