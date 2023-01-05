---
title: スマート マーカーを処理してチャートを生成する
type: docs
weight: 2100
url: /ja/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

Aspose.Cells API は、[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)書式設定と数式がデザイナー スプレッドシートに配置されてから処理されるスマート マーカーを操作するためのクラス[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)クラスを使用して、指定されたスマート マーカーに従ってデータを入力します。スマート マーカーを処理して Excel グラフを作成することもできます。これには、次の手順が必要です。

- デザイナースプレッドシートの作成
- 指定されたデータ ソースに対するデザイナー スプレッドシートの処理
- 入力されたデータに基づくグラフの作成

{{% /alert %}}

## デザイナースプレッドシートの作成

デザイナー スプレッドシートは、Microsoft Excel アプリケーションまたは Aspose.Cells API で作成されたシンプルな Excel ファイルで、視覚的な書式設定、数式、およびスマート マーカーが含まれており、実行時に内容を入力できます。

簡単にするために、Aspose.Cells for .NET API を使用してデザイナー スプレッドシートを作成し、後でデモンストレーションのために動的に作成されたデータ ソースに対して処理します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## 処理デザイナー スプレッドシート

デザイナー スプレッドシートを処理するには、デザイナー スプレッドシートで使用されるスマート マーカーに対応するデータ ソースが必要です。たとえば、DataTable Sales の Year 列を表すスマート マーカー エントリを &=Sales.Year として作成しました。対応する列がデータ ソースで使用できない場合、Aspose.Cells API はその特定のスマート マーカーの処理をスキップし、その結果、特定のスマート マーカーのデータは取り込まれません。

この使用例を示すために、データ ソースをゼロから作成し、前の手順で作成したデザイナー スプレッドシートに対して処理します。ただし、リアルタイムのシナリオでは、データが既に使用可能であり、さらに処理できる可能性があるため、データが既に使用可能である場合は、データ ソースの作成をスキップできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

次のコード スニペットが示すように、スマート マーカーの処理は非常に単純です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

上記のコード スニペットは、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)最初のステップで作成されたクラス。デザイナ スプレッドシート ファイルがディスクまたはメモリ上に既にある場合は、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)既存のデザイナー スプレッドシートをロードしてクラスを作成します。

{{% /alert %}}

## チャートの作成

データが配置されたら、データ ソースに基づいてグラフを作成するだけです。例を単純にするために、[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)これにより、チャートをさらに構成する必要がなくなります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
