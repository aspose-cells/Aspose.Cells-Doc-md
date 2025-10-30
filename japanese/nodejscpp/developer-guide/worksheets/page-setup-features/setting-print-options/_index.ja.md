---
title: Node.jsとC++を使用した印刷オプションの設定
linktitle: 印刷オプションの設定
type: docs
weight: 40
url: /ja/nodejs-cpp/setting-print-options/
description: この記事では、Node.js APIとC++ライブラリを使用してExcelワークシートのページ設定機能の印刷オプションをプログラムによって設定する方法を示します。印刷範囲、印刷タイトル、ページ順序を設定できます。
keywords: Node.jsをC++経由で使用してExcelの印刷範囲を設定し、印刷タイトルを設定し、ページ順序を設定する
---

{{% alert color="primary" %}}

Microsoft Excel のページ設定設定には、ワークシートページが印刷される方法を制御するいくつかの印刷オプション (またはシートオプションとも呼ばれる) が含まれています。

{{% /alert %}}

## **印刷オプションの設定**

これらの印刷オプションにより、ユーザーは次のような操作を行うことができます:

- ワークシート上の特定の印刷範囲を選択する。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

Aspose.Cells for Node.js via C++は、Microsoft Excelが提供するすべての印刷オプションをサポートしており、開発者は [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) クラスが提供するプロパティを使用してこれらのオプションを簡単に設定できます。これらのプロパティの使用方法については、以下で詳しく説明します。

### **印刷範囲の設定**

デフォルトでは、印刷エリアにはデータを含むワークシートのすべての領域が組み込まれます。開発者はワークシートの特定の印刷エリアを設定することができます。

特定の印刷エリアを選択するには、[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)クラスの[**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--)プロパティを使用します。このプロパティに印刷エリアを定義するセル範囲を割り当てます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **印刷タイトルを設定する**

Aspose.Cellsでは、印刷されるワークシートのすべてのページで行見出しと列見出しを繰り返すことができます。これを行うには、[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)クラスの[**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--)および[**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--)プロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **その他の印刷オプションの設定**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)クラスは、次の一般的な印刷オプションを設定するためのいくつかの他のプロパティも提供します。

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): グリッド線を印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): 行と列の見出しを印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): ワークシートを白黒モードで印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): ワークシート上に印刷コメントを表示するか、もしくはワークシートの末尾に表示するかを定義します。
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): グラフィックなしでシートを印刷するかどうかを定義するBoolean型のプロパティ。
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): 表示されるままのセルエラー、空白、ダッシュ、またはN/A として印刷するかを定義する。

[**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) と [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) のプロパティを設定するために、Aspose.Cells for Node.js via C++は2つの列挙型 [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) と [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) を提供しており、それぞれに事前定義された値が含まれています。これらの値は [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) と [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) プロパティに割り当てられます。

[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) 列挙型の事前定義された値とその説明は以下の通りです。

|**コメント印刷タイプ**|**説明**|
| :- | :- |
|PrintInPlace|: ワークシート上に表示されているコメントを印刷することを指定。
|PrintNoComments|: コメントを印刷しないことを指定。
|PrintSheetEnd|: ワークシートの最後にコメントを印刷することを指定。

[**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) 列挙型の事前定義された値とその説明は以下の通りです。

|**エラー印刷タイプ**|**説明**|
| :- | :- |
|PrintErrorsBlank|: エラーを印刷しないことを指定。
|PrintErrorsDash|: エラーを "--" として印刷することを指定。
|PrintErrorsDisplayed|: 表示されているエラーを印刷することを指定。
|PrintErrorsNA|: エラーを "#N/A" として印刷することを指定。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **ページ順の設定**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) クラスは、複数のページを印刷する順序を設定するための [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) プロパティを提供します。ページの順序を設定する方法は以下の2つです。

- **Down then over:** 右側のページを印刷する前に、すべてのページを下に印刷します。
- **Over then down:** 下側のページを印刷する前に、左から右のページを印刷します。

Aspose.Cellsは、すべての事前定義された順序タイプを含む列挙型 [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) を提供しています。

[**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) 列挙型の事前定義された値は以下に一覧表示されています。

|**印刷順序タイプ**|**説明**|
| :- | :- |
|DownThenOver|: 下に印刷してから右に印刷するよう指定。
|OverThenDown|: 左から右に印刷してから下に印刷するよう指定。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
