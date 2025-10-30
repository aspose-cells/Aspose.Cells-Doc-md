---
title: チャートシートのPdfBookmarkEntryをGolangを使ってC++で作成
linktitle: チャートシートの PdfBookmarkEntry を作成
type: docs
weight: 50
url: /ja/go-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Aspose.Cells for C++を使用してチャートシート用のPdfBookmarkEntryを作成する方法を学ぶ。
---

## **可能な使用シナリオ**

以前、Aspose.Cellsは通常のシートに対して[**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/)を作成していました。しかし、今ではAspose.Cellsはチャートシートに対しても[**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/)を作成できます。チャートシートにはセルA1以外のセルがないため、A1セルのみに[**PdfBookmarkEntry**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/)を作成します。

## **チャートシートの PdfBookmarkEntry を作成**

次のサンプルコードは、4つのシートを持つ[サンプルExcelファイル](61767756.xlsx)をロードします。そのうち2つは通常のシートで、残りの2つはチャートシートです。以下のように4つのブックマークエントリを作成します。

- ブックマーク-I
- ブックマーク-II-Chart1
- ブックマーク-III
- ブックマーク-IV-Chart2

次のスクリーンショットは、サンプルコードによって生成された[出力PDF](61767757.pdf)を示しています。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePdfbookmarkentryForChartSheet.go" >}}
