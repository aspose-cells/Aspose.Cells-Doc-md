---
title: データ範囲とスパークライングループの位置を指定してスパークラインをコピーする
type: docs
weight: 300
url: /ja/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excelは、スパークラインのデータ範囲と位置を指定してコピーすることを可能にします。Aspose.Cells for Python via .NETは、この機能をサポートしています。

{{% /alert %}}

Microsoft Excelでスパークラインを他のセルにコピーするには:

1. スパークラインを含むセルを選択します。
1. **デザイン**タブの**スパークライン**セクションから**データの編集**を選択します。
1. **グループの位置とデータの編集**を選択します。
1. データ範囲と位置を指定します。
1. **OK** をクリックします。

Aspose.Cells for Python via .NETは、SparklineCollection.Add(dataRange, row, column)メソッドを提供して、スパークラインのデータ範囲と位置を指定できます。次のサンプルコードは、上のスクリーンショットのように、ソースExcelファイルを読み込み、最初のスパークライングループにアクセスし、データ範囲と位置を追加します。最後に、出力Excelファイルをディスクに書き込みます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

