---
title: ファイルを保存するさまざまな方法
linktitle: ファイルを保存する
type: docs
weight: 40
url: /ja/net/different-ways-to-save-files/
description: Aspose.Cells for .NETを使用してファイルをさまざまな形式で保存できます。PDF形式でファイルを保存する。HTML形式でファイルを保存する。DOCX形式でファイルを保存する。PPTX形式でファイルを保存する。JSON形式でファイルを保存する。MHTML形式でファイルを保存する。
keywords: Aspose.Cellsを使用してExcelをPDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTMLなどの形式でC#を使用して保存するまたは変換する。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、様々な方法でファイルを作成して保存することができます。この記事ではファイルを保存するさまざまな方法について説明します。

{{% /alert %}}

## **ファイルを保存する異なる方法**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)を提供し、Excelファイルを操作するために必要なプロパティとメソッドを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスは、Excelファイルを保存するために使用される[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを提供します。[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドには、さまざまな方法でファイルを保存するために使用される多くのオーバーロードがあります。

ファイルの保存形式は、[**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型によって決定されます。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|CSV|CSVファイルを表します|
|Excel97To2003|はExcel 97-2003ファイルを表します
|Xlsx|Excel 2007 XLSXファイルを表します|
|Xlsm|Excel 2007 XLSMファイルを表します|
|Xltx|Excel 2007テンプレートXLTXファイルを表します|
|Xltm|Excel 2007マクロ有効XLTMファイルを表します|
|Xlsb|Excel 2007バイナリXLSBファイルを表します|
|SpreadsheetML|スプレッドシートXMLファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TabDelimited|はタブ区切りのテキストファイルを表します
|ODS|ODSファイルを表します|
|Html|HTMLファイルを表します|
|MHtml|MHTMLファイルを表します|
|Pdf|PDFファイルを表します|
|XPS|XPSドキュメントを表します|
|TIFF|タグ付き画像ファイル形式（TIFF）を表します|

## **異なる形式でファイルを保存する方法**

ファイルを保存するには、[**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型からの所望のファイル形式を指定して、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)オブジェクトの[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを呼び出す際にファイル名（保存先パスを含む）を指定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **WorkbookをPDFに保存する方法**
Portable Document Format（PDF）は、1990年代にAdobeによって作成されたドキュメントの一種です。このファイル形式の目的は、アプリケーションソフトウェア、ハードウェア、およびオペレーティングシステムに依存しない形式で、文書やその他のリファレンス資料を表現するための標準を導入することでした。PDFファイル形式には、テキスト、画像、ハイパーリンク、フォームフィールド、リッチメディア、デジタル署名、添付ファイル、メタデータ、地理空間機能、3Dオブジェクトなどの情報を含めるための完全な機能があります。

Aspose.CellsでWorkbookをPDFファイルに保存する方法のコードは次のとおりです:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **WorkbookをテキストまたはCSV形式で保存する方法**

時々、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelおよびAspose.Cellsの両方はアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正してファイルをCSV形式で保存することもできます。デフォルトでは、[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)はコンマなので、CSV形式に保存する場合は区切り文字を指定しないでください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **カスタム区切り記号を使用してテキストファイルにファイルを保存する方法**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **ストリームにファイルを保存する方法**

ファイルをストリームに保存するには、*MemoryStream*または*FileStream*オブジェクトを作成し、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)オブジェクトの[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを呼び出してそのストリームオブジェクトにファイルを保存します。[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを呼び出す際に、所望のファイル形式を[**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型を使用して指定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **ExcelファイルをHTMLとMHTファイルに保存する方法**
Aspose.Cellsは、単にExcelファイル、JSON、CSVなどのファイルを.htmlおよび.mhtファイルとして簡単に保存できます。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **ExcelファイルをOpenOffice（ODS、SXC、FODS、OTS）に保存する方法**
ファイルを開いた形式で保存できます：ODS、SXC、FODS、OTSなど。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **ExcelファイルをJSONまたはXMLに保存する方法**

JSON（JavaScript Object Notation）は、人間が読めるテキストを使用してデータを格納および送信するためのオープンな標準ファイル形式です。 JSONファイルは.json拡張子で保存されます。 JSONはより少ないフォーマットが必要であり、XMLの良い代替手段です。 JSONはJavaScriptに由来していますが、言語に依存しないデータ形式です。 JSONの生成と解析は、多くの現代のプログラミング言語でサポートされています。 application/jsonはJSONに使用されるメディアタイプです。

Aspose.CellsはファイルをJSONまたはXMLに保存することをサポートしています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **高度なトピック**
- [ワークブックの圧縮レベルを調整](/cells/ja/net/adjust-workbook-compression-level/)
- [ストリクトなOpen XMLスプレッドシート形式でワークブックを保存](/cells/ja/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [レスポンスオブジェクトへのファイルの保存](/cells/ja/net/saving-file-to-response-object/)
