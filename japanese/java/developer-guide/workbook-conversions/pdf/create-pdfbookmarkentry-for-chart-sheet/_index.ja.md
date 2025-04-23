---
title: チャートシートの PdfBookmarkEntry を作成
type: docs
weight: 50
url: /ja/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **可能な使用シナリオ**

以前、Aspose.Cellsは通常のシートに [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) を作成していました。しかし、Aspose.Cellsはチャートシートにも [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) を作成することができるようになりました。チャートシートには A1セル以外に他のセルがないため、セルA1に対して [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) を作成します。

## **チャートシートの PdfBookmarkEntry を作成**

以下のサンプルコードは、四つのシートを含む[sample Excel file](61767772.xlsx)をロードします。そのうち二つは通常のシートであり、それ以外の二つはチャートシートです。次のように、四つのブックマークエントリを作成します

- ブックマーク-I
- ブックマーク-II-Chart1
- ブックマーク-III
- ブックマーク-IV-Chart2

次のスクリーンショットは、サンプルコードによって生成された[output PDF](61767771.pdf)を参照用に示しています。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
{{< app/cells/assistant language="java" >}}
