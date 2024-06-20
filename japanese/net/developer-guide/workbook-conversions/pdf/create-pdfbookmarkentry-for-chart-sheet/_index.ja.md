---
title: チャートシートの PdfBookmarkEntry を作成
type: docs
weight: 50
url: /ja/net/create-pdfbookmarkentry-for-chart-sheet/
---

## **可能な使用シナリオ**

以前、Aspose.Cellsは通常のシートに対して[**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)を作成していました。しかし、今ではAspose.Cellsはチャートシートに対しても[**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)を作成できます。チャートシートにはセルA1以外のセルがないため、A1セルのみに[**PdfBookmarkEntry**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)を作成します。

## **チャートシートの PdfBookmarkEntry を作成**

次のサンプルコードは、4つのシートを持つ[サンプルExcelファイル](61767756.xlsx)をロードします。そのうち2つは通常のシートであり、残り2つはチャートシートです。次のように、以下のように4つのブックマークエントリを作成します。

- ブックマーク-I
- ブックマーク-II-Chart1
- ブックマーク-III
- ブックマーク-IV-Chart2

次のスクリーンショットは、サンプルコードによって生成された[出力PDF](61767757.pdf)を示しています。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
