---
title: Node.jsを使ったC++によるセルの書式設定
description: Aspose.Cells for Node.js via C++ でセルの書式設定とスタイル設定方法（数値書式、日付書式、フォントスタイル、その他のセルスタイルオプション）を学習します。ガイドは、魅力的でプロフェッショナルなスプレッドシートの作成をサポートします。
keywords: Aspose.Cells for Node.js via C++、セル書式設定、スタイリング、数値書式設定、日付書式設定、フォントスタイル、セルスタイルオプション、スプレッドシート、作成、プロフェッショナルな見た目、行と列の書式設定。
linktitle: セルの書式設定
type: docs
weight: 120
url: /ja/nodejs-cpp/cells-formatting/
---

## **紹介**

{{% alert color="primary" %}}

Aspose.Cellsは、セルの書式スタイルの取得/設定に使用される[**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)と[**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドを提供します。Aspose.Cellsはまた、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)クラスも提供します。

{{% /alert %}}

## **GetStyleおよびSetStyleメソッドを使用してセルの書式設定する方法**

セルに異なる種類の書式設定スタイルを適用して、背景色や前景色、枠線、フォント、水平および垂直の配置、インデントレベル、テキストの方向、回転角などを設定する。

### **GetStyle および SetStyle メソッドの使用方法**

開発者が異なるセルに異なる書式スタイルを適用する必要がある場合は、[**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)メソッドを使用してセルの[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)を取得し、スタイル属性を指定してから、[**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドを使用して書式設定を適用するのが良いです。以下は、このアプローチを示す例です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **異なるセルのフォーマットにスタイルオブジェクトを使用する方法**

開発者が複数のセルに同じ書式スタイルを適用したい場合は、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトを使用できます。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトの使用手順は以下のとおりです。

1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--)メソッドを呼び出して、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトを追加します。
2. 新たに追加された[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトにアクセスします。
3. 望む書式設定を適用するために、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトのプロパティ/属性を設定します。
4. 設定済みの[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトを目的のセルに割り当てます。

このアプローチは、アプリケーションの効率を大幅に改善し、メモリも節約できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Microsoft Excel 2007 の事前定義されたスタイルの使用方法**

Microsoft Excel 2007 に異なる書式スタイルを適用する必要がある場合、Aspose.Cells API を使用してスタイルを適用します。以下に、セルに事前定義されたスタイルを適用するこのアプローチをデモンストレーションするための例が示されています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **セル内の選択された文字の書式設定方法**

フォント設定の取り扱いは、セル内のテキストの書式設定方法について説明していますが、セルの内容全体の書式設定方法のみを説明しています。しかし、選択した文字のみを書式設定する場合はどうすればよいでしょうか？

Aspose.Cellsもこの機能をサポートしています。このトピックでは、その機能を効果的に使用する方法について説明します。

### **選択された文字の書式設定方法**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供します。[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションの各要素は[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスは、セル内の文字列の範囲を選択するための[**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-)メソッドを提供し、以下のパラメータを取ります。

- **開始インデックス**、選択を開始する文字のインデックス。
- **文字数**、選択する文字数。

[**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-)メソッドは、開発者がセル内の文字列を形式設定できるようにする[**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)クラスのインスタンスを返します。コード例のように、出力ファイルのA1セルには「Visit」という単語はデフォルトのフォントでフォーマットされ、「Aspose!」は太字で青色で表示されます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

セル内のリッチテキストの一部を書式設定したい場合は、[**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) & [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)メソッドの使用を検討してください。[**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--)メソッドはテキストの部分にアクセスし、変更は[**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)メソッドを通じて行えます。一方、**Get**メソッドは[**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)オブジェクトの配列を返し、これらを操作してフォント名、フォント色、太字などのさまざまなプロパティを設定できます。

{{% /alert %}}

## **行および列の書式設定方法**

時には、開発者は行または列に同じ書式を適用する必要があります。セルごとに書式を適用することは時間がかかるため、良い解決策ではありません。
この問題に対処するために、Aspose.Cells がこの記事で詳しく説明しているシンプルで高速な方法を提供します。

### **行および列の書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートへのアクセスを可能にする[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供し、[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションはさらに[**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--)コレクションを提供します。

### **行の書式設定方法**

[**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--)コレクションの各アイテムは[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)オブジェクトを表します。[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)オブジェクトは、行の書式設定に使用される[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)メソッドを提供します。同じ書式を行に適用するには、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトを使用します。以下にその使用方法を示します。

1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスに[**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--)メソッドを呼び出して、[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトを追加します。
2. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトのプロパティを設定して、書式設定を適用します。
3. relevant属性をONにします。
4. 設定済みの[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)オブジェクトを[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)オブジェクトに割り当てます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **列のフォーマット方法**

[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションは、[**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--)コレクションも提供します。[**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--)コレクション内の各アイテムは[**Column**](https://reference.aspose.com/cells/nodejs-cpp/column)オブジェクトを表します。[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)オブジェクトと同様に、[**Column**](https://reference.aspose.com/cells/nodejs-cpp/column)オブジェクトも列の書式設定に[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)メソッドを提供します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **高度なトピック**
- [位置合わせ設定](/cells/ja/nodejs-cpp/cells-alignment-settings/)
- [境界線の設定](/cells/ja/nodejs-cpp/cells-border-settings/)
- [ExcelおよびODSファイルの条件付き書式を設定します。](/cells/ja/nodejs-cpp/conditional-formatting/)
- [Excelのテーマと色](/cells/ja/nodejs-cpp/excel-themes-and-colors/)
- [塗りつぶしの設定](/cells/ja/nodejs-cpp/cells-fill-settings/)
- [フォントの設定](/cells/ja/nodejs-cpp/cells-font-settings/)
- [ワークブックのセルをフォーマットする](/cells/ja/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [1904年日付システムの実装](/cells/ja/nodejs-cpp/implement-1904-date-system/)
- [セルの結合および解除](/cells/ja/nodejs-cpp/merging-and-unmerging-cells/)
- [数値の設定](/cells/ja/nodejs-cpp/cells-number-settings/)
- [セルのスタイルの取得および設定](/cells/ja/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="nodejs-cpp" >}}
