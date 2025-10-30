---
title: Node.js経由のC++を使用したマージン設定
linktitle: マージンの設定
type: docs
weight: 20
url: /ja/nodejs-cpp/setting-margins/
description: この記事では、サンプルコードを使ってExcelワークシートのマージンを設定する方法と、Node.js APIを経由してページ中央、ヘッダー、フッターのマージンをプログラム的に設定する方法について学びます。
keywords: Excelワークシートのマージンを中央に設定（Node.js via C++）、ヘッダーとフッターのマージンを設定（Node.js via C++）
---

{{% alert color="primary" %}}

Aspose.CellsはMicrosoft Excelのページ設定オプションを完全にサポートしています。開発者は印刷プロセスを制御するためにワークシートのページ設定設定を構成する必要があります。このトピックでは、Aspose.Cellsを使用してページ余白を設定する方法について説明します。

{{% /alert %}}

## **マージンの設定**

Aspose.Cellsは、Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートへアクセス可能な [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートのページセットアップオプションを設定するために使用される [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)プロパティを提供します。[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)属性は[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)クラスのオブジェクトであり、印刷されたワークシートのページレイアウト設定を可能にします。[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)クラスはさまざまなページ設定オプションを設定するためのプロパティとメソッドを提供します。

### **ページ余白**

ページ余白（左、右、上、下）を[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)クラスのメンバーを使って設定します。一部のメソッド例は以下の通りです。

- [**PageSetup.getLeftMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getLeftMargin--)
- [**PageSetup.getRightMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getRightMargin--)
- [**PageSetup.getTopMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getTopMargin--)
- [**PageSetup.getBottomMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBottomMargin--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Set bottom, left, right and top page margins
pageSetup.setBottomMargin(2);
pageSetup.setLeftMargin(1);
pageSetup.setRightMargin(1);
pageSetup.setTopMargin(3);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetMargins_out.xls"));
```

### **ページの中央に配置**

ページを横方向および縦方向に中央揃えに配置することは可能です。そのための便利なメンバーとして[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)クラスの[**PageSetup.getCenterHorizontally()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterHorizontally--)と[**PageSetup.getCenterVertically()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterVertically--)があります。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Center on page Horizontally and Vertically
pageSetup.setCenterHorizontally(true);
pageSetup.setCenterVertically(true);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```

### **ヘッダーとフッタのマージン**

ヘッダーとフッターの余白を設定するには、[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)クラスのメンバーである[**PageSetup.getHeaderMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeaderMargin--)と[**PageSetup.getFooterMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooterMargin--)を使います。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Header / Footer margins
pageSetup.setHeaderMargin(2);
pageSetup.setFooterMargin(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
