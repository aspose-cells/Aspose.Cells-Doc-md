---
title: Node.jsとC++を使用したPDFの作成
linktitle: Pdf
type: docs
weight: 220
url: /ja/nodejs-cpp/convert-excel-to-pdf/
description: Aspose.Cells for Node.js via C++を使用してExcelワークブックをPDFに変換する方法を学びます。 
---

{{% alert color="primary" %}}
Aspose.CellsはExcelワークブックをPDFに変換することをサポートしています。この例では、Excelワークブックを完全にPDFに変換する方法を示します。
{{% /alert %}}

## **ExcelワークブックをPDFに変換する**

PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++は、API情報とバージョン番号を出力ドキュメントに直接書き込みます。たとえば、ドキュメントをPDFにレンダリングした際、**PDF Producer**フィールドに値（例：'Aspose.Cells v23.2'）を設定します。

出力ドキュメントでこの情報を変更することができることに注意してください。
{{% /alert %}}

### **直接変換**

Aspose.Cells for Node.js via C++は、その他のソフトウェアに依存せずにスプレッドシートをPDFに変換することをサポートします。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを使用してExcelファイルをPDFとして保存します。[**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドは、ExcelのネイティブファイルをPDFに変換するための[**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙型メンバーを提供します。

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. 空のコンストラクタを呼び出して[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用して、スプレッドシート上で作業を行います（入力データ、書式設定の適用、数式の設定、画像の挿入など）。
1. スプレッドシートコードが完了したら、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを呼び出して、スプレッドシートを保存します。

ファイル形式はPDFである必要がありますので、[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)列挙型から*Pdf*（事前に定義された値）を選択して最終的なPDFドキュメントを生成します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **高度な変換**

異なる属性を設定するために[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)クラスを使用したり、出力PDFの印刷、フォント、セキュリティ、圧縮設定を制御するために[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)クラスの異なるプロパティを設定することもできます。 

[**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--)は最も重要なプロパティで、PDFの標準遵守レベルを設定できます。現在はPDF 1.4、PDF 1.5、PDF 1.6、PDF 1.7、PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3u形式に保存できます。PDF/A形式では、出力ファイルのサイズが通常のPDFファイルよりも大きくなります。

#### **PDF/A準拠ファイルへのワークブックの保存**

以下のコードスニペットは、[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) クラスを使用してExcelファイルをPDF/A準拠のPDF形式に保存する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
[**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--)プロパティは、Aspose.Cells for Node.js via C++ 5.3.0のリリースとともに追加されました。
{{% /alert %}}

#### **PDF作成時間の設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) クラスを使用すると、PDF作成時刻を取得または設定することができます。次のコードは、[**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) プロパティを使用してPDFファイルの作成時刻を設定する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **ContentCopyForAccessibilityオプションの設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) クラスを使用すると、変換されたPDFのコンテンツアクセスを制御するためのPDF [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) オプションを取得または設定できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **PDFへのカスタムプロパティのエクスポート**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) クラスを使用すると、元のワークブック内のカスタムプロパティをPDFにエクスポートすることができます。プロパティのエクスポート方法を指定するために [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) 列挙型が提供されています。これらのプロパティは、次の画像に示すように、Adobe Acrobat Readerで[ファイル]をクリックして[プロパティ]オプションをクリックすることで観察することができます。テンプレートファイル "sourceWithCustProps.xlsx" は[こちら](sourceWithCustProps.xlsx)からダウンロードでき、解析用の出力PDFファイル "outSourceWithCustProps" は[こちら](outSourceWithCustProps.pdf)で利用できます。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **変換属性**

新しいリリースごとに変換機能を強化しています。Aspose.CellのExcelからPDFへの変換にはまだいくつかの制限があります。MapChartはPDF形式への変換時にサポートされていません。また、一部の図形オブジェクトには十分なサポートがありません。

以下の表は、Aspose.Cellsを使用してPDFにエクスポートする際に完全または部分的にサポートされているすべての機能をリストしています。この表は最終的なものではなく、すべてのスプレッドシート属性を網羅していませんが、PDFへの変換にはサポートされていないまたは部分的にサポートされている機能を特定しています。

|**ドキュメント要素**|**属性**|**サポート**|**注釈**|
| :- | :- | :- | :- |
|配置| |はい| |
|背景設定| |はい| |
|ボーダー|色|はい| |
|ボーダー|線のスタイル|はい| |
|ボーダー|線の幅|はい| |
|セルデータ| |はい| |
|コメント| |はい| |
|条件付き書式| |はい| |
|ドキュメントプロパティ| |はい| |
|図形オブジェクト| |部分的|図形オブジェクトの影や3D効果には十分なサポートがありません。WordArtとSmartArtは部分的にサポートされています。|
|フォント|サイズ|はい| |
|フォント|色|はい| |
|フォント|スタイル|はい| |
|フォント|下線|はい| |
|フォント|効果|はい||
|画像| |はい| |
|ハイパーリンク| |はい| |
|チャート|  |部分的に| MapChartはサポートされていません。|
|セルの結合|  |はい|  |
|改ページ|  |はい|  |
|ページ設定|ヘッダー/フッター|はい|  |
|ページ設定|余白|はい|  |
|ページ設定|ページの向き|はい|  |
|ページ設定|ページサイズ|はい|  |
|ページ設定|印刷範囲|はい|  |
|ページ設定|印刷タイトル|はい|  |
|ページ設定|拡大/縮小|はい|  |
|行の高さ/列の幅|  |はい|  |
|右から左への言語|  |はい|  |

{{% alert color="primary" %}}
スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。
{{% /alert %}}

## **高度なトピック**
- [名前付き目次でPDFブックマークを追加する](/cells/ja/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [出力PDFの空白ページを回避する](/cells/ja/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDFへの変換時に特定のUnicode文字のフォントを変更する](/cells/ja/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [XLSXファイルをPDF形式に変換](/cells/ja/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [PDFA-1aに準拠したExcelファイルをPDF形式に変換する](/cells/ja/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像やチャートを含むXLSファイルをPDFに変換](/cells/ja/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [チャートシートの PdfBookmarkEntry を作成](/cells/ja/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [1つのPDFページでワークシートのすべての列を表示する](/cells/ja/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandlerクラスを使用してPDFへのレンダリング中にDrawObjectとバインドを取得](/cells/ja/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excelファイルを変換する際のフォントの置換に関する警告を取得](/cells/ja/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel を PDF にレンダリングする際のエラーを無視](/cells/ja/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - ExcelからPDFへの変換](/cells/ja/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDFへ保存する際にコメントを印刷する](/cells/ja/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [ExcelをPDFに変換する際のOffice Add-Insのレンダリング](/cells/ja/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excelのワークシートごとに1つのPDFページをレンダリング - ExcelからPDFへの変換](/cells/ja/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cellsによる出力PDFでUnicode補助文字をレンダリングする](/cells/ja/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - ExcelからPDFへの変換](/cells/ja/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [異なるPDFファイルごとに各ワークシートを保存](/cells/ja/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [標準または最小サイズでExcelをPDFに保存](/cells/ja/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [指定されたワークシートをPDFに保存](/cells/ja/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [PDFドキュメントをセキュアにする](/cells/ja/nodejs-cpp/secure-pdf-documents/)
- [出力PDFおよび画像内の文字列の交差方法を指定](/cells/ja/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
