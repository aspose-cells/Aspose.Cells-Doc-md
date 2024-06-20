---
title: ピボットテーブルを更新し計算項目を持つピボットテーブルを更新する
type: docs
weight: 40
url: /ja/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: この記事では、Aspose.Cells for Python via .NETを使用した計算されたアイテムを持つピボットテーブルの更新および計算方法を示しています。
keywords: Aspose.Cells for Python Excel、Excel Pythonライブラリ、計算されたアイテムを持つピボットテーブルの更新と計算
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、計算されたアイテムを持つピボットテーブルの更新と計算をサポートしています。この機能を実行するには通常通り[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#)と[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#)を使用してください。

{{% /alert %}}

## **計算項目を持つピボットテーブルを更新および計算する**

次のサンプルコードでは、"add"、"div"、"div2"などの3つの計算されたアイテムを持つピボットテーブルを含む[元のExcelファイル](5115238.xlsx)を読み込みます。まず、セルD2の値を20に変更し、Aspose.Cells for Python via .NETのAPIを使用してピボットテーブルを更新および計算し、ワークブックをPDF形式で保存します。その結果得られる[出力PDF](5115229.pdf)は、Aspose.Cells for Python via .NETが計算されたアイテムを持つピボットテーブルを正常に更新および計算したことを示しています。これをMicrosoft Excelで確認するには、手動でセルD2に値20を入力し、Alt+F5ショートカットキーを使用するか、ピボットテーブルの更新ボタンをクリックしてピボットテーブルを更新してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
