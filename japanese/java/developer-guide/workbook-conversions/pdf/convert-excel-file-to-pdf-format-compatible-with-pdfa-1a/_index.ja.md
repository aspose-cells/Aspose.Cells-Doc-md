---
title: ExcelファイルをPDFA 1aに対応したPDF形式に変換
type: docs
weight: 80
url: /ja/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能な使用シナリオ**

PDF/Aは、文書の長期保存を目的として設計されたPDFの特別な派生です。PDF/Aは、PDFのISO標準版であり、文書で使用されているすべてのフォントをPDFファイル内に埋め込むアーカイブ形式のPDFです。PDF/Aは、フォントのリンク切断（埋め込みではなく）や暗号化などの機能を禁止することで、PDFとは異なります。Aspose.Cellsを使用して、ExcelファイルをPDF/Aに準拠したPDFファイルに保存することができます（PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3uがサポートされています）。このトピックでは、ExcelブックをPDF/A準拠（PDF/A-1a）のPDFファイルとして保存する方法について説明します。

## **PDF/A-1aと互換性のある形式でExcelファイルを変換**

開発者は、[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラスを使用して変換のために異なる属性を設定できます。[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラスの異なるプロパティを設定すると、出力PDFの印刷、フォント、セキュリティ、および圧縮設定を制御することができます。最も重要なプロパティは[PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)で、ExcelファイルをPDF/Aに準拠したPDFファイルに保存することができます。

次のサンプルコードは、ExcelファイルをPDF/A-1aに互換する形式に変換する方法について説明しています。[出力PDF](outputCompliancePdfA1a.pdf)および参照用のスクリーンショットを参照してください。

## **スクリーンショット**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
