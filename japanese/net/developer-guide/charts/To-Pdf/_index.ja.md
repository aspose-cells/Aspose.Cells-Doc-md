---
title: グラフをPDFに変換する 
description: Aspose.Cells for .NETを使用して、Microsoft ExcelからグラフをPDFドキュメントに変換する方法を学びます。当ガイドでは、Microsoft Excelからグラフをエクスポートし、PDFとして保存する手順を示します。
keywords: Aspose.Cells for .NET, グラフをPDF, Microsoft Excel, PDF変換, エクスポート, 配布, アーカイブ
type: docs
weight: 47
url: /ja/net/chart-to-pdf/
---

## **PDFへのチャートのレンダリング**

Aspose.CellsのAPIは、結果のPDFをディスクパスまたはストリームに保存する能力を持つ [**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) メソッドを公開しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **希望のページサイズでチャートPDFを作成**
Aspose.Cellsを使用して、指定のページサイズでグラフのPDFを作成し、ページ内でのグラフの配置方法を上部、下部、センター、左、右などで指定することができます。また、出力されたグラフはストリームまたはディスク上に作成することができます。以下は、サンプルコードです。[サンプルExcelファイル](64716906.xlsx)を読み込み、ワークシート内の最初のチャートにアクセスし、指定のページサイズで[出力PDF](64716907.pdf)に変換するコードです。このスクリーンショットは、出力PDFのページサイズがコード内で指定されたように7x7であり、グラフが水平および垂直の両方向で中央に配置されていることを示しています。 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

{{< app/cells/assistant language="csharp" >}}
