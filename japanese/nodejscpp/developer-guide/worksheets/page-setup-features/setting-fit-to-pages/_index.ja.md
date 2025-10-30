---
title: Node.jsとC++を使ってExcelを幅と高さに合わせて印刷する方法
linktitle: Excelを縮小ページ幅と高さに印刷するにはどうすればよいですか
type: docs
weight: 200
url: /ja/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: このページは、Aspose.Cells for Node.js via C++を用いたFitToPagesWideとFitToPagesTallの設定方法について解説したコード例を示します。
keywords: Node.jsとC++を使用したFitToPagesWideとFitToPagesTallの設定方法、追加方法、Excelでの使用方法、クリア方法、全ページ幅・高さ調整の印刷方法、ワークシートを一ページに印刷、すべての列を一ページに印刷する方法。
---

## **紹介**

 FitToPagesWideとFitToPagesTallの設定は、Microsoft Excelなどのスプレッドシートアプリケーションで、印刷時にスプレッドシートの縮尺を制御するために使用されます。これらの設定は、印刷結果が指定したページ数内に収まるように、横方向と縦方向の両方でスケーリングを行います。各設定の詳細は以下の通りです：

1. FitToPagesWide：この設定は、印刷出力が何ページの横幅に収まるべきかを指定します。たとえば、FitToPagesWideを1に設定すると、内容は1ページ幅に収まるように縮尺されます。
2. FitToPagesTall: この設定は、縦方向のページ数を指定します。例：FitToPagesTallを1に設定すると、内容は1ページの高さに収まるようにスケールされます。

## **FitToPagesWide と FitToPagesTall を使用する理由**
FitToPagesWideとFitToPagesTallを設定する理由は次の通りです：
1. 印刷レイアウトの制御：横と縦のページ数を指定することで、印刷された文書が見やすく整理された状態になるように保証できます。列や行がページ間で不自然に切れることも避けられます。
2. 一貫性: 複数のシートやレポートを印刷する場合、これらの設定を使用すると一貫したフォーマットを保て、比較や分析が容易になります。
3. 専門的なプレゼンテーション: 内容を適切にスケーリングして指定ページ数に収めることで、よりプロフェッショナルで洗練されたデータの提示が可能となります。

## **Excelでファイルを横長・縦長のフィットページとして印刷する方法**

Microsoft ExcelでFitToPagesWideとFitToPagesTallを設定するには、以下の手順に従います：

1. Excelワークブックを開き、印刷したいシートに移動します。
2. リボンのページレイアウトタブに移動します。
3. ページ設定グループの右下にある矢印をクリックし、ページ設定ダイアログボックスを開きます。
4. ページ設定ダイアログのページタブに進みます。
6. スケーリングの下で、「Fit to」を選択し、横と縦のページ数を指定します：最初のボックスに望むページの横数を入力します（Fit to x pages wide）。次のボックスに望むページの縦数を入力します（Fit to y pages tall）。
<br>
<img src="2.png" width=60% />

設定を適用するにはOKをクリックします。

## **Aspose.Cells for Node.js via C++を使用したExcelを幅と高さで調整して印刷する方法**

特定のワークシートでFitToPagesWideとFitToPagesTallを設定するには：まず、[サンプルファイル](input.xlsx)を読み込み、その後、目的のワークシートの[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)オブジェクトの[**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--)および[**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)プロパティを変更します。以下はNode.jsの例です：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

出力結果：
<br>
<img src="1.png" width=60% />

## **1ページにワークシートを印刷する方法（Aspose.Cells for Node.js via C++）**

ワークシートを1ページに印刷するには：まず、[サンプルファイル](sample.xlsx)を読み込み、その後、[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--)プロパティを設定します。以下はNode.jsの例です：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

出力結果：
<br>
<img src="3.png" width=60% />

## **ワークシートのすべての列を1ページに印刷する方法（Aspose.Cells for Node.js via C++）**

ワークシートのすべての列を1ページに印刷するには：まず、[サンプルファイル](sample.xlsx)を読み込み、その後、[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/)オブジェクトの[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)プロパティを設定します。以下はNode.jsの例です：

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

出力結果：
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
