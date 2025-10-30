---
title: GolangとC++でスパークラインのデータ範囲とグループの位置を指定してコピー
linktitle: データ範囲と場所を指定してスパークラインをコピー
type: docs
weight: 300
url: /ja/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aspose.Cells for C++を使用して、データ範囲と位置を指定してスパークラインをコピーする方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、データ範囲とスパークライングループの位置を指定してスパークラインをコピーすることができます。Aspose.Cellsでは、この機能をサポートしています。

{{% /alert %}}

Microsoft Excelでスパークラインを他のセルにコピーするには:

1. スパークラインを含むセルを選択します。
1. **デザイン**タブの**スパークライン**セクションから**データの編集**を選択します。
1. **グループの位置とデータの編集**を選択します。
1. データ範囲と位置を指定します。
1. **OK** をクリックします。

Aspose.Cellsは、`SparklineCollection.Add(dataRange, row, column)`メソッドを提供しており、これを使ってスパークラインのデータ範囲と位置を指定できます。以下のサンプルコードは、上のスクリーンショットに示されたソースExcelファイルを読み込み、最初のスパークライングループにアクセスし、データ範囲と位置を追加します。最後に、出力Excelファイルを書き出します（画像も上記のスクリーンショットで示されています）。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
