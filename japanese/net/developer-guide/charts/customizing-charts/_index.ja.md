---
title: チャートのカスタマイズ
description: Aspose.Cells for .NETでチャートのカスタマイズ方法を学びます。このガイドでは、チャートのレイアウトの変更、データ系列の追加と書式設定、軸の調整、外観と使いやすさを向上させるためのさまざまな書式設定オプションの適用方法を紹介します。
keywords: Aspose.Cells for .NET、チャート作成、カスタマイズ、レイアウト、データ系列、軸、書式設定、外観、使いやすさ。
type: docs
weight: 40
url: /ja/net/customizing-charts/
---


## **カスタムチャートの作成**

これまでに、標準のフォーマット設定を持つ標準チャートを取り上げてきました。データソースを定義し、いくつかのプロパティを設定するだけで、チャートはそのデフォルトのフォーマット設定で作成されます。ただし、Aspose.Cells APIでは、自分自身のフォーマット設定を持つカスタムチャートを作成することもサポートされています。

開発者は、Aspose.Cellsを使用して実行時にカスタムチャートを作成できます。

チャートはデータ系列で構成されます。Aspose.Cellsの各データ系列は[**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクトで表され、 [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトは[**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)オブジェクトのコレクションとして機能します。カスタムチャートを作成する際、開発者は異なる種類のチャートを異なるデータ系列に使用する自由があります（[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)オブジェクトで収集されたデータ系列）。

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

現在、Aspose.Cellsでは、パイチャート、折れ線グラフ、列グラフ、列積み上げグラフを組み合わせたカスタムチャートのみがサポートされていますが、将来のリリースでさらに多くのチャートがサポートされる予定です。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
