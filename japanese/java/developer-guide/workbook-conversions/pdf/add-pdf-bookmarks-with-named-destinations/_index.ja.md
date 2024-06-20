---
title: 名前付き目次でPDFブックマークを追加する
type: docs
weight: 20
url: /ja/java/add-pdf-bookmarks-with-named-destinations/
---

## **可能な使用シナリオ**

名前付き目次はPDFページに依存しないPDF内のブックマークまたはリンクの特別な種類です。つまり、PDFにページが追加または削除されても、ブックマークは無効になる可能性がありますが、名前付き目次はそのままです。名前付き目次を作成するには、[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName)プロパティを設定してください。

## **名前付き目次でPDFブックマークを追加する**

次のサンプルコードと、[ソースExcelファイル](50528370.xlsx)、[出力PDFファイル](50528369.pdf)を参照してください。スクリーンショットには、出力PDF内のブックマークや名前付き目次が表示されています。また、名前付き目次の表示方法と、Acrobat ReaderのProfessional版が必要な点についても説明されています。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
