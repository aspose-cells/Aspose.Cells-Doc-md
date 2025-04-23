---
title: ファイルを保存するさまざまな方法
linktitle: ファイルを保存する
type: docs
weight: 40
url: /ja/python-net/different-ways-to-save-files/
description: Aspose.Cells for Python via .NET は、ファイルをさまざまなフォーマットに保存できます。PDFとして保存、HTMLとして保存、DOCXとして保存、PPTXとして保存、JSONとして保存、MHTMLとして保存。
keywords: Aspose.Cells for Python via .NET は、ExcelをPDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTMLなどに保存や変換が可能です。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET により、ファイルの作成と保存が可能です。この資料では、ファイルの保存方法について説明します。

{{% /alert %}}

## **ファイルを保存する異なる方法**

Aspose.Cells for Python via .NET の `[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)` は、Microsoft Excelファイルを表し、Excelファイルを操作するために必要なプロパティやメソッドを提供します。`[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)` クラスはExcelファイルを保存するための `[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)` メソッドを提供します。`[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)` メソッドは、多くのオーバーロードを持ち、ファイルをさまざまな方法で保存するために使用されます。

ファイルの保存形式は、[**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)列挙型によって決定されます。

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

ファイルを保存するには、[**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)列挙型からの所望のファイル形式を指定して、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)オブジェクトの[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)メソッドを呼び出す際にファイル名（保存先パスを含む）を指定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **WorkbookをPDFに保存する方法**
Portable Document Format（PDF）は、1990年代にAdobeによって作成されたドキュメントの一種です。このファイル形式の目的は、アプリケーションソフトウェア、ハードウェア、およびオペレーティングシステムに依存しない形式で、文書やその他のリファレンス資料を表現するための標準を導入することでした。PDFファイル形式には、テキスト、画像、ハイパーリンク、フォームフィールド、リッチメディア、デジタル署名、添付ファイル、メタデータ、地理空間機能、3Dオブジェクトなどの情報を含めるための完全な機能があります。

以下のコード例では、Aspose.Cells for Python via .NET を使ってワークブックをPDFファイルとして保存する方法を示します：
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **WorkbookをテキストまたはCSV形式で保存する方法**

時には、複数のワークシートが含まれたワークブックをテキスト形式に変換または保存したいと思うことがあります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでは、Microsoft ExcelとAspose.Cells for Python via .NETの両方がアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正して、CSV形式でファイルを保存することも可能です。デフォルトでは、区切り文字はカンマ（,）ですので、CSV形式で保存する場合は区切り文字を指定しないでください。注意点として、評価版を使用している場合でも `[**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/)` プロパティがtrueに設定されている場合でも、プログラムは一つのワークシートだけをエクスポートします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **カスタム区切り記号を使用してテキストファイルにファイルを保存する方法**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **ExcelファイルをHTMLとMHTファイルに保存する方法**
Aspose.Cells for Python via .NET は、Excel、JSON、CSV、その他のファイルを簡単に保存でき、Aspose.Cells for Python via .NET によってロード可能な.htmlや.mhtファイルとして保存されます。
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **ExcelファイルをOpenOffice（ODS、SXC、FODS、OTS）に保存する方法**
ファイルを開いた形式で保存できます：ODS、SXC、FODS、OTSなど。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **ExcelファイルをJSONまたはXMLに保存する方法**

JSON（JavaScript Object Notation）は、人間が読めるテキストを使用してデータを格納および送信するためのオープンな標準ファイル形式です。 JSONファイルは.json拡張子で保存されます。 JSONはより少ないフォーマットが必要であり、XMLの良い代替手段です。 JSONはJavaScriptに由来していますが、言語に依存しないデータ形式です。 JSONの生成と解析は、多くの現代のプログラミング言語でサポートされています。 application/jsonはJSONに使用されるメディアタイプです。

Aspose.Cells for Python via .NET は、JSONまたはXMLへの保存もサポートしています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **高度なトピック**
- [ワークブックの圧縮レベルを調整](/cells/ja/python-net/adjust-workbook-compression-level/)
- [ストリクトなOpen XMLスプレッドシート形式でワークブックを保存](/cells/ja/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

