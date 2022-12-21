---
title: グラフ シートの PdfBookmarkEntry を作成する
type: docs
weight: 50
url: /ja/net/create-pdfbookmarkentry-for-chart-sheet/
---
## **考えられる使用シナリオ**

以前は、Aspose.Cells が作成されます[**Pdfブックマークエントリ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)通常のシートの場合。しかし、今では Aspose.Cells も作成できます[**Pdfブックマークエントリ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)チャートシート用。チャートシートにはセルA1以外のセルがないため、作成します[**Pdfブックマークエントリ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry)セル A1 のみ。

## **グラフ シートの PdfBookmarkEntry を作成する**

次のサンプル コードは、[サンプル Excel ファイル](61767756.xlsx) 4枚のシートがあります。そのうちの 2 枚は通常のシートで、残りの 2 枚はチャート シートです。次のように 4 つのブックマーク エントリを作成します。

- ブックマーク-I
- ブックマーク II チャート 1
- しおりⅢ
- ブックマーク-IV-チャート2

次のスクリーンショットは、[PDF出力](61767757.pdf)参照用のサンプル コードによって生成されます。

![todo:画像_代替_文章](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
