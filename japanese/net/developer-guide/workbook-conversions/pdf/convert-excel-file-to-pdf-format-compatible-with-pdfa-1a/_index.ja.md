---
title: Excel ファイルを PDFA-1a と互換性のある PDF 形式に変換する
type: docs
weight: 130
url: /ja/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **考えられる使用シナリオ**

PDF/A は、ドキュメントの長期保存用に設計された PDF のユニークなフレーバーです。 PDF/A は、Portable Document Format (PDF) の ISO 標準化バージョンであり、ドキュメントで使用されるすべてのフォントを PDF ファイル内に埋め込む PDF のアーカイブ形式です。 PDF/A は、フォントのリンク (フォントの埋め込みではなく) や暗号化などの機能を禁止している点で PDF とは異なります。 Aspose.Cells を使用すると、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できます (PdfA1a と PdfA1b の両方がサポートされています)。このトピックでは、Excel ブックを PDF/A 準拠 (PdfA1a) PDF ファイルに保存する方法について説明します。

## **Excel ファイルを PDFA-1a と互換性のある PDF 形式に変換する**

開発者は、**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用して、変換用にさまざまな属性を設定します。のさまざまなプロパティの設定**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用すると、出力 PDF の印刷、フォント、セキュリティ、および圧縮の設定を制御できます。最も重要なプロパティは、**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できます。

次のサンプル コードでは、Excel ファイルを PDFA-1a と互換性のある PDF 形式に変換する方法について説明します。ご覧ください[PDF出力](outputCompliancePdfA1a.pdf)参照用のスクリーンショットと同様に。

## **スクリーンショット**

![todo:画像_代替_文章](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
