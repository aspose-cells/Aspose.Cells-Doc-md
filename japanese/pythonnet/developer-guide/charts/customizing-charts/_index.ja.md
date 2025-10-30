---
title: チャートのカスタマイズ
description: Aspose.Cells for Python via .NET でチャートのカスタマイズ方法を学びます。ガイドでは、チャートのレイアウトの変更、データ系列の追加とフォーマット、軸の調整、さまざまなフォーマットオプションの適用について説明します。
keywords: Aspose.Cells for Python via .NET、チャート作成、カスタマイズ、レイアウト、データシリーズ、軸、フォーマット、外観、操作性。
type: docs
weight: 40
url: /ja/python-net/customizing-charts/
---


## **カスタムチャートの作成**

これまでチャートについて説明する際、標準のフォーマット設定を持つ標準的なチャートについて見てきました。データソースを定義し、いくつかのプロパティを設定するだけで、チャートはデフォルトのフォーマット設定で作成されます。しかし、Aspose.Cells for Python via .NET APIは、開発者が独自のフォーマット設定でチャートを作成できるカスタムチャートの作成もサポートしています。

開発者は Aspose.Cells for Python via .NET を使用して、実行時にカスタムチャートを作成できます。

チャートはデータシリーズで構成されています。Aspose.Cells for Python via .NET における各データシリーズは [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) オブジェクトで表され、[**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) オブジェクトは [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) オブジェクトのコレクションを表します。カスタムチャートを作成するとき、開発者はさまざまな種類のチャートを異なるデータシリーズ（[**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) オブジェクトに収集）に使用する自由があります。

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

現在、Aspose.Cells for Python via .NET は、パイ、ライン、コラム、コラムスタックチャートの組み合わせのみをサポートしていますが、今後のリリースでより多くのチャートがサポートされる予定です。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
