---
title: ExcelをPdf、Image、その他の形式に変換する
linktitle: ワークブックの変換
type: docs
weight: 65
url: /ja/net/convert-workbook-to-different-formats/
description: ExcelファイルをWord、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XMLなど他の形式に変換する
---

{{% alert color="primary" %}}

Aspose.Cellsは多くの形式間での変換をサポートしています。技術的には、変換とはワークブックを1つのファイル形式で読み込み、別の形式で保存することを指します。

{{% /alert %}}

## **ExcelワークブックをPDFに変換**

PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **ExcelワークブックをJPGに変換**
Aspose.CellsはExcelファイルをJPGに変換することをサポートしています。
以下のコード例は、ブックをJPG形式で保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Excelブックを画像に変換する**
Aspose.CellsはExcelファイルを画像に変換することをサポートしています。
以下のコード例は、ブックを画像として保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **ExcelブックをXPSに変換する**

XPS文書形式は、文書のレイアウトと各ページの外観、配布、アーカイブ、レンダリング、処理、印刷に関するレンダリング規則を定義する構造化されたXMLマークアップで構成されています。

XPSのマークアップ言語はXAMLのサブセットで、Windows Presentation Foundation（WPF）のプリミティブをマークアップするためにベクトルグラフィックス要素を組み込むことができます。使用される要素はパスや他の幾何学的プリミティブで記述されています。

XPSファイルは、実際には、文書を構成するファイルを含むOpen Packaging Conventionsを使用するユニコードZIPアーカイブであり、各ページのためのXMLマークアップファイル、テキスト、埋め込みフォント、ラスタ画像、2Dベクトルグラフィック、およびデジタル著作権管理情報が含まれています。XPSファイルの内容は、ZIPファイルをサポートするアプリケーションで開くことで簡単に調べることができます。

Aspose.Cells 6.0.0以降、Microsoft ExcelからXPSへの変換がサポートされています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **ExcelをOds、Sxc、Fods（OpenOffice / LibreOffice Calc）に変換する**
Aspose.CellsはExcelファイルをOds、Sxc、Fodsファイルに変換することをサポートしています。以下のコード例は、[tempalte](book1.xlsx)をOds、Sxc、Fodsファイルに変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **ExcelワークブックをMHTMLファイルに変換する**

MHTMLは通常のHTMLと外部リソース（通常はリンクされた画像、アニメーション、オーディオなどのコンテンツ）を1つのファイルに組み合わせたものです。.mhtファイル拡張子を持つ電子メールで使用されています。

Aspose.CellsはMHTMLファイルの読み書きをサポートしています。

以下のコード例は、ワークブックをMHTMLファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **ExcelワークブックをHTMLに変換する**

Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートするサポートを提供しています。このため、Aspose.Cellsは[**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)クラスを使用して出力されるHTMLのいくつかの側面を制御する柔軟性を提供しています。

以下のコード例は、ブックをHTMLファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **HTMLの画像設定を設定する**

8.0.2以降、Aspose.Cellsは[**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)クラスのための[**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)を公開し、スプレッドシートをHTML形式に保存する際に開発者がイメージ設定を指定できるようにしています。

適用できるいくつかの画像設定の詳細は以下のとおりです。

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)：画像タイプを指定します。すべての形状（チャートを含む）は、出力HTMLでは画像としてレンダリングされることに注意してください。
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)：線、曲線、塗りつぶしエリアのアンチエイリアシングを指定します。
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)：テキストのレンダリング品質を指定します。
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)：Jpegを指定すると0から100までの画像品質を指定します。
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)：画像の垂直解像度（dpi）を取得または設定します。
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)：画像の水平解像度（dpi）を取得または設定します。
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)：Tiffを指定すると画像の圧縮タイプを取得または設定します。
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)：ImageFormatをPngと指定すると、画像の背景が透明にするかどうか示します。

以下のコードは、[**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)を使用して異なる設定を指定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **ExcelブックをMarkdownに変換する**

