---
title: ファイルを保存するさまざまな方法
linktitle: ファイルを保存
type: docs
weight: 40
url: /ja/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells は、ファイルの作成と保存を可能にします。この記事では、ファイルを保存するさまざまな方法について説明します。

{{% /alert %}}

## **ファイルを保存するさまざまな方法**

Aspose.Cells は**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**これは Microsoft Excel ファイルを表し、Excel ファイルの操作に必要なプロパティとメソッドを提供します。の**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラスが提供する**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Excelファイルを保存するために使用される方法。の**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**メソッドには、さまざまな方法でファイルを保存するために使用される多くのオーバーロードがあります。

ファイルが保存されるファイル形式は、**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**列挙

|**ファイル形式の種類**|**説明**|
|:- |:- |
|CSV|CSV ファイルを表します|
|Excel97To2003|Excel 97 - 2003 ファイルを表します|
|xlsx|Excel 2007 XLSX ファイルを表します|
|Xlsm|Excel 2007 XLSM ファイルを表します|
|Xltx|Excel 2007 テンプレート XLTX ファイルを表します|
|Xltm|Excel 2007 マクロ有効 XLTM ファイルを表します|
|Xlsb|Excel 2007 バイナリ XLSB ファイルを表します|
|SpreadsheetML|スプレッドシート XML ファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TabDelimited|タブ区切りのテキスト ファイルを表します|
|ODS|ODS ファイルを表します|
|HTML|HTML ファイルを表します|
|MHtml|MHTML ファイルを表します|
|PDF|PDF ファイルを表します|
|XPS|XPS ドキュメントを表します|
|TIFF|タグ付き画像ファイル形式 (TIFF) を表します|

## **ファイルを別の形式で保存する**

ファイルを保存場所に保存するには、ファイル名 (保存パスを含む) と目的のファイル形式 (**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**列挙) を呼び出すとき**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**オブジェクトの**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **ワークブックを Pdf として保存**
Portable Document Format (PDF) は、1990 年代に Adobe によって作成されたドキュメントの一種です。このファイル形式の目的は、ドキュメントやその他の参考資料を、アプリケーション ソフトウェア、ハードウェア、およびオペレーティング システムに依存しない形式で表現するための標準を導入することでした。 PDF ファイル形式には、テキスト、画像、ハイパーリンク、フォーム フィールド、リッチ メディア、デジタル署名、添付ファイル、メタデータ、地理空間機能、および 3D オブジェクトなど、ソース ドキュメントの一部として含めることができる完全な機能があります。

次のコードは、workbook を Aspose.Cells の pdf ファイルとして保存する方法を示しています。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **ワークブックをテキストまたは CSV 形式で保存する**

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存する必要があります。テキスト形式 (例: TXT、TabDelim、CSV など) の場合、既定では、Microsoft Excel と Aspose.Cells の両方で、アクティブなワークシートの内容のみが保存されます。

次のコード例は、ブック全体をテキスト形式で保存する方法を示しています。 Microsoft Excel または OpenOffice スプレッドシート ファイル (XLS、XLSX、XLSM、XLSB、ODS など) のソース ワークブックを任意の数のワークシートと共に読み込みます。

コードが実行されると、ブック内のすべてのシートのデータが TXT 形式に変換されます。

同じ例を変更して、ファイルを CSV に保存できます。デフォルトでは、**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**はコンマなので、CSV 形式で保存する場合はセパレータを指定しないでください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **カスタム セパレータを使用したテキスト ファイルの保存**

テキスト ファイルには、書式設定されていないスプレッドシート データが含まれています。このファイルは、データ間にカスタマイズされた区切り文字を含めることができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **ファイルをストリームに保存する**

ファイルをストリームに保存するには、*メモリーストリーム*また*ファイルストリーム*オブジェクトを呼び出して、そのストリーム オブジェクトにファイルを保存します。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**オブジェクトの**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。を使用して目的のファイル形式を指定します。**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**を呼び出すときの列挙**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **ファイルを Html および Mht ファイルとして保存する**
Aspose.Cells は、Excel ファイル、JSON、CSV、または Aspose.Cells が .html および .mht ファイルとしてロードできるその他のファイルを簡単に保存できます。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **OpenOffice として保存 (ODS、SXC、FODS、OTS)**
ファイルをオープンオフィス形式として保存できます：ODS、SXC、FODS、OTSなど。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Excel ファイルを JSON または XML として保存する**

JSON (JavaScript Object Notation) は、人間が判読できるテキストを使用してデータを保存および送信するデータ共有用のオープン スタンダード ファイル形式です。 JSON ファイルは .json 拡張子で保存されます。 JSON は書式設定が少なくて済み、XML の優れた代替手段です。 JSON は JavaScript から派生したものですが、言語に依存しないデータ形式です。 JSON の生成と解析は、多くの最新のプログラミング言語でサポートされています。 application/json は、JSON に使用されるメディア タイプです。

Aspose.Cells は、JSON または XML へのファイルの保存をサポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **先行トピック**
- [ワークブックの圧縮レベルを調整する](/cells/ja/net/adjust-workbook-compression-level/)
- [ワークブックを厳密な Open XML スプレッドシート形式で保存する](/cells/ja/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [ファイルを応答オブジェクトに保存する](/cells/ja/net/saving-file-to-response-object/)
