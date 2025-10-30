---
title: ExcelファイルをPDFA 1aに対応したPDF形式に変換
type: docs
weight: 130
url: /ja/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Aspose.Cells for Python via .NET APIを使用した、PDFA 1aに対応した形式のExcelファイルをPDF形式に変換する方法の学習。
keywords: ExcelファイルをPDFA 1aに対応したPDF形式に変換する方法、PDFA 1a、PDFA 1b、PDF14、PDF15、PDF16、PDF17に対応したExcelファイルをPDF形式に変換する方法。
---

## **可能な使用シナリオ**

PDF/Aは、文書の長期保存のために設計されたPDFの特別なバージョンで、すべてのフォントがPDFファイル内に埋め込まれるアーカイブ形式のPDFです。PDF/Aは、フォントのリンク設定（フォントの埋め込みに対するリンク設定）や暗号化などの機能を禁止することによって、通常のPDFから異なります。Aspose.Cells for Python via .NETを使用すると、ExcelファイルをPDF/Aに準拠したPDFファイル（PdfA1aおよびPdfA1bの両方がサポートされています）に保存できます。

## **Excel ファイルを PDF フォーマットに変換する（PDFA-1a に対応）**

開発者は変換の様々な属性を設定するために [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) クラスを使用できます。出力 PDF の印刷、フォント、セキュリティおよび圧縮設定について、[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) クラスの異なるプロパティを設定することで制御できます。最も重要なプロパティは、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できるようにする [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) です。

次のサンプルコードでは、Excel ファイルを PDFA-1a と互換性のある PDF フォーマットに変換する方法について説明しています。参照用の [出力 PDF](outputCompliancePdfA1a.pdf) およびスクリーンショットをご覧ください。

## **スクリーンショット**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertExcelFileToPDFA_1a.py" >}}
{{< app/cells/assistant language="python-net" >}}
