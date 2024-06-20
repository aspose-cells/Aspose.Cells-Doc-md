---
title: 名前付き目次でPDFブックマークを追加する
type: docs
weight: 20
url: /ja/net/add-pdf-bookmarks-with-named-destinations/
---

## **可能な使用シナリオ**

名前付き目次はPDFページに依存しないPDF内のブックマークまたはリンクの特別な種類です。つまり、PDFにページが追加または削除されても、ブックマークは無効になる可能性がありますが、名前付き目次はそのままです。名前付き目次を作成するには、[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry/properties/destinationname)プロパティを設定してください。

## **名前付き目次でPDFブックマークを追加する**

以下のサンプルコードとその[ソースExcelファイル](50528348.xlsx)、[出力PDFファイル](50528349.pdf)を参照してください。スクリーンショットには、出力PDF内のブックマークと名前付きデスティネーションが表示されます。スクリーンショットには、名前付きデスティネーションの表示方法と、Acrobat Readerのプロフェッショナルバージョンが必要であることが記載されています。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-AddPDFBookmarksWithNamedDestinations.cs" >}}
