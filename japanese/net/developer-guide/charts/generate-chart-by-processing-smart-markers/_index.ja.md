---
title: スマートマーカーの処理によるチャートの生成
description: Aspose.Cells for .NETを使用してスマートマーカーを処理してグラフを生成する方法を学んでください。当社のガイドでは、スマートマーカーとそのプロパティを処理して、グラフの外観と使いやすさを向上させる方法を示します。
keywords: Aspose.Cells for .NET、チャート生成、スマートマーカー、外観、使いやすさ、処理。
type: docs
weight: 2100
url: /ja/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Aspose.Cells APIでは、スマートマーカーを処理するための[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)クラスを提供しており、そこでデザイナースプレッドシートに書式設定や数式が配置され、指定されたスマートマーカーに従ってデータを埋めるための[**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)クラスで処理されます。スマートマーカーを処理してExcelのチャートを作成することも可能であり、そのためには次の手順が必要です。

- デザイナースプレッドシートの作成
- 指定されたデータソースに対してデザイナースプレッドシートを処理
- 埋め込まれたデータに基づいたチャートの作成

{{% /alert %}}

## デザイナースプレッドシートの作成

デザイナースプレッドシートとは、Microsoft ExcelアプリケーションまたはAspose.Cells APIを使用して作成されたシンプルなExcelファイルであり、ビジュアル書式設定、数式、およびスマートマーカーが含まれており、コンテンツはランタイムで埋めることができます。

簡単にするために、デモンストレーション目的でAspose.Cells for .NET APIを使用してデザイナースプレッドシートを作成し、後でそれを動的に作成されたデータソースに処理する方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## デザイナースプレッドシートの処理

デザイナースプレッドシートを処理するためには、デザイナースプレッドシートで使用されているスマートマーカーに対応するデータソースが必要です。たとえば、Sales. Yearを表すSmart Markerエントリとして&=Sales.Yearを作成しました。DataTable SalesのYear列に対応する列がデータソースにない場合、当該スマートマーカーの処理はAspose.Cells APIでスキップされ、その結果、特定のスマートマーカーのデータが埋められません。

このユースケースをデモンストレーションするために、前の手順で作成したデザイナースプレッドシートに対してデータソースを作成し処理します。ただし、リアルタイムのシナリオでは、データがすでに利用可能な場合はデータソースの作成をスキップすることができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

スマートマーカーの処理は、以下のコードスニペットによって簡単にデモンストレーションされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

上記のコードスニペットは最初の手順で作成された[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの既存のインスタンスを使用しています。デザイナースプレッドシートファイルがすでにディスクまたはメモリにある場合は、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのインスタンスを作成することができます。

{{% /alert %}}

## チャートの作成

データが用意されている場合、必要なのはデータソースに基づいたチャートを作成するだけです。例をシンプルにするために、[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)メソッドを使用するので、チャートを追加の構成する必要がありません。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
