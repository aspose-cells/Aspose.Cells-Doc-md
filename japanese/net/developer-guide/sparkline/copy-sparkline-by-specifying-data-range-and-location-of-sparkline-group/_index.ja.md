---
title: スパークライン グループのデータ範囲と場所を指定してスパークラインをコピーする
type: docs
weight: 300
url: /ja/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel では、スパークライン グループのデータ範囲と場所を指定して、スパークラインをコピーできます。 Aspose.Cells はこの機能をサポートしています。

{{% /alert %}}

Microsoft Excel でスパークラインを他のセルにコピーするには:

1. スパークラインを含むセルを選択します。
1. 選択する**データの編集**から**スパークライン**のセクション**デザイン**タブ。
1. 選択する**グループの場所とデータの編集**.
1. データの範囲と場所を指定します。
1. クリック**わかった**.

Aspose.Cells は、スパークライン グループのデータ範囲と場所を指定するための SparklineCollection.Add(dataRange, row, column) メソッドを提供します。次のサンプル コードは、上のスクリーンショットに示すようにソース Excel ファイルを読み込み、最初のスパークライン グループにアクセスして、スパークライン グループにデータ範囲と場所を追加します。最後に、上のスクリーンショットにも示されているように、出力 Excel ファイルをディスクに書き込みます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
