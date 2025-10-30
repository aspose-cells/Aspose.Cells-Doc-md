---  
title: ExcelをPdf、Image、その他の形式に変換する  
linktitle: ワークブックの変換  
type: docs  
weight: 65  
url: /ja/nodejs-cpp/convert-workbook-to-different-formats/  
description: Node.js経由でC++を使用してExcelファイルをWord、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XMLなどに変換します。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは多くの形式間での変換をサポートしています。技術的には、変換とはワークブックを1つのファイル形式で読み込み、別の形式で保存することを指します。  
{{% /alert %}}  

## **ExcelワークブックをPDFに変換**  
PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。  

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **ExcelワークブックをJPGに変換**  
Aspose.CellsはExcelファイルをJPGに変換することをサポートしています。下記のコード例は、ワークブックをJPGとして保存する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Excelブックを画像に変換する**  
Aspose.CellsはExcelファイルを画像に変換することをサポートしています。下記のコード例は、ワークブックを画像として保存する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **ExcelブックをXPSに変換する**  
XPS文書形式は、文書のレイアウトと各ページの外観、配布、アーカイブ、レンダリング、処理、印刷に関するレンダリング規則を定義する構造化されたXMLマークアップで構成されています。  

XPSのマークアップ言語はXAMLのサブセットで、Windows Presentation Foundation（WPF）のプリミティブをマークアップするためにベクトルグラフィックス要素を組み込むことができます。使用される要素はパスや他の幾何学的プリミティブで記述されています。  

XPSファイルは、実際には、文書を構成するファイルを含むOpen Packaging Conventionsを使用するユニコードZIPアーカイブであり、各ページのためのXMLマークアップファイル、テキスト、埋め込みフォント、ラスタ画像、2Dベクトルグラフィック、およびデジタル著作権管理情報が含まれています。XPSファイルの内容は、ZIPファイルをサポートするアプリケーションで開くことで簡単に調べることができます。  

Aspose.Cells 6.0.0以降、Microsoft ExcelからXPSへの変換がサポートされています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **ExcelをOds、Sxc、Fods（OpenOffice / LibreOffice Calc）に変換する**  
Aspose.CellsはExcelファイルをOds、Sxc、Fodsファイルに変換することをサポートしています。下記のコード例は、[テンプレート](book1.xlsx)をOds、Sxc、Fodsファイルに変換する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **ExcelワークブックをMHTMLファイルに変換する**  
MHTMLは通常のHTMLと外部リソース（通常はリンクされた画像、アニメーション、オーディオなどのコンテンツ）を1つのファイルに組み合わせたものです。.mhtファイル拡張子を持つ電子メールで使用されています。  

Aspose.CellsはMHTMLファイルの読み書きをサポートしています。  

以下のコード例は、ワークブックをMHTMLファイルとして保存する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **ExcelワークブックをHTMLに変換する**  
Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートする機能をサポートしています。これには、出力HTMLの複数の側面を制御する柔軟性を提供する [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) クラスを使用します。  

以下のコード例は、ブックをHTMLファイルとして保存する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **HTMLの画像設定を設定する**  
8.0.2以降、Aspose.Cellsは[**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--)を[**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions)クラスに公開しており、開発者がスプレッドシートをHTML形式で保存する際の画像の設定を指定できるようになっています。  

適用できるいくつかの画像設定の詳細は以下のとおりです。  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/)：画像タイプを指定します。すべての形状（チャートを含む）は、出力HTMLでは画像としてレンダリングされることに注意してください。   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--)：JPEGとして[**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/)を指定した場合、画像の品質を0から100の範囲で指定します。  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)：画像の垂直解像度（dpi）を取得または設定します。  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--)：画像の水平解像度（dpi）を取得または設定します。  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/)：[**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/)をTiffとして指定した場合の画像の圧縮タイプを取得または設定します。  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--)：ImageFormatをPngと指定すると、画像の背景が透明にするかどうか示します。  

