---
title: 計算項目を含むピボット テーブルを更新して計算する
type: docs
weight: 40
url: /ja/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: この記事では、Aspose.Cells for Python via .NET の計算項目を含むピボット テーブルを更新して計算する方法を説明します。
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET は、計算項目を含むピボット テーブルの更新と計算をサポートするようになりました。をご利用ください。[**ピボットテーブル.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#)そして[**ピボットテーブルの計算データ**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#)通常どおり、この機能を実行します。

{{% /alert %}}

##  **計算項目を含むピボット テーブルを更新して計算する**

次のサンプルコードは、[ソースエクセルファイル](5115238.xlsx)これには、「add」、「div」、「div2」などの 3 つの計算項目を含むピボット テーブルが含まれています。まずセル D2 の値を 20 に変更し、次に Aspose.Cells for Python via .NET API を使用してピボット テーブルを更新および計算し、ワークブックを PDF 形式で保存します。の結果は、[出力PDF](5115229.pdf) Aspose.Cells for Python via .NET が、計算項目を含むピボット テーブルを正常に更新および計算したことを示しています。 Excel Microsoft を使用して確認するには、セル D2 に値 20 を手動で入力し、Alt+F5 ショートカット キーを使用するか、ピボット テーブルの [更新] ボタンをクリックしてピボット テーブルを更新します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
