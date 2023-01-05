---
title: チャートのカスタマイズ
type: docs
weight: 40
url: /ja/net/customizing-charts/
---
{{% alert color="primary" %}}

## **カスタム グラフの作成**

これまでグラフについて説明してきたとき、標準の書式設定が設定された標準のグラフを見てきました。データ ソースを定義し、いくつかのプロパティを設定するだけで、既定の形式設定でグラフが作成されます。ただし、Aspose.Cells API はカスタム グラフの作成もサポートしており、開発者は独自の形式設定でグラフを作成できます。

開発者は、実行時に Aspose.Cells を使用してカスタム グラフを作成できます。

グラフはデータ系列で構成されています。 Aspose.Cells の各データ系列は、[**シリーズ**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクト[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトはのコレクションとして機能します[**シリーズ**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクト。カスタム グラフを作成する場合、開発者は、さまざまなデータ シリーズにさまざまな種類のグラフを自由に使用できます ([**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)物体）。

以下のコード例は、カスタム グラフを作成する方法を示しています。この例では、最初のデータ系列に縦棒グラフを使用し、2 番目の系列に折れ線グラフを使用します。その結果、折れ線グラフと組み合わせた縦棒グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

現在、Aspose.Cells は、円グラフ、折れ線グラフ、縦棒グラフ、積み上げ縦棒グラフを組み合わせたカスタム グラフのみをサポートしていますが、今後のリリースではさらに多くのグラフがサポートされる予定です。

{{% /alert %}}
