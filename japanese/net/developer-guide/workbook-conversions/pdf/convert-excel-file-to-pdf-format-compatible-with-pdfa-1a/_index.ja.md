---
title: ExcelファイルをPDFA 1aに対応したPDF形式に変換
type: docs
weight: 130
url: /ja/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **可能な使用シナリオ**

PDF/Aは、文書の長期保存のために設計されたPDFの特別な仕様です。PDF/Aは、Portable Document Format（PDF）のISO標準化バージョンであり、文書内で使用されるすべてのフォントをPDFファイルに埋め込むアーカイブ形式のPDFです。Aspose.Cellsを使用して、ExcelファイルをPDF/A準拠のPDFファイル（PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、およびPDF/A-3uがサポートされています）に保存することができます。このトピックでは、ExcelワークブックをPDF/A準拠（PDF/A-1a）のPDFファイルに保存する方法について説明します。

## **ExcelファイルをPDF形式に変換して、PDF/A-1aと互換性がある形式にする方法**

開発者は変換の様々な属性を設定するために [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) クラスを使用できます。出力 PDF の印刷、フォント、セキュリティおよび圧縮設定について、[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) クラスの異なるプロパティを設定することで制御できます。最も重要なプロパティは、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できるようにする [**PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) です。

次のサンプルコードは、ExcelファイルをPDF/A-1aに対応する形式に変換する方法を説明しています。参照用の[outpur PDF](outputCompliancePdfA1a.pdf)およびスクリーンショットをご覧ください。

## **スクリーンショット**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
{{< app/cells/assistant language="csharp" >}}