Aspose.Cells APIは、スプレッドシートをMarkdown形式にエクスポートするサポートを提供しています。アクティブなワークシートをMarkdownにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2パラメータとして[**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を渡します。また、ワークシートをMarkdownにエクスポートするための追加の設定を指定するには、[**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)クラスを使用できます。

以下のコード例は、[**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型のメンバーを使用してアクティブなワークシートをMarkdownにエクスポートする方法を示しています。生成されたコードの参照用に、[出力Markdownファイル](md_sample.txt)をご覧ください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **ExcelワークブックをJSONに変換**

Aspose.CellsはワークブックをJSON(JavaScript Object Notation)ファイルに変換する機能をサポートしています。

次のコード例は、アクティブワークシートを[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型メンバーを使用してJSONにエクスポートする方法を示しています。参照のために、コードによって生成された[出力JSONファイル](Book1.Json)に変換する[ソースファイル](Book1.xlsx)をご覧ください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **ExcelをXMLに変換**
Aspose.Cellsは、ワークブックをExcel 2003スプレッドシートXMLおよびプレーンXMLデータに変換することをサポートしています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **ExcelブックをTIFFに変換する**
Aspose.Cellsは、ワークブックをTIFFファイルに変換することをサポートしています。

以下のコードスニペットは、ExcelをTIFFに変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **ExcelブックをDOCXに変換する**

Aspose.Cells APIは、スプレッドシートをDOCX形式に変換するサポートを提供しています。ワークブックをDOCXにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2パラメータとして[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を渡します。また、ワークシートをDOCXにエクスポートするための追加の設定を指定するには、[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions)クラスを使用できます。

次のコード例は、アクティブワークシートを[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型メンバーを使用してDOCXにエクスポートする方法を示しています。参照のために、コードによって生成された[出力DOCXファイル](Book1.docx)をご覧ください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **ExcelブックをPPTXに変換する**

Aspose.Cells APIは、スプレッドシートをPPTX形式に変換するためのサポートを提供します。ワークブックをPPTXにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2パラメーターとして[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を渡します。ワークシートをPPTXにエクスポートする追加の設定を指定するには、[**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions)クラスを使用できます。

次のコード例は、アクティブワークシートを[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型メンバーを使用してPPTXにエクスポートする方法を示しています。参照のために、コードによって生成された[出力PPTXファイル](Book1.pptx)をご覧ください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **ExcelワークブックをEPUBに変換**

Aspose.Cells APIは、スプレッドシートのEPUB形式への変換をサポートしています。ワークブックをEPUBにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2引数に[**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を渡します。 また、[**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions)クラスを使用して、ワークシートのエクスポートに関する追加設定を指定できます。

以下のコード例は、[**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙体のメンバーを使用してアクティブなワークシートをEPUBにエクスポートする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToEPUB-1.cs" >}}

## **ExcelワークブックをAZW3に変換**

Aspose.Cells APIは、スプレッドシートのAZW3形式への変換をサポートしています。ワークブックをAZW3にエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)メソッドの第2引数に[**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)を渡します。 また、[**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions)クラスを使用して、ワークシートのエクスポートに関する追加設定を指定できます。

以下のコード例は、[**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙体のメンバーを使用してアクティブなワークシートをAZW3にエクスポートする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToAZW3-1.cs" >}}

## **高度なトピック**
- [XLSB のリビジョンを XLSM に変換する](/cells/ja/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ja/net/convert-excel-to-html/)
- [イメージ](/cells/ja/net/convert-excel-to-image/)
- [Json](/cells/ja/net/convert-workbook-to-json/)
- [ExcelワークブックをOds、Sxc、Fods（OpenOffice / LibreOffice calc）に変換します。](/cells/ja/net/convert-excel-to-ods/)
- [Pdf](/cells/ja/net/convert-excel-workbook-to-pdf/)
- [ExcelをCSV、TSV、およびTxtに変換](/cells/ja/net/convert-excel-to-csv-tsv-and-txt/)
- [文書変換の進行状況を追跡する](/cells/ja/net/track-document-conversion-progress/)
- [CSV、TSV、およびTXTをExcelに変換する](/cells/ja/net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="csharp" >}}
