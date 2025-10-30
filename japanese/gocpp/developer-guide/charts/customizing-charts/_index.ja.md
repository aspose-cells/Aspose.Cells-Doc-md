---
title: Golang を使った C++ によるチャートのカスタマイズ
linktitle: チャートのカスタマイズ
description: Aspose.Cells for C++のチャートのカスタマイズ方法について学びます。ガイドは、チャートレイアウトの変更、データ系列の追加・フォーマット、軸の調整、さまざまなフォーマットオプションの適用により、チャートの外観と使いやすさを向上させる方法を説明します。
keywords: Aspose.Cells for C++、チャート作成、カスタマイズ、レイアウト、データ系列、軸、フォーマット、外観、使いやすさ。
type: docs
weight: 40
url: /ja/go-cpp/customizing-charts/
---


## **カスタムチャートの作成**

これまでにチャートについて話す際、標準的な書式設定を持つ標準チャートを見てきました。データソースを定義し、一部のプロパティを設定するだけで、チャートはデフォルトの書式設定で作成されます。しかし、Aspose.Cells APIは、開発者が独自の書式設定を持つチャートを作成できるカスタムチャートの作成もサポートしています。

開発者は、Aspose.Cellsを使用して実行時にカスタムチャートを作成できます。

チャートはデータ系列で構成されます。Aspose.Cellsの各データ系列は[**Series**](https://reference.aspose.com/cells/go-cpp/series/)オブジェクトで表され、 [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)オブジェクトは[**Series**](https://reference.aspose.com/cells/go-cpp/series/)オブジェクトのコレクションとして機能します。カスタムチャートを作成する際、開発者は異なる種類のチャートを異なるデータ系列に使用する自由があります（[**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)オブジェクトで収集されたデータ系列）。

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

現在、Aspose.Cellsはパイチャート、ラインチャート、カラムチャート、およびカラム積み上げチャートを組み合わせたカスタムチャートのみをサポートしていますが、今後のリリースでさらに多くのチャートがサポートされる予定です。

{{% /alert %}}
