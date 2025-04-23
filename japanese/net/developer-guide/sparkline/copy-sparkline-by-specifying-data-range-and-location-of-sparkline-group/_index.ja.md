---
title: データ範囲とスパークライングループの位置を指定してスパークラインをコピーする
type: docs
weight: 300
url: /ja/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
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

Aspose.Cellsは、SparklineCollection.Add(dataRange, row, column)メソッドを提供し、スパークライングループのデータ範囲と位置を指定します。以下のサンプルコードは、上記のスクリーンショットで示すようにソースのExcelファイルをロードし、最初のスパークライングループにアクセスしてデータ範囲と位置を追加します。最後に、出力のExcelファイルをディスクに書き込みます（これも上記のスクリーンショットで示されています）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
