---
title: Golangを使ったC++経由でExcelをPdf、Image、その他の形式に変換
linktitle: ワークブックの変換
type: docs
weight: 65
url: /ja/go-cpp/convert-workbook-to-different-formats/
description: ExcelファイルをWord、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XMLなどに変換します。これはAspose.Cells for C++を使用しています。
---

{{% alert color="primary" %}}

Aspose.Cellsは多くのフォーマット間の変換をサポートしています。技術的には、変換は一つのファイル形式のワークブックを読み込み、別の形式で保存することを意味します。

{{% /alert %}}

## **ExcelワークブックをPDFに変換**

PDFファイルは、企業、政府機関、個人間で文書を交換するために広く使用されています。標準的な文書形式であり、ソフトウェア開発者からはMicrosoft ExcelファイルをPDFに変換する方法の提案をよく求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **ExcelワークブックをJPGに変換**
Aspose.CellsはExcelファイルをJPGに変換することをサポートしています。
以下のコード例は、ブックをJPG形式で保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Excelブックを画像に変換する**
Aspose.CellsはExcelファイルを画像に変換することをサポートしています。
以下のコード例は、ブックを画像として保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **ExcelブックをXPSに変換する**

XPS文書形式は、文書のレイアウトと各ページの外観、配布、アーカイブ、レンダリング、処理、印刷に関するレンダリング規則を定義する構造化されたXMLマークアップで構成されています。

XPSのマークアップ言語はXAMLのサブセットであり、ドキュメントにベクターグラフィックス要素を組み込むことを可能にします。これはXAMLを使用してWindows Presentation Foundation (WPF) のプリミティブにマークアップします。使用される要素はパスや他の幾何学的プリミティブとして記述されます。

XPSファイルは、実際にはOpen Packaging Conventionsを使用したUnicode ZIPアーカイブであり、文書を構成するファイルを含みます。これらには各ページのXMLマークアップファイル、テキスト、埋め込みフォント、ラスター画像、2Dベクターグラフィックス、デジタル著作権管理情報が含まれます。XPSファイルの内容はZIPファイルをサポートするアプリケーションで開くだけで簡単に調べることができます。

Aspose.Cells 6.0.0以降、Microsoft ExcelからXPSへの変換がサポートされています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **ExcelをOds、Sxc、Fods（OpenOffice / LibreOffice Calc）に変換**
Aspose.CellsはExcelファイルをOds、Sxc、Fodsファイルに変換することをサポートしています。以下のコード例は、【テンプレート】(book1.xlsx)をOds、Sxc、Fodsファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **ExcelワークブックをMHTMLファイルに変換する**

MHTMLは通常のHTMLと外部リソース（通常はリンクされた画像、アニメーション、オーディオなどのコンテンツ）を1つのファイルに組み合わせたものです。.mhtファイル拡張子を持つ電子メールで使用されています。

Aspose.CellsはMHTMLファイルの読み書きをサポートしています。

以下のコード例は、ワークブックをMHTMLファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **ExcelワークブックをHTMLに変換する**

Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートする機能をサポートしています。これには、出力HTMLの複数の側面を制御する柔軟性を提供する [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/) クラスを使用します。

以下のコード例は、ブックをHTMLファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **HTMLの画像設定を設定する**

8.0.2以降、Aspose.Cellsは[**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/)を[**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/)クラスに公開しており、開発者がスプレッドシートをHTML形式で保存する際の画像の設定を指定できるようになっています。

以下は適用可能な画像設定の詳細です：

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/)：画像タイプを指定します。すべての形状（チャートを含む）は、出力HTMLでは画像としてレンダリングされることに注意してください。
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/)：[**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/)がJpegとして指定された場合、画像の品質を0から100の間で指定します。
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/)：画像の垂直解像度（dpi）を取得または設定します。
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/)：画像の水平解像度（dpi）を取得または設定します。
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/)：[**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/)をTiffとして指定した場合の画像の圧縮タイプを取得または設定します。
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/)：ImageFormatをPngと指定すると、画像の背景が透明にするかどうか示します。

