---
title: GolangとC++でExcelをPDFにレンダリングしながらタイムラインを描画
linktitle: ExcelをPDFにレンダリングする際のタイムラインの描画
type: docs
weight: 60
url: /ja/go-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: GolangとC++を使用してAspose.CellsでExcelファイルのタイムラインを管理
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずに、タイムラインをPDFにレンダリング
---

## **ExcelをPDFにレンダリングする際のタイムラインの描画**
タイムラインが適用されたExcelファイルがある場合、そのExcelをPDFにエクスポートし、タイムラインの設定を保持したまま出力できることをAspose.Cellsはサポートしています。単にタイムライン付きのExcelファイルをPDFにエクスポートすると、生成されたPDFにはタイムラインが表示されます。

以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、ワークブックを[出力PDFファイル](out.pdf)として保存します。以下のスクリーンショットは、ソースのExcelファイルと生成されたPDFファイルを比較したものです。

<img src="out.png" width="60%">

## **サンプルコード**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DrawTimelineWhileRenderingExcelToPdf.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DrawTimelineWhileRenderingExcelToPdf-1.go" >}}
