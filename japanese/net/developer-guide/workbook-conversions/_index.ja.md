---
title: Excel を Pdf、画像、その他の形式に変換する
linktitle: ワークブックの変換
type: docs
weight: 65
url: /ja/net/convert-workbook-to-different-formats/
description: Excel ファイルを Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML などに変換します。
---
{{% alert color="primary" %}}

Aspose.Cells は、多くのフォーマット間の変換をサポートしています。技術的には、変換とは、ワークブックをあるファイル形式で読み込み、別のファイル形式に保存することを意味します。

{{% /alert %}}

## **ExcelワークブックをPDFに変換**

PDF ファイルは、組織、政府機関、および個人の間でドキュメントを交換するために広く使用されています。これは標準的なドキュメント形式であり、ソフトウェア開発者は Microsoft Excel ファイルを PDF ドキュメントに変換する方法を見つけるように求められることがよくあります。

Aspose.Cells は、Excel ファイルから PDF への変換をサポートし、変換で高い視覚的忠実度を維持します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Excel ワークブックを JPG に変換**
Aspose.Cells は、Excel ファイルの JPG への変換をサポートしています。
次のコード例は、ワークブックを JPG として保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Excel ワークブックを画像に変換**
Aspose.Cells は、Excel ファイルの画像への変換をサポートしています。
次のコード例は、ワークブックを画像として保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Excel ブックを XPS に変換する**

XPS ドキュメント形式は、ドキュメントのレイアウトと各ページの外観を定義する構造化された XML マークアップと、ドキュメントの配布、アーカイブ、レンダリング、処理、および印刷のためのレンダリング ルールで構成されます。

XPS のマークアップ言語は XAML のサブセットであり、XAML を使用して Windows Presentation Foundation (WPF) プリミティブをマークアップし、ドキュメントにベクター グラフィック要素を組み込むことができます。使用される要素は、パスおよびその他のジオメトリ プリミティブの観点から記述されます。

実際、XPS ファイルは、ドキュメントを構成するファイルを含む、Open Packaging Conventions を使用した Unicode ZIP アーカイブです。これらには、各ページの XML マークアップ ファイル、テキスト、埋め込みフォント、ラスター イメージ、2D ベクター グラフィックス、およびデジタル著作権管理情報が含まれます。 XPS ファイルの内容は、ZIP ファイルをサポートするアプリケーションで開くだけで調べることができます。

Aspose.Cells 6.0.0 から、Microsoft Excel から XPS への変換がサポートされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Excel を Ods、Sxc、Fods に変換 (OpenOffice / LibreOffice Calc)**
Aspose.Cells は、Excel ファイルを Ods、Sxc、および Fods ファイルに変換することをサポートしています。以下のコード例は、[テンプレート](book1.xlsx)Ods、Sxc、および Fods ファイルに。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Excel ワークブックを MHTML ファイルに変換する**

MHTML は、通常の HTML と外部リソース (つまり、画像、アニメーション、オーディオなど、通常はリンクされるコンテンツ) を 1 つのファイルに結合します。これらは、ファイル拡張子が .mht の電子メールに使用されます。

Aspose.Cells は、MHTML ファイルの読み取りと書き込みをサポートします。

次のコード例は、ワークブックを MHTML ファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Excel ワークブックを HTML に変換する**

 Aspose.Cells API は、スプレッドシートを HTML 形式にエクスポートするためのサポートを提供します。この目的のために、Aspose.Cells は**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**クラスを使用して、出力 HTML のいくつかの側面を柔軟に制御できます。

次のコード例は、ブックを HTML ファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **HTML の画像プリファレンスの設定**