以下のコードは、異なる設定を指定するために[**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/)を使用する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **ExcelブックをMarkdownに変換する**

Aspose.Cells APIはスプレッドシートをMarkdown形式にエクスポートする機能も提供しています。アクティブなワークシートをMarkdownにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2引数として[**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/)を渡してください。また、追加の設定を指定するために[**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/)クラスも使用できます。

以下のコード例は、[**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙体メンバーを使用してアクティブなワークシートをMarkdownにエクスポートする例です。コードによって生成された[出力Markdownファイル](md_sample.txt)を参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **ExcelワークブックをJSONに変換**

Aspose.Cellsは、ワークブックをJSON（JavaScript Object Notation）ファイルに変換することをサポートします。

以下のコード例は、[**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙体メンバーを使用してアクティブなワークシートをJSONにエクスポートする例です。ソースファイル（Book1.xlsx）を変換し、生成された[出力JSONファイル](Book1.Json)を参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **ExcelをXMLに変換**
Aspose.Cellsは、ワークブックをExcel 2003スプレッドシートXMLおよびプレーンXMLデータに変換することをサポートしています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **ExcelブックをTIFFに変換する**
Aspose.Cellsは、ワークブックをTIFFファイルに変換することをサポートしています。

以下のコードスニペットは、ExcelをTIFFに変換する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **ExcelブックをDOCXに変換する**

Aspose.Cells APIはスプレッドシートをDOCX形式に変換することもサポートしています。ワークブックをDOCXにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2引数として[**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/)を渡します。また、[**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/)クラスを使用して追加の設定も指定できます。

以下のコード例は、[**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙体メンバーを使用してアクティブなワークシートをDOCXにエクスポートする例です。コードによる[出力DOCXファイル](Book1.docx)の生成結果を確認してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **ExcelブックをPPTXに変換する**

Aspose.CellsはスプレッドシートをPPTX形式に変換する機能も提供しています。ワークブックをPPTXにエクスポートするには、[**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/)を[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2引数として渡してください。さらに、[**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/)クラスを利用して追加の設定も可能です。

次のコード例は、[**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙メンバーを使用してアクティブなシートをPPTXにエクスポートする方法を示しています。コードによって生成された[出力PPTXファイル](Book1.pptx)を参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **ExcelワークブックをEPUBに変換**

Aspose.Cells APIは、スプレッドシートをEPUB形式に変換するサポートを提供します。ワークブックをEPUBにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第二引数として[**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/)を渡してください。また、[**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)クラスを使用してEPUBへのシートのエクスポートに関する追加設定を指定することも可能です。

次のコード例は、[**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙メンバーを使用してアクティブなシートをEPUBにエクスポートする方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **ExcelワークブックをAZW3に変換**

Aspose.Cells APIは、スプレッドシートをAZW3形式に変換するサポートを提供します。ワークブックをAZW3にエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第二引数として[**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/)を渡してください。また、[**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)クラスを使用してAZW3へのシートのエクスポートに関する追加設定を指定できます。

次のコード例は、[**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙メンバーを使用してアクティブなシートをAZW3にエクスポートする方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **高度なトピック**
- [XLSB のリビジョンを XLSM に変換する](/cells/ja/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ja/cpp/convert-excel-to-html/)
- [イメージ](/cells/ja/cpp/convert-excel-to-image/)
- [Json](/cells/ja/cpp/convert-workbook-to-json/)
- [ExcelワークブックをOds、Sxc、およびFods（OpenOffice / LibreOffice calc）に変換。](/cells/ja/cpp/convert-excel-to-ods/)
- [Pdf](/cells/ja/cpp/convert-excel-workbook-to-pdf/)
- [ExcelをCSV、TSV、Textに変換](/cells/ja/cpp/convert-excel-to-csv-tsv-and-txt/)
- [文書変換の進行状況を追跡する](/cells/ja/cpp/track-document-conversion-progress/)
- [CSV、TSV、TXTをExcelに変換](/cells/ja/cpp/convert-csv-tsv-and-txt-to-excel/)
