---
title: Excel ファイルを CSV、PDF、その他の形式で保存する
linktitle: ファイルを保存
type: docs
weight: 20
url: /ja/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**では、柔軟な API を使用して、開発者がゼロから Excel ファイルを作成できます。Excel ファイルを作成したら、ワークブック (ファイル) も保存する必要があります。 Aspose.Cells は、これらのファイルを保存するさまざまな方法を提供します。このトピックでは、開発者がファイルを保存するために採用できるすべての方法について説明します。

{{% /alert %}}

## **ファイルを保存するさまざまな方法**

Aspose.Cells API という名前のクラスを提供します[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)これは Excel ファイルを表し、開発者が Excel ファイルを操作するために必要なすべてのプロパティとメソッドを提供します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスは[**セーブ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)Excel ファイルの保存に使用されるメソッド。の[**セーブ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)メソッドには、さまざまな方法で Excel ファイルを保存するために使用される多くのオーバーロードがあります。

開発者は、ファイルを保存するファイル形式を指定することもできます。ファイルは、XLS、SpreadsheetML、CSV、タブ区切り、タブ区切り値 TSV、XPS など、いくつかの形式で保存できます。これらのファイル形式は、[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙。

[**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙には、次のように、事前定義された多くのファイル形式 (ユーザーが選択できます) が含まれています。

|**ファイル形式の種類**|**説明**|
|:- |:- |
|[**自動**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API は、save メソッドの最初のパラメーターで指定されたファイル拡張子から適切な形式を検出しようとします。|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|CSV ファイルを表します|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Office Open XML SpreadsheetML ファイルを表します|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|XML ベースの XLSM ファイルを表します|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Excel テンプレート ファイルを表します|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Excel マクロ有効テンプレート ファイルを表します|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Excel XLAM ファイルを表します|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|タブ区切り値ファイルを表します|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|タブ区切りのテキスト ファイルを表します|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|HTML ファイルを表します|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|MHTML ファイルを表します|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|OpenDocument スプレッドシート ファイルを表します|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Excel 1997 ～ 2003 リビジョンの既定の形式である XLS ファイルを表します|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|SpreadSheetML ファイルを表します|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Excel 2007 バイナリ XLSB ファイルを表します|
|[**わからない**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|認識できない形式を表しており、保存できません。|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|PDF ドキュメントを表します|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|XML Paper Specification (XPS) ファイルを表します|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Tagged Image File Format (TIFF) ファイルを表します|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|XML ベースの Scalable Vector Graphics (SVG) ファイルを表します|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|データ交換フォーマットを表します。|
|[**数字**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|数値ファイルを表します。|
|[**マークダウン**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|マークダウン ドキュメントを表します。|
**通常、Excel ファイルを保存するには、次の 2 つの方法があります。**

1. **ファイルを特定の場所に保存する**
1. **ファイルをストリームに保存する**

## **ファイルをある場所に保存する**

開発者がファイルを保存場所に保存する必要がある場合は、ファイル名 (完全な保存パスを含む) と目的のファイル形式 ([**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙) の呼び出し中[**セーブ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)）の方法[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)物体。

**例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **ワークブックをテキストまたは CSV 形式に保存する**

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存する必要があります。テキスト形式 (たとえば、TXT、TabDelim、CSV など) の場合、既定では、Microsoft Excel と Aspose.Cells の両方がアクティブなワークシートの内容のみを保存します。

次のコード例は、ブック全体をテキスト形式で保存する方法を示しています。任意の Microsoft Excel または OpenOffice スプレッドシート ファイル (つまり、XLS、XLSX、XLSM、XLSB、ODS など) であるソース ワークブックを任意の数のワークシートと共に読み込みます。

コードが実行されると、ブック内のすべてのシートのデータが TXT 形式に変換されます。

同じ例を変更して、ファイルを CSV に保存できます。デフォルトでは、[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator)はコンマなので、CSV 形式で保存する場合はセパレータを指定しないでください。

**例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **カスタム セパレータを使用したテキスト ファイルの保存**

テキスト ファイルには、書式設定されていないスプレッドシート データが含まれています。このファイルは、データ間にカスタマイズされた区切り文字を含めることができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **ファイルをストリームに保存する**

開発者がファイルを**ストリーム**次に、彼らは作成する必要があります**FileOutputStream**オブジェクトにファイルを保存します**ストリーム**を呼び出してオブジェクトを[**セーブ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)）の方法[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)物体。開発者は、目的のファイル形式を指定することもできます ([**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)列挙) の呼び出し中[**セーブ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)） 方法。

**例：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **ファイルを他の形式に保存する**

### **XLSファイル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX ファイル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDFファイル**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **ContentCopyForAccessibility オプションを設定する**

とともに[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラス、PDFを取得または設定できます[**アクセシビリティExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)変換された PDF のコンテンツ アクセスを制御するオプション。これは、スクリーン リーダー ソフトウェアが PDF ファイルを読み取るために PDF ファイル内のテキストを利用できるようにすることを意味します。アクセス許可の変更パスワードを適用し、スクリーンショットの 2 つの項目の選択を解除することで、無効にすることができます。[ここ](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **カスタム プロパティを PDF にエクスポート**

とともに[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラスを使用すると、ソース ワークブックのカスタム プロパティを PDF にエクスポートできます。[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)列挙子は、プロパティをエクスポートする方法を指定するために提供されています。これらのプロパティは、次の図に示すように、[ファイル] をクリックしてから [プロパティ] オプションをクリックすると、Adobe Acrobat Reader で確認できます。テンプレートファイル「sourceWithCustProps.xlsx」がダウンロード可能[ここ](sourceWithCustProps.xlsx)テストおよび出力用の PDF ファイル「outSourceWithCustProps」が利用可能[ここ](outSourceWithCustProps.pdf)分析のために。

![todo:画像_代替_文章](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Excel ワークブックを Markdown に変換する**

Aspose.Cells API は、スプレッドシートを Markdown 形式にエクスポートするためのサポートを提供します。アクティブなワークシートを Markdown にエクスポートするには、次を渡します。[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)の 2 番目のパラメータとして[**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)） 方法。使用することもできます[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)クラスを使用して、ワークシートを Markdown にエクスポートするための追加設定を指定します。

次のコード例は、アクティブなワークシートを Markdown にエクスポートする方法を示しています。[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)列挙メンバー。をご覧ください[出力Markdownファイル](Book1.txt)参照用のコードによって生成されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **先行トピック**
- [ワークブックの圧縮レベルを調整する](/cells/ja/java/adjust-workbook-compression-level/)
- [ワークブックを別の形式に変換する](/cells/ja/java/converting-workbook-to-different-formats/)
- [ワークブックを厳密な Open XML スプレッドシート形式で保存する](/cells/ja/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Excel から TIFF への変換の進行状況を追跡する](/cells/ja/java/track-conversion-progress-of-excel-to-tiff/)
- [ドキュメント変換の進行状況を追跡する](/cells/ja/java/track-document-conversion-progress/)
