---  
title: 名前付き範囲を作成しコピーする方法（Node.jsとC++）  
linktitle: アクセスおよび名前付き範囲のコピーを作成します  
type: docs  
weight: 200  
url: /ja/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Excelで名前付き範囲を作成、アクセス、およびコピーする方法をAspose.Cells for Node.js via C++を使って学びましょう。  
---  

## **紹介**  

通常、列と行のラベルは個々のセルを参照するために使用されますが、セル範囲、数式、定数値を表すための説明的な名前を作成することも可能です。**name**は、セル、範囲、数式、または定数を表す文字列を指すことがあります。範囲に名前を付けることにより、その範囲は名前で参照できるようになります。理解しやすい名前を使用しましょう。たとえば、Sales!C20:C30といった難解な範囲には「Products」のような名前を付けると良いです。これは、同じワークシート上のデータに参照される場合や、異なるワークシートの範囲を表す場合に役立ちます。*名前付き範囲は、リストコントロール、ピボットテーブル、チャートなどのソース範囲として使う場合に特に強力な機能です。*  

## **Microsoft Excelを使用した名前付き範囲の操作**  

### **名前付き範囲を作成します**  

次のステップは、**MS Excel**を使用してセルまたはセル範囲に名前を付ける方法を説明します。この方法は**Microsoft Office Excel 2003**、**Microsoft Excel 97**、2000、2002に適用されます。  

1. 名前を付けたいセルまたはセル範囲を選択します。  
2. 数式バーの左端にある**名前ボックス**をクリックします。  
3. セルの名前を入力します。  
4. ENTERキーを押します。  

{{% alert color="primary" %}}  
セルの内容を変更しているときにはセルに名前を付けることはできません。  
{{% /alert %}}  

## **Aspose.Cellsを使用した名前付き範囲の操作**  

ここでは、Aspose.Cells API を使用してタスクを実行します。  
Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスには[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションが提供されています。  

### **名前付き範囲の作成**  

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションのオーバーロードされた[**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)メソッドを呼び出すことで、名前付き範囲を作成することが可能です。通常、[**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-)メソッドの一般的なバージョンは、以下のパラメータを取ります:  

- 左上のセルの名前、範囲内の左上のセルの名前。  
- 右下のセルの名前、範囲内の右下のセルの名前。  

[**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-)メソッドを呼び出すと、[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)クラスのインスタンスとして新しく作成された範囲が返されます。この[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)オブジェクトを使用して、名前付き範囲を構成します。たとえば、[**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--)プロパティを使用して範囲の名前を設定します。次の例は、B4:G14を拡張するセルの名前付き範囲を作成する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **名前付き範囲内のセルにデータを入力する**  

範囲の個々のセルにデータを挿入できます。パターンに従って範囲の個々のセルにデータを挿入できます  

- **JavaScript**: Range[row,column]  

A1:C4をスパンするセルの名前付き範囲があるとします。行列は4 * 3 = 12個のセルを作ります。個々の範囲セルは順次配置されています: 範囲[0,0]、範囲[0,1]、範囲[0,2]、範囲[1,0]、範囲[1,1]、範囲[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。  

範囲内のセルを特定するには、次のプロパティを使用します:  

- firstRowは、名前範囲の最初の行のインデックスを返します。  
- firstColumnは、名前範囲の最初の列のインデックスを返します。  
- rowCountは、名前範囲内の総行数を返します。  
- columnCountは、名前範囲内の総列数を返します。  

次の例では、指定された範囲のセルに値を入力する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **名前付き範囲内のセルを特定する**  

範囲の個々のセルにデータを挿入できます。  

- **JavaScript**: Range[row,column]  

A1:C4をスパンする名前付き範囲があるとします。行列は4 * 3 = 12個のセルを作ります。個々の範囲セルは順次配置されています: 範囲[0,0]、範囲[0,1]、範囲[0,2]、範囲[1,0]、範囲[1,1]、範囲[1,2]、範囲[2,0]、範囲[2,1]、範囲[2,2]、範囲[3,0]、範囲[3,1]、範囲[3,2]。  

範囲内のセルを特定するには、次のプロパティを使用します:  

- firstRowは、名前範囲の最初の行のインデックスを返します。  
- firstColumnは、名前範囲の最初の列のインデックスを返します。  
- rowCountは、名前範囲内の総行数を返します。  
- columnCountは、名前範囲内の総列数を返します。  

次の例では、指定された範囲のセルに値を入力する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **名前付き範囲へのアクセス**  

#### **特定の名前付き範囲にアクセスする**  

指定された名前で範囲にアクセスするために、[**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)コレクションの[**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-)メソッドを呼び出します。典型的な[**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-)メソッドは、名前付き範囲の名前を取り、[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)クラスのインスタンスとして指定された名前付き範囲を返します。次の例は、名前で指定された範囲にアクセスする方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **スプレッドシート内のすべての名前付き範囲にアクセス**  

[**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)コレクションの[**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--)メソッドを呼び出して、スプレッドシート内のすべての名前定義範囲を取得します。 [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--)メソッドは、[**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)コレクション内のすべての名前定義範囲の配列を返します。  

次の例は、ワークブック内のすべての名前付き範囲にアクセスする方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **名前付き範囲をコピー**  

Aspose.Cellsは、別の範囲にセルの書式付きでコピーするための[**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-)メソッドを提供します。  

次の例では、ソース範囲のセルを別の名前付き範囲にコピーする方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
