---
title: Node.jsとC++を使用したファイル保存方法の多様性
linktitle: ファイルを保存する
type: docs
weight: 40
url: /ja/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++は、PDF、HTML、DOCX、PPTX、JSON、MHTMLなどさまざまな形式でファイルを保存できます。
keywords: Aspose.Cellsは、Node.jsとC++を使用してExcelをPDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTMLなどに保存します。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、様々な方法でファイルを作成して保存することができます。この記事ではファイルを保存するさまざまな方法について説明します。

{{% /alert %}}

## **ファイルを保存する異なる方法**

Aspose.Cellsは、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を表すクラスを提供し、Excelファイルを操作するためのプロパティとメソッドを備えています。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイルを保存するために使用される[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを提供します。[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドは、多くのオーバーロードを持ち、さまざまな方法でファイルを保存します。

保存先のファイル形式は、[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体によって決まります。

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

ファイルをストレージに保存するには、ファイル名（ストレージパスを含む）と希望のファイル形式（[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体から選択）を指定して、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)オブジェクトの[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを呼び出します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **WorkbookをPDFに保存する方法**
ポータブルドキュメント形式(PDF)は、1990年代初頭にAdobeによって作成された文書の一種です。このファイル形式の目的は、アプリケーションソフトウェアやハードウェア、オペレーティングシステムに依存しない文書や参照資料の表現標準を導入することでした。PDFは、テキスト、画像、ハイパーリンク、フォームフィールド、リッチメディア、デジタル署名、添付ファイル、メタデータ、地理空間機能、および3Dオブジェクトを含める完全な能力を持つフォーマットで、ソース文書の一部となることができます。

Aspose.Cellsを使用してワークブックをPDFファイルとして保存する方法を示すコード例：
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **WorkbookをテキストまたはCSV形式で保存する方法**

時々、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelおよびAspose.Cellsの両方はアクティブなワークシートの内容のみを保存します。

以下のコード例は、ワークブック全体をテキスト形式に保存する方法を説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）をロードし、複数のワークシートを含むソースワークブックを使用します。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正して、ファイルをCSVに保存することができます。デフォルトでは、[**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--)はカンマですので、CSV形式で保存するときは区切り文字を指定しないでください。ご注意：評価版を使用している場合、[**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--)プロパティがtrueに設定されていても、プログラムはワークシート1つのみをエクスポートします。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **カスタム区切り記号を使用してテキストファイルにファイルを保存する方法**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **ストリームにファイルを保存する方法**

ファイルをストリームに保存するには、*MemoryStream*または*FileStream*オブジェクトを作成し、そのストリームオブジェクトにファイルを保存します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)オブジェクトの[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを呼び出します。呼び出すときは、希望のファイル形式を[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体で指定し、[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを使用します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **ExcelファイルをHTMLとMHTファイルに保存する方法**
Aspose.Cellsは、Excelファイル、JSON、CSV、その他Aspose.Cellsでロードできる.htmlや.mhtファイルとして保存できるファイルを簡単に保存します。
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **ExcelファイルをOpenOffice（ODS、SXC、FODS、OTS）に保存する方法**
私たちは、ファイルをOpenOffice形式（ODS、SXC、FODS、OTSなど）で保存できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **ExcelファイルをJSONまたはXMLに保存する方法**

JSON（JavaScript Object Notation）は、人間が読めるテキストを使用してデータを格納および送信するためのオープンな標準ファイル形式です。 JSONファイルは.json拡張子で保存されます。 JSONはより少ないフォーマットが必要であり、XMLの良い代替手段です。 JSONはJavaScriptに由来していますが、言語に依存しないデータ形式です。 JSONの生成と解析は、多くの現代のプログラミング言語でサポートされています。 application/jsonはJSONに使用されるメディアタイプです。

Aspose.CellsはファイルをJSONまたはXMLに保存することをサポートしています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **高度なトピック**
- [ワークブックの圧縮レベルを調整](/cells/ja/nodejs-cpp/adjust-workbook-compression-level/)
- [ストリクトなOpen XMLスプレッドシート形式でワークブックを保存](/cells/ja/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [レスポンスオブジェクトへのファイルの保存](/cells/ja/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