## **ExcelブックをMarkdownに変換する**  
Aspose.Cells APIは、スプレッドシートをMarkdown形式にエクスポートすることもサポートしています。アクティブなワークシートをMarkdownにエクスポートするには、[**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)メソッドの第2引数として[**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)を渡します。また、[**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions)クラスを使用して、ワークシートのMarkdownエクスポートに関する追加設定を指定することも可能です。  

以下のコード例は、[**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体のメンバーを使用してアクティブなワークシートをMarkdownにエクスポートする方法を示しています。生成された[出力Markdownファイル](md_sample.txt)を参考にしてください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **ExcelワークブックをJSONに変換**  
Aspose.Cellsは、ワークブックをJson（JavaScript Object Notation）ファイルに変換することをサポートしています。  

以下のコード例は、[**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体のメンバーを使用してアクティブなワークシートをJsonにエクスポートする方法を示しています。コードを参照して、[ソースファイル](Book1.xlsx)を[出力Jsonファイル](Book1.Json)に変換してください。  

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

## **ExcelをXMLに変換**  
Aspose.Cellsは、ワークブックをExcel 2003スプレッドシートXMLおよびプレーンXMLデータに変換することをサポートしています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **ExcelブックをTIFFに変換する**  
Aspose.Cellsは、ワークブックをTIFFファイルに変換することをサポートしています。  

以下のコードスニペットは、ExcelをTIFFに変換する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **ExcelブックをDOCXに変換する**  
Aspose.Cells APIは、スプレッドシートをDOCX形式に変換することもサポートしています。ワークブックをDOCXにエクスポートするには、[**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)メソッドの第2引数として[**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)を渡してください。また、[**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions)クラスを使用して、ワークシートのエクスポートに関する追加設定を指定できます。  

以下のコード例は、[**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体のメンバーを使用してアクティブなワークシートをDOCXにエクスポートする方法を示しています。生成された[出力DOCXファイル](Book1.docx)を参考にしてください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **ExcelブックをPPTXに変換する**  
Aspose.Cells APIは、スプレッドシートをPPTX形式に変換することもサポートしています。ワークブックをPPTXにエクスポートするには、[**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)メソッドの第2引数として[**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)を渡します。また、[**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions)クラスを使用して、ワークシートのエクスポートに関する追加設定を指定できます。  

以下のコード例は、[**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体のメンバーを使用してアクティブなワークシートをPPTXにエクスポートする方法を示しています。生成された[出力PPTXファイル](Book1.pptx)を参考にしてください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **ExcelワークブックをEPUBに変換**  
Aspose.Cells APIは、スプレッドシートをEPUB形式に変換することもサポートしています。ワークブックをEPUBにエクスポートするには、[**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)メソッドの第2引数として[**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)を渡します。また、[**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions)クラスを使用して、ワークシートをEpubにエクスポートする追加設定を指定できます。  

以下のコード例は、[**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体のメンバーを使用してアクティブなワークシートをEPUBにエクスポートする方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **ExcelワークブックをAZW3に変換**  
Aspose.Cells APIは、スプレッドシートをAZW3形式に変換することもサポートしています。ワークブックをAZW3にエクスポートするには、[**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)メソッドの第2引数として[**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)を渡します。また、[**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions)クラスを使用して、ワークシートのエクスポートに関する追加設定を指定できます。  

以下のコード例は、[**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙体のメンバーを使用してアクティブなワークシートをAZW3にエクスポートする方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **高度なトピック**  
- [XLSB のリビジョンを XLSM に変換する](/cells/ja/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/ja/nodejs-cpp/convert-excel-to-html/)  
- [イメージ](/cells/ja/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/ja/nodejs-cpp/convert-workbook-to-json/)  
- [ExcelワークブックをOds、Sxc、Fods（OpenOffice / LibreOffice calc）に変換する。](/cells/ja/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/ja/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [ExcelをCSV、TSV、Txtに変換](/cells/ja/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [文書変換の進行状況を追跡する](/cells/ja/nodejs-cpp/track-document-conversion-progress/)  
- [CSV、TSV、およびTXTをExcelに変換する](/cells/ja/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
