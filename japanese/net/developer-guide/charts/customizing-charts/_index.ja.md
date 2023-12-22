---
title: グラフのカスタマイズ
description: Aspose.Cells for .NET でグラフをカスタマイズする方法を学びましょう。このガイドでは、グラフのレイアウトを変更し、データ シリーズを追加および書式設定し、軸を調整し、さまざまな書式設定オプションを適用してグラフの外観と使いやすさを向上させる方法を説明します。
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /ja/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **カスタムチャートの作成**

これまでグラフについて説明してきたとき、標準の書式設定を持つ標準グラフを見てきました。データ ソースを定義し、いくつかのプロパティを設定するだけで、デフォルトの形式設定でグラフが作成されます。ただし、Aspose.Cells API は、開発者が独自の形式設定でグラフを作成できるカスタム グラフの作成もサポートしています。

開発者は、Aspose.Cells を使用して実行時にカスタム グラフを作成できます。

チャートはデータ系列で構成されます。 Aspose.Cells の各データ系列は、[**シリーズ**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)一方、反対する[**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトは、次のコレクションとして機能します。[**シリーズ**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクト。カスタム グラフを作成する場合、開発者は、さまざまなデータ シリーズ ([**シリーズコレクション**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)物体）。

以下のコード例は、カスタム グラフの作成方法を示しています。この例では、最初のデータ系列に縦棒グラフを使用し、2 番目のデータ系列に折れ線グラフを使用します。その結果、折れ線グラフと組み合わせた縦棒グラフがワークシートに追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

現在、Aspose.Cells は円グラフ、折れ線グラフ、縦棒グラフ、縦棒積み上げグラフを組み合わせたカスタム グラフのみをサポートしていますが、将来のリリースではさらに多くのグラフがサポートされる予定です。

{{% /alert %}}
