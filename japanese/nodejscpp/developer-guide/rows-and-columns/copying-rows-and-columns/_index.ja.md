---  
title: Node.jsとC++を使用した行と列のコピー  
linktitle: 行と列のコピー  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/copying-rows-and-columns/  
description: この記事では、Aspose.Cells for Node.js via C++ APIを使用した行と列のコピー方法を紹介します。  
keywords: Node.js経由のC++：行と列のコピー方法、Node.jsでの行のコピー、Node.jsでの列のコピー、Aspose.Cells for Node.js via C++を使用した行と列の貼り付け、複数の行と列の貼り付け、単一の行または列のコピーと貼り付け方法。  
---  

## **紹介**  

時には、ワークシート全体をコピーせずに行や列をコピーする必要があります。Aspose.Cellsを使用すると、ワークブック内またはワークブック間で行や列をコピーすることができます。  
行（または列）をコピーすると、それに含まれるデータ（更新された参照を含む数式、値、コメント、書式設定、非表示セル、画像、その他の図形オブジェクトなど）がコピーされます。  

## **Microsoft Excelで行や列をコピーする方法**  

1. コピーしたい行または列を選択します。  
1. 行または列をコピーする場合は、**標準**ツールバーの**コピー**をクリックするか、**CTRL**+**C**を押します。  
1. コピーする選択範囲の下または右側に行または列を選択します。  
1. 行または列をコピーする際に、**挿入**メニューで**コピーしたセル**をクリックします。  

{{% alert color="primary" %}}  
**標準**ツールバーの**貼り付け**をクリックするか、**Insert**メニューのコマンドをクリックする代わりに**CTRL**+**V**を押すと、宛先セルの内容が置き換えられます。  
{{% /alert %}}  

## **Microsoft Excelを使用した貼り付けオプションを使用した行や列の貼り付け方法**  

1. コピーしたいデータやその他の属性を含むセルを選択します。  
1. **コピー**をクリックしてHomeタブを選択します。  
1. **貼り付け**したいエリア内で最初のセルをクリックします。  
1. Homeタブで、**貼り付け**の横にある矢印をクリックし、**貼り付け**を選択します。  
1. 希望する**オプション**を選択します。  

## **Aspose.Cells for Node.js via C++を使用して行と列をコピーする方法**  

## **単一の行をコピーする方法**  

Aspose.Cells は [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) クラスの [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) メソッドを提供します。このメソッドは、数式、値、コメント、セル書式、非表示セル、画像、その他の描画オブジェクトを含むすべてのタイプのデータをソース行から宛先行にコピーします。  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) メソッドは次のパラメータを受け取ります：  

- ソースの [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) オブジェクト、  
- ソースの行インデックス、および  
- 宛先の行インデックス。  

このメソッドを使用して、シート内または別のシートに行をコピーします。[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) メソッドはMicrosoft Excelと似た動作をします。例えば、宛先行の高さを明示的に設定する必要はなく、その値もコピーされます。  

次の例は、ワークシートで行をコピーする方法を示しています。テンプレートとなるMicrosoft Excelファイルを使用し、2行目（データ、書式、コメント、画像などを含む）をコピーし、それを同じワークシートの12行目に貼り付けます。  

[**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) メソッドを使用すれば、ソース行の高さを取得するステップをスキップし、宛先行の高さを設定することも可能です。[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) メソッドは自動的に行の高さを調整します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
行をコピーする際は、関連する画像、グラフ、またはその他の描画オブジェクトに注目することが重要です。これはMicrosoft Excelと同じです。  

1. もしソース行インデックスが5であれば、画像、グラフなどはその3行に含まれている場合にコピーされます（開始行インデックスが4で終了行インデックスが6の場合）。  
1. 宛先行にある既存の画像やグラフなどは削除されません。  
{{% /alert %}}  

## **複数の行をコピーする方法**  

また、[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) メソッドを使用して複数の行をコピーし、その際に追加の整数型のパラメータでコピーするソース行の数を指定することもできます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **列をコピーする方法**  

Aspose.Cellsは [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) クラスの [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) メソッドを提供します。このメソッドは、数式（更新された参照付き）を含むすべてのタイプのデータ、値、コメント、セル書式、非表示セル、画像、およびその他の描画オブジェクトをソース列から宛先列にコピーします。  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) メソッドは次のパラメータを受け取ります：  

- ソースの [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) オブジェクト、  
- ソースの列インデックス、および  
- 宛先の列インデックス。  

この [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) メソッドを使用して、シート内または別のシートに列をコピーします。  

この例では、ワークシートから列をコピーして別のブック内のワークシートに貼り付けます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **複数の列をコピーする方法**  

[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) メソッドに似ており、Aspose.Cells APIは複数のソース列を新しい場所にコピーするために [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) メソッドも提供しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **貼り付けオプションを使用して行と列を貼り付ける方法**  

Aspose.Cellsは現在、関数[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)および[**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-)を使用して[**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/)を提供しています。これにより、Excelと同様の適切な貼り付けオプションを設定することができます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
