---
title: Node.js経由のページブレーク管理（C++）
linktitle: ページブレークの管理
type: docs
weight: 30
url: /ja/nodejs-cpp/managing-page-breaks/
description: この記事では、Aspose.Cells for Node.js via C++を使用してExcelワークシートのページブレークをプログラム的に追加、解除、削除する方法のサンプルコードと解説を提供します。
keywords: ページブレークの設定（Node.js+C++）、Excelのページブレーク設定（Node.js+C++）、ページブレークのクリア（Node.js+C++）、特定のページブレークの削除（Node.js+C++）
---

{{% alert color="primary" %}}

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページブレークが追加されるセルの位置によっては、ページが終了し、ページブレークの後のデータの残りが次のページで印刷されます。単純に言えば、ページブレークは、指定に応じてワークシートを複数のページに分割します。Aspose.Cellsを使用して、実行時にワークシートにページブレークを追加することもできます。Aspose.Cellsでは、以下の2種類のページブレークを追加できます。

- 水平ページブレーク
- 垂直ページブレーク

後続の議論では、Aspose.Cellsを使用して、どのようにしてワークシートに水平または垂直のページブレークを追加できるかについて説明します。

{{% /alert %}}

## **ページブレーク**

Aspose.CellsはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートを管理するために使用される幅広い範囲のプロパティとメソッドを提供しています。

ページブレークを追加するには、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--)および[**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--)プロパティを使用します。

[**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--)および[**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--)プロパティは、いくつかのページブレークを含む可能性があるコレクションであり、各コレクションには水平および垂直ページブレークを管理するためのいくつかのメソッドが含まれています。

### **ページブレークの追加**

ワークシートにページブレークを追加するには、指定されたセルで垂直および水平のページブレークを挿入します。[**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-)と[**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-)メソッドを呼び出します。各**add**メソッドは、ブレークを追加するセルの名前を受け取ります。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

ページビューモードまたは印刷プレビューモードで、これらの改ページがどのように動作するかを確認できます。

{{% /alert %}}

### **特定の改ページを削除する**

特定のページブレークを削除するには、[**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-)と[**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-)メソッドを呼び出します。各**removeAt**メソッドは、削除対象のページブレークのインデックスを受け取ります。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **重要なこと**

ページ設定の**fitToPages**（[**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--)と[**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)）プロパティを設定すると、ページブレーク設定に影響し、印刷時にページブレーク設定が考慮されませんが、設定自体は維持されます。
{{< app/cells/assistant language="nodejs-cpp" >}}