8.0.2から、Aspose.Cellsが公開されました**[ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**のために**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**クラスを使用すると、開発者はスプレッドシートを HTML 形式で保存するときに画像の設定を指定できます。

以下は、適用できる画像設定の一部の詳細です。

- **[画像タイプ](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: 画像の種類を指定します。チャートを含むすべての形状は、出力 HTML で画像としてレンダリングされることに注意してください。
- **[SmoothingMode](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: 塗りつぶされた領域の線、曲線、エッジのアンチエイリアシングを指定します。
- **[TextRenderingHint](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: テキスト レンダリングの品質を指定します。
- **[品質](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)** : 画像の品質を 0 ～ 100 で指定します。**[画像タイプ](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**jpegと指定されています。
- **[垂直解像度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: イメージの垂直方向の解像度をドット/インチで取得または設定します。
- **[水平解像度](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**: イメージの水平方向の解像度をドット/インチで取得または設定します。
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)** : イメージの圧縮タイプを取得または設定します。**[画像タイプ](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**は Tiff として指定されます。
- **[透明](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**ImageFormat が Png として指定されている場合、画像の背景を透明にするかどうかを示します。

以下のコードは、使用方法を示しています**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**さまざまな設定を指定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Excel ワークブックを Markdown に変換する**

Aspose.Cells API は、スプレッドシートを Markdown 形式にエクスポートするためのサポートを提供します。アクティブなワークシートを Markdown にエクスポートするには、次を渡します。**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**の 2 番目のパラメータとして**[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)**方法。使用することもできます**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**クラスを使用して、ワークシートを Markdown にエクスポートするための追加設定を指定します。

次のコード例は、アクティブなワークシートを Markdown にエクスポートする方法を示しています。**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**列挙メンバー。をご覧ください[出力Markdownファイル](md_sample.txt)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Excel ワークブックを JSON に変換する**

Aspose.Cells は、ワークブックを Json (JavaScript Object Notation) ファイルに変換することをサポートしています。

次のコード例は、アクティブなワークシートを Json にエクスポートする方法を示しています。[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙メンバー。変換するコードを参照してください[ソースファイル](Book1.xlsx)に[出力Jsonファイル](Book1.Json)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Excel を XML に変換する**
Aspose.Cells は、ブックを Excel 2003 スプレッドシート XML およびプレーン XML データに変換することをサポートしています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Excel ワークブックを TIFF に変換**
Aspose.Cells は、ブックの TIFF ファイルへの変換をサポートしています。

以下のコード スニペットは、Excel を TIFF に変換する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Excel ワークブックを DOCX に変換する**

Aspose.Cells API は、スプレッドシートを DOCX 形式に変換するためのサポートを提供します。ワークブックを DOCX にエクスポートするには、次を渡します。[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)の 2 番目のパラメータとして[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法。使用することもできます[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions)クラスを使用して、ワークシートを DOCX にエクスポートするための追加設定を指定します。

次のコード例は、アクティブなワークシートを DOCX にエクスポートする方法を示しています。[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙メンバー。をご覧ください[出力 DOCX ファイル](Book1.docx)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Excel ワークブックを PPTX に変換**

Aspose.Cells API は、スプレッドシートを PPTX 形式に変換するためのサポートを提供します。ワークブックを PPTX にエクスポートするには、次を渡します。[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)の 2 番目のパラメータとして[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法。使用することもできます[**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions)クラスを使用して、ワークシートを PPTX にエクスポートするための追加設定を指定します。

次のコード例は、アクティブなワークシートを PPTX にエクスポートする方法を示しています。[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙メンバー。をご覧ください[出力PPTXファイル](Book1.pptx)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **先行トピック**
- [XLSB のリビジョンを XLSM に変換](/cells/ja/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/ja/net/convert-excel-to-html/)
- [画像](/cells/ja/net/convert-excel-to-image/)
- [ジェイソン](/cells/ja/net/convert-workbook-to-json/)
- [Excel ワークブックを Ods、Sxc、および Fods (OpenOffice / LibreOffice calc) に変換します。](/cells/ja/net/convert-excel-to-ods/)
- [PDF](/cells/ja/net/convert-excel-workbook-to-pdf/)
- [Excel を CSV、TSV、および Txt に変換する](/cells/ja/net/convert-excel-to-csv-tsv-and-txt/)
- [ドキュメント変換の進行状況を追跡する](/cells/ja/net/track-document-conversion-progress/)
- [CSV、TSV、TXT を Excel に変換](/cells/ja/net/convert-csv-tsv-and-txt-to-excel/)
