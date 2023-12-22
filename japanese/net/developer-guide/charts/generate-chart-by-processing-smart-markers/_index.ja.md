---
title: スマートマーカーを処理してチャートを生成
description: Aspose.Cells for .NET を使用してスマート マーカーを使用してグラフを生成する方法について説明します。このガイドでは、スマート マーカーとそのプロパティを処理してグラフの外観と使いやすさを向上させる方法を説明します。
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /ja/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API は、[**ワークブックデザイナー**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)スマート マーカーを操作するためのクラス。書式設定と数式はデザイナー スプレッドシートに配置され、その後で処理されます。[**ワークブックデザイナー**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)指定されたスマート マーカーに従ってデータを埋めるクラス。スマート マーカーを処理して Excel グラフを作成することもできます。これには次の手順が必要です。

- デザイナースプレッドシートの作成
- 指定されたデータ ソースに対してデザイナー スプレッドシートを処理する
- 入力されたデータに基づいたグラフの作成

{{% /alert %}}

## デザイナースプレッドシートの作成

デザイナー スプレッドシートは、視覚的な書式設定、数式、スマート マーカーを含む Microsoft Excel アプリケーションまたは Aspose.Cells API で作成された単純な Excel ファイルで、実行時に内容を入力できます。

わかりやすくするために、Aspose.Cells for .NET API を使用してデザイナー スプレッドシートを作成し、その後、デモンストレーションの目的で動的に作成されたデータ ソースに対してそれを処理します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## 処理デザイナーのスプレッドシート

デザイナー スプレッドシートを処理するには、デザイナー スプレッドシートで使用されるスマート マーカーに対応するデータ ソースが必要です。たとえば、DataTable Sales の Year 列を表すスマート マーカー エントリを &=Sales. Year として作成しました。対応する列がデータ ソースで使用できない場合、Aspose.Cells API はその特定のスマート マーカーの処理をスキップし、その結果、特定のスマート マーカーのデータは入力されません。

この使用例を示すために、データ ソースを最初から作成し、前のステップで作成したデザイナー スプレッドシートに対して処理します。ただし、リアルタイム シナリオでは、さらなる処理にデータがすでに利用可能である可能性があるため、データがすでに利用可能な場合はデータ ソースの作成をスキップできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

次のコード スニペットが示すように、スマート マーカーの処理は非常に簡単です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

上記のコード スニペットは、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)最初のステップで作成したクラス。すでにディスクまたはメモリ上にデザイナー スプレッドシート ファイルがある場合は、次のインスタンスを作成できます。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)既存のデザイナー スプレッドシートをロードしてクラスを作成します。

{{% /alert %}}

## チャートの作成

データを配置したら、あとはデータ ソースに基づいてグラフを作成するだけです。例を単純にするために、次を使用します。[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)これにより、チャートをさらに構成する必要がなくなります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
