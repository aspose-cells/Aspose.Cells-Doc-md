---
title: ファイルを保存するさまざまな方法
linktitle: ファイルを保存する
type: docs
weight: 40
url: /ja/net/different-ways-to-save-files/
description: Aspose.Cells for .NET は、ファイルをさまざまな形式で保存できます。ファイルを PDF に保存。 ファイルを HTML に保存。 ファイルを DOCX に保存。 ファイルを PPTX に保存。 ファイルを JSON に保存。 ファイルを MHTML に保存。
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells により、ファイルの作成と保存が可能になります。この記事では、ファイルを保存するさまざまな方法について説明します。

{{% /alert %}}

##  **ファイルを保存するさまざまな方法**

 Aspose.Cells は、**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**これは Microsoft Excel ファイルを表し、Excel ファイルを操作するために必要なプロパティとメソッドを提供します。の**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラスが提供するのは、**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Excel ファイルを保存するために使用されるメソッド。の**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**メソッドには、さまざまな方法でファイルを保存するために使用される多くのオーバーロードがあります。

ファイルが保存されるファイル形式は、**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**列挙

|**ファイル形式の種類**|**説明**|
| :- | :- |
|CSV|CSV ファイルを表します|
|Excel97To2003|Excel 97 ～ 2003 ファイルを表します|
|XLSX|Excel 2007 XLSX ファイルを表します|
|Xlsm|Excel 2007 XLSM ファイルを表します|
|Xltx|Excel 2007 テンプレート XLTX ファイルを表します|
|Xltm|Excel 2007 マクロが有効な XLTM ファイルを表します|
|Xlsb|Excel 2007 バイナリ XLSB ファイルを表します|
|SpreadsheetML|スプレッドシート XML ファイルを表します|
|TSV|タブ区切り値ファイルを表します|
|TabDelimited|タブ区切りテキストファイルを表します|
|ODS|ODS ファイルを表します|
|HTML|HTML ファイルを表します|
|MHtml|MHTML ファイルを表します|
|PDF|PDF ファイルを表します|
|XPS|XPS ドキュメントを表します|
|TIFF|タグ付き画像ファイル形式を表します (TIFF)|

##  **ファイルをさまざまな形式で保存する方法**

ファイルを保管場所に保存するには、ファイル名 (保管パスを含む) と希望のファイル形式 (ファイル形式から指定) を指定します。**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**列挙型) を呼び出すとき**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**オブジェクトの**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **ワークブックを PDF に保存する方法**
Portable Document Format (PDF) は、1990 年代に Adobe によって作成されたドキュメントの種類です。このファイル形式の目的は、アプリケーション ソフトウェア、ハードウェア、オペレーティング システムに依存しない形式でドキュメントやその他の参考資料を表現するための標準を導入することでした。 PDF ファイル形式には、テキスト、画像、ハイパーリンク、フォームフィールド、リッチメディア、デジタル署名、添付ファイル、メタデータ、地理空間機能、3D オブジェクトなどの情報を含めて、ソースドキュメントの一部として使用できる完全な機能が備わっています。

次のコードは、ワークブックを Aspose.Cells の PDF ファイルとして保存する方法を示しています。
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **ワークブックをテキストまたは CSV 形式で保存する方法**

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式 (TXT、TabDelim、CSV など) の場合、デフォルトでは、Microsoft Excel と Aspose.Cells の両方がアクティブなワークシートの内容のみを保存します。

次のコード例は、ブック全体をテキスト形式で保存する方法を説明します。任意の数のワークシートを含むソース ワークブック (Microsoft Excel または OpenOffice スプレッドシート ファイル (つまり、XLS、XLSX、XLSM、XLSB、ODS など)) を読み込みます。

コードが実行されると、ブック内のすべてのシートのデータが TXT 形式に変換されます。

同じ例を変更して、ファイルを CSV に保存できます。デフォルトでは、**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**はカンマなので、CSV 形式で保存する場合は区切り文字を指定しないでください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **カスタム区切り文字を使用してファイルをテキスト ファイルに保存する方法**

テキスト ファイルには、書式設定されていないスプレッドシート データが含まれています。このファイルは、データ間にカスタマイズされた区切り文字を含めることができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **ファイルをストリームに保存する方法**

ファイルをストリームに保存するには、*メモリストリーム*または*ファイルストリーム*オブジェクトを呼び出し、そのストリーム オブジェクトにファイルを保存します。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**オブジェクトの**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。を使用して希望のファイル形式を指定します。**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**を呼び出すときの列挙**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **Excel ファイルを HTML および Mht ファイルに保存する方法**
Aspose.Cells は、Excel ファイル、JSON、CSV、または Aspose.Cells によって読み込まれるその他のファイルを .html および .mht ファイルとして保存することができます。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **Excel ファイルを OpenOffice に保存する方法 (ODS、SXC、FODS、OTS)**
ファイルをオープン オフィス形式で保存できます: ODS、SXC、FODS、OTS など。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **Excel ファイルを JSON または XML に保存する方法**

JSON (JavaScript Object Notation) は、人間が読めるテキストを使用してデータを保存および送信する、データ共有用のオープン標準ファイル形式です。 JSON ファイルは .json 拡張子で保存されます。 JSON は、必要な書式設定が少なく、XML の代替として適しています。 JSON は JavaScript から派生していますが、言語に依存しないデータ形式です。 JSON の生成と解析は、多くの最新のプログラミング言語でサポートされています。 application/json は、JSON に使用されるメディア タイプです。

Aspose.Cells は、JSON または XML へのファイルの保存をサポートしています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **アドバンストトピック**
- [ワークブックの圧縮レベルを調整する](/cells/ja/net/adjust-workbook-compression-level/)
- [ワークブックを厳密なオープン XML スプレッドシート形式で保存](/cells/ja/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [ファイルを応答オブジェクトに保存する](/cells/ja/net/saving-file-to-response-object/)
