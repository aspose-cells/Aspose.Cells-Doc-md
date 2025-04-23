---
title: Node.jsとC++を使用したワークシートビュー
linktitle: ワークシートビュー
type: docs
weight: 40
url: /ja/nodejs-cpp/worksheet-views/
description: この記事では、Node.jsとNode.js APIを使用してExcelワークブックおよびワークシートのページブレークプレビューとやり取りする方法を説明します。分割ペイン、フリーズペイン、ズーム倍率も扱います。
---

## **ページブレークプレビュー**

すべてのワークシートは次の2つのモードで表示できます:

- 通常の表示。
- ページブレークプレビュー。

標準ビューはワークシートのデフォルトビューです。ページブレークプレビューは、印刷される範囲を表示する編集ビューです。ページブレークプレビューでは、各ページに表示されるデータを確認でき、印刷エリアやページ区切りを調整できます。Aspose.Cells for Node.js via C++を使用して、開発者は標準ビューやページブレークプレビューを有効にできます。

### **表示モードの制御**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスには、ワークシートを管理するための多くのプロパティやメソッドが含まれています。通常またはページ休止プレビューモードを有効にするには、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)プロパティを使用します。[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)はブールプロパティであり、**true** または **false** の値のいずれかを格納できるためです。

#### **通常の表示の有効化**

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)プロパティを **false** に設定することで、ワークシートを通常ビューに設定します。

#### **ページブレークプレビューの有効化**

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)プロパティを **true** に設定することで、任意のワークシートをページ休止プレビューに設定します。これにより、ワークシートが通常ビューからページ休止プレビューに切り替わります。

次の例は、[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)プロパティを使用してExcelファイルの最初のワークシートのページ休止プレビューモードを有効にする方法を示しています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスのインスタンスを作成して開きます。最初のワークシートのビューは、[**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)プロパティを**true**に設定することでページ休止プレビューに切り替えます。変更されたファイルは、output.xlsとして保存されます。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **ズームファクター**

### **Microsoft Excel の使用**

Microsoft Excel には、ワークシートのズームやスケーリング要素を設定する機能があります。この機能は、ユーザーがワークシートの内容を小さなビューまたは大きなビューで表示するのに役立ちます。ユーザーは、ズーム要素を任意の値に設定できます。

### **Aspose.Cells & ズーム要素**

Aspose.Cellsを使用すると、開発者はワークシートのズームファクタを設定できます。
Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが用意されています。ワークシートのズームファクタを設定するには、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--)プロパティを使用します。ズームファクタは、[**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--)プロパティに数値（整数）を割り当てることで設定されます。

以下に完全な例を示します。これは、[**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--)プロパティを使用してExcelファイルの最初のワークシートのズーム倍率を設定する方法を示しています。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスのインスタンスを作成することで開かれます。最初のワークシートのズームファクタは75に設定され、変更されたファイルはoutput.xlsとして保存されます。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **ウィンドウ枠の固定**

### **Microsoft Excel の使用**

ウィンドウ枠の固定は、Microsoft Excel が提供する機能です。枠を固定すると、ワークシートをスクロールしても表示され続けるデータを選択できます。

### **Aspose.Cells & ウィンドウ枠の固定**

Aspose.Cellsを使用すると、開発者は実行時にワークシートにウィンドウ枠を適用できます。

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートの管理に豊富なプロパティやメソッドを提供します。フリーズペインを設定するには、Worksheetクラスの[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドを呼び出します。[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)メソッドは以下のパラメータを取ります：

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **フリーズされた列**、左側のペインに表示される列数。

book1.xlsファイルは、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスのコンストラクタを呼び出してインスタンス化し、最初のワークシートでいくつかの行と列が固定されます。変更されたファイルはoutput.xlsとして保存されます。

以下に、Excelファイルの最初のワークシートの4行目および3列目（行と列は0から始まるインデックスで表される、C4から始まる）の行と列を固定する方法を示す完全な例が示されています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **画面の分割**

ワークシート内で二つの異なるビューを取得するには、画面を分割する必要があります。Microsoft Excel は、ワークシートのコピーを複数表示し、各パネで独立してスクロールできる非常に便利な機能を提供しています：画面の分割。

パネは同時に動作します。片方で変更を加えると、同時に他方にも変更が表示されます。Aspose.Cells は、ユーザーに対して画面の分割機能を提供しています。

### **画面の分割の適用と解除**

#### **画面の分割**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイルを管理するための多くのプロパティとメソッドが提供されます。分割ビューを実装するには、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)を使用します。パネルを解除するには、[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--)メソッドを使用します。

例では、シンプルなテンプレート ファイルをロードして、最初のワークシートのセルに分割パネル機能を適用し、更新されたファイルを保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

上記のコードを実行すると、生成されたファイルには分割ビューが表示されます。

#### **パネルの削除**

分割ペインを[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--)メソッドを使用して削除します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **高度なトピック**
- [ワークシートでゼロの値の表示を非表示にする](/cells/ja/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [ワークシートタブの色を設定する](/cells/ja/nodejs-cpp/set-worksheet-tab-color/)
- [グリッド線と行列見出しの表示と非表示](/cells/ja/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [行と列、スクロールバーの表示と非表示](/cells/ja/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [ワークシートとタブの表示と非表示](/cells/ja/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [ワークシートで値の代わりに数式を表示する](/cells/ja/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [エラーチェックオプションを使用する](/cells/ja/nodejs-cpp/use-error-checking-options/)

