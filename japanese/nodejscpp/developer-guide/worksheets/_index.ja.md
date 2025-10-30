---  
title: Node.js経由でC++を使ってMicrosoft Excelファイルのワークシートを管理  
linktitle: ワークシート  
type: docs  
weight: 90  
url: /ja/nodejs-cpp/manage-worksheets/  
description: Aspose.Cells for Node.js via C++を使用してワークシートの追加、削除、アクティブ化を行います。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsの柔軟なAPIを使用して、Microsoft Excelファイルでワークシートを簡単に作成、管理できます。このトピックでは、Microsoft Excelファイルにワークシートを追加および削除する方法について説明します。  
{{% /alert %}}  

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。  

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートの管理のためのさまざまなプロパティとメソッドを提供します。  

## **新しいExcelファイルにワークシートを追加する**  

プログラムで新しいExcelファイルを作成するには：  

1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスのオブジェクトを作成します。  
1. [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)クラスの[**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-)メソッドを呼び出します。空のワークシートが自動的に追加されます。新しいワークシートのシート番号を渡して[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションから参照できます。  
1. ワークシートの参照を取得します。  
1. ワークシートで作業を実行します。  
1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドを呼び出して、新しいワークシートを含むExcelファイルを保存します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **デザイナースプレッドシートにワークシートを追加する**  

デザイナスプレッドシートにワークシートを追加する操作は、新しいワークシートの追加と同じですが、既存のExcelファイルを開く必要があります。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを使用してデザイナスプレッドシートを開くことができます。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **シート名を使用してワークシートにアクセスする**  

名前またはインデックスを指定して任意のワークシートにアクセスできます。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **シート名を使用してワークシートを削除する**  

ファイルからワークシートを削除するには、[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)クラスの[**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-)メソッドを呼び出します。シート名を渡して特定のワークシートを削除できます。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Sheet Indexを使用してワークシートを削除する**  

名前でワークシートを削除するのは、ワークシートの名前がわかっている場合に効果的です。ワークシート名が不明な場合は、シート番号を指定するオーバーロードされた[**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-)メソッドを使用してください。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **シートのアクティブ化およびワークシート内のアクティブセルを作成します**  

時には、Microsoft Excel ファイルを開いたときに特定のワークシートをアクティブにして表示させる必要があります。同様に、特定のセルをアクティブにしてスクロールバーをそのセルに合わせることもあります。Aspose.Cellsはこれらすべてのタスクを実行できます。  

**アクティブなシート**とは、作業中のシートのことです。タブ上のアクティブなシートの名前は、デフォルトで太字になります。  

**アクティブなセル**は選択されたセルであり、タイプを始めるとデータが入力されるセルです。1度に1つのセルがアクティブです。アクティブなセルは太い枠で強調表示されます。  

### **シートのアクティブ化とセルをアクティブにする**  

Aspose.Cellsはシートとセルをアクティブにするための特定のAPI呼び出しを提供します。例えば、[**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--)プロパティはワークブック内のアクティブなシートを設定するのに役立ちます。同様に、[**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--)プロパティはワークシート内でアクティブなセルを設定および取得するために使用されます。  

特定のデータを表示させるために水平または垂直スクロールバーを目的の行と列のインデックス位置に合わせるには、[**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--)と[**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--)プロパティを使用します。  

次の例は、ワークシートをアクティブ化し、その中のアクティブなセルにします。生成された出力では、スクロールバーは、2行と2列を最初に表示されるようにスクロールします。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **高度なトピック**  
- [ワークシートのコピーおよび移動](/cells/ja/nodejs-cpp/copying-and-moving-worksheets/)  
- [ワークシート内のセル数を数える](/cells/ja/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [空のワークシートを検出する](/cells/ja/nodejs-cpp/detecting-empty-worksheets/)  
- [ワークシートがダイアログシートであるかを検索する](/cells/ja/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [ワークシートの一意のIDを取得](/cells/ja/nodejs-cpp/get-worksheet-unique-id/)  
- [シナリオを作成、操作、またはワークシートから削除する](/cells/ja/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [ページ区切りの管理](/cells/ja/nodejs-cpp/managing-page-breaks/)  
- [ページ設定機能](/cells/ja/nodejs-cpp/page-setup-features/)   
- [Aspose.Cellsを使用したOpenXmlのSheet.SheetIdプロパティを利用する](/cells/ja/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [ワークシートビュー](/cells/ja/nodejs-cpp/worksheet-views/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
