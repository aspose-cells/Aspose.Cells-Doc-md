---
title: ExcelファイルをCSV、PDF、その他の形式に保存する
linktitle: ファイルを保存する
type: docs
weight: 20
url: /ja/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells**は、柔軟なAPIを使用して開発者がExcelファイルをゼロから作成することを可能にします。Excelファイルを作成した後は、ワークブック（ファイル）を保存する必要があります。Aspose.Cellsでは、これらのファイルを保存するさまざまな方法を提供しています。このトピックでは、開発者がファイルを保存するために採用できるすべての方法について議論します。

{{% /alert %}}

## **ファイルを保存するさまざまな方法**

Aspose.Cells APIでは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)というクラスが提供され、開発者がExcelファイルを操作する際に必要なすべてのプロパティとメソッドを提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスはExcelファイルを保存するために使用される[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))メソッドを提供します。[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))メソッドには、さまざまな方法でExcelファイルを保存するための多数のオーバーロードが用意されています。

開発者はまた、保存するファイルのフォーマットを指定することができます。ファイルはXLS、SpreadsheetML、CSV、タブ区切り、タブ区切り値TSV、XPSなどの形式で保存することができます。これらのファイル形式は[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙型を使用して指定されます。

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙型には、次のような事前に定義されたファイル形式が含まれています。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|APIは、saveメソッドの最初のパラメータで指定されたファイル拡張子から適切なフォーマットを検出しようとします|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|CSVファイルを表します|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Office Open XML SpreadsheetMLファイルを表します|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|XMLベースのXLSMファイルを表します|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Excelテンプレートファイルを表します|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Excelマクロ有効化テンプレートファイルを表します|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Excel XLAMファイルを表します|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|タブ区切り値ファイルを表します|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|タブ区切りテキストファイルを表します|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|HTMLファイルを表します|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|MHTMLファイルを表します|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|OpenDocumentスプレッドシートファイルを表します|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Excel 1997年から2003年までの形式のデフォルトのXLSファイルを表します|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|SpreadSheetMLファイルを表します|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Excel 2007バイナリXLSBファイルを表します|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|認識されない形式を表し、保存できません。|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|PDFドキュメントを表します|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|XML Paper Specification（XPS）ファイルを表します|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Tagged Image File Format（TIFF）ファイルを表します|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|XMLベースの拡張可能なベクトルグラフィックス（SVG）ファイルを表します|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|データ交換形式を表します。|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|ナンバーズファイルを表します。|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|マークダウンドキュメントを表します。|
**通常、Excelファイルを保存する方法は2つあります:**

1. **ファイルを特定の場所に保存**
1. **ファイルをストリームに保存**

## **ファイルを任意の場所に保存する**

開発者がファイルを特定のストレージ場所に保存する必要がある場合、単にファイル名（完全な保存パスを含む）と所望のファイル形式（[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙体を使用）を指定して[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)オブジェクトの[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))メソッドを呼び出すことで可能です。

**例:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **ワークブックをテキストまたはCSV形式で保存**

時々、複数のワークシートを持つワークブックをテキスト形式に変換または保存したいことがあります。テキスト形式（たとえばTXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelとAspose.Cellsの両方がアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードが実行されると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正してファイルを CSV に保存できます。デフォルトでは、[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) はコンマですので、CSV 形式に保存する場合はセパレーターを指定しないでください。ご注意ください：評価版を使用しており、かつメソッド [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) のパラメーターが true に設定されていても、プログラムは引き続きワークシートを1つだけエクスポートします。

**例:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **カスタム区切り文字でテキストファイルを保存**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **ストリームにファイルを保存**

開発者がファイルを**ストリーム**に保存する必要がある場合、**FileOutputStream**オブジェクトを作成して、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)オブジェクトの[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))メソッドを呼び出してその**ストリーム**オブジェクトにファイルを保存します。開発者は、[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))メソッドを呼び出す際に、所望のファイル形式（[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙体を使用）も指定できます。

**例:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **他の形式にファイルを保存**

### **XLS ファイル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX ファイル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF ファイル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **ContentCopyForAccessibilityオプションの設定**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class, you can get or set the PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) option to control the content access in the converted PDF. It means it allows screen reader software to utilize the text within the PDF file for reading the PDF file.  You can disable it by applying a change permissions password and deselecting the two items in the screenshot [here](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **PDFへのカスタムプロパティのエクスポート**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class, you can export the custom properties in source workbook to the PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on File and then properties option as shown in the following image. Template file "sourceWithCustProps.xlsx"  can be downloaded [here](sourceWithCustProps.xlsx) for testing and output PDF file "outSourceWithCustProps" is available [here](outSourceWithCustProps.pdf) for analysis.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **ExcelブックをMarkdownに変換する**

Aspose.Cells APIは、スプレッドシートをMarkdown形式にエクスポートするサポートを提供します。アクティブワークシートをMarkdownにエクスポートするには、2番目のパラメーターとして[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)を渡します。ワークシートのエクスポートのための追加の設定を指定するために[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)クラスを使用することもできます。

以下のコード例は、[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)列挙型メンバーを使用してアクティブなワークシートをMarkdownにエクスポートする方法を示しています。コードによって生成された[出力Markdownファイル](Book1.txt)を参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **高度なトピック**
- [ワークブックの圧縮レベルを調整](/cells/ja/java/adjust-workbook-compression-level/)
- [ワークブックを異なる形式に変換する](/cells/ja/java/converting-workbook-to-different-formats/)
- [ストリクトなOpen XMLスプレッドシート形式でワークブックを保存](/cells/ja/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [ExcelからTIFFへの変換の進行状況を追跡](/cells/ja/java/track-conversion-progress-of-excel-to-tiff/)
- [文書変換の進行状況を追跡する](/cells/ja/java/track-document-conversion-progress/)
