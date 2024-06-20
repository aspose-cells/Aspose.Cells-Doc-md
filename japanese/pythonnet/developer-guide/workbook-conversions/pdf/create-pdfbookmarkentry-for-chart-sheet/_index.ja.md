---
title: チャートシートの PdfBookmarkEntry を作成
type: docs
weight: 50
url: /ja/python-net/create-pdfbookmarkentry-for-chart-sheet/
description: Aspose.Cells for Python via .NET APIを使用して、Chart Sheet用のPdfBookmarkEntryを作成する方法について学びます。
keywords: PythonでChart Sheet用のPdfBookmarkEntryを作成する方法、Pythonを使用したChart Sheet用のPdfBookmarkEntryの追加、PythonでChart Sheet用のPdfBookmarkEntryを挿入する方法、PythonのPdfBookmarkEntryをChart Sheet用に追加
---

## **可能な使用シナリオ**

以前は、Aspose.Cells for Python via .NETは通常のシートに対して [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) を作成していました。しかし、現在、Aspose.Cells for Python via .NETはチャートシートに対しても [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) を作成できます。チャートシートに他のセルが存在しないため、セルA1に対してのみ [**PdfBookmarkEntry**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/) を作成します。

## **チャートシートの PdfBookmarkEntry を作成**

次のサンプルコードは、4つのシートを持つ[サンプルExcelファイル](61767756.xlsx)をロードします。そのうち2つは通常のシートであり、残り2つはチャートシートです。次のように、以下のように4つのブックマークエントリを作成します。

- ブックマーク-I
- ブックマーク-II-Chart1
- ブックマーク-III
- ブックマーク-IV-Chart2

次のスクリーンショットは、サンプルコードによって生成された[出力PDF](61767757.pdf)を示しています。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-CreatePdfBookmarkEntryForChartSheet.py" >}}
