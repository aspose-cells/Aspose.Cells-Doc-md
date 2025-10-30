---  
title: Node.js経由でC++を使ってダイナミックチャートを作成する  
linktitle: ダイナミックチャートの作成  
description: Aspose.Cells for Node.js via C++でダイナミックチャートを作成する方法を学びます。このガイドは、要件に基づいてチャートのデータ、シリーズ、フォーマットを動的に更新し、ワークシート内で変化するデータをビジュアルに提示する方法を説明します。  
keywords: Aspose.Cells for Node.js、チャーティング、ダイナミックチャート、データ、シリーズ、フォーマット、ワークシート、更新。  
type: docs  
weight: 240  
url: /ja/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
ダイナミック（またはインタラクティブ）チャートは、データのスコープを変更するとチャートが変わる能力を持っています。つまり、データソースが変更されると、動的なチャートは自動的に変更を反映できます。データソースの変更をトリガーするためには、Excelテーブルのフィルタリングオプションを使用するか、ComboBoxやドロップダウンリストなどのコントロールを使用することができます。

この記事は、上記の両アプローチを使用してAspose.Cells for Node.js via C++ APIを活用し、ダイナミックチャートを作成する方法を示します。  
{{% /alert %}}  

## **Excelテーブルの使用**  

{{% alert color="primary" %}}  
ExcelテーブルはAspose.Cellsの視点ではListObjectsと呼ばれるため、「テーブル」ではなく「ListObject」という用語を使用します。詳細については、[ListObjectsの作成方法](/cells/ja/nodejs-cpp/create-and-format-table/)およびAspose.Cells for Node.js via C++ APIをご参照ください。  
{{% /alert %}}  

ListObjectsは、ユーザー操作による並べ替えとフィルタリングの機能を内蔵しています。これらは、[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)のヘッダー行に自動的に追加されるドロップダウンリストを通じて提供されます。これらの機能（並べ替えとフィルタリング）によって、[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)は動的チャートのデータソースとして最適な候補となります。なぜなら、並べ替えやフィルタの変更に伴い、チャート内のデータ表現も変更され、[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)の現在の状態を反映するからです。

簡潔なデモを保つために、最初から[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を作成し、以下の手順で進めていきます。

1. 空の[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を作成します。
1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)内の最初の[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)の[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)にアクセスします。
1. セルにデータを挿入します。
1. 挿入されたデータに基づいて[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)を作成します。
1. [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)のデータ範囲に基づいて[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart)を作成します。
1. 結果をディスクに保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **動的な数式の使用**  

もし、[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)をダイナミックチャートのデータソースとして使用したくない場合、もう一つの方法はExcelの関数（または数式）を使用してダイナミックなデータ範囲を作成し、コントロール（例:コンボボックス）でデータの変更をトリガーすることです。このシナリオでは、VLOOKUP関数を使用して選択に応じた値を取得します。選択が変更されると、VLOOKUP関数はセルの値を更新します。セル範囲全体にVLOOKUPを利用している場合、ユーザー操作により範囲全体が更新され、これをダイナミックチャートのデータソースとして使用できます。

デモンストレーションを理解しやすくするために、以下に概説されているように始め、Workbookを作成し、段階的に進めます。

1. 空の[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を作成します。
1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)内の最初の[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)の[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)にアクセスします。
1. 名前付き範囲を作成してセルにデータを挿入します。このデータはダイナミックチャートのシリーズとして機能します。
1. 前のステップで作成したNamed Rangeを基に[**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox)を作成します。
1. VLOOKUP関数のデータソースとして機能する範囲を作成するためにセルにさらなるデータを挿入します。
1. セル範囲にVLOOKUP関数（適切なパラメータ付き）を挿入します。この範囲は動的チャートのソースとして機能します。
1. 前のステップで作成した範囲に基づいて[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart)を作成します。
1. 結果をディスクに保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
