---
title: Node.js経由でMicrosoft Excelファイルのテーブルを作成・管理する
linktitle: テーブル
type: docs
weight: 150
url: /ja/nodejs-cpp/create-and-format-table/
description: Aspose.Cells for Node.js via C++を使用してExcelファイルのテーブルを挿入、リサイズ、編集、削除、フォーマットします。
---

## **テーブルの作成**

スプレッドシートの利点の1つは、電話リスト、タスクリスト、取引のリスト、資産リスト、負債リストなど、さまざまなタイプのリストを作成できることです。複数のユーザーが協力して、さまざまなリストを利用、作成、維持することができます。

Aspose.Cellsはリストの作成と管理をサポートしています。

### **リストオブジェクトの利点**

実際のリストオブジェクトにデータのリストを変換するときの利点はいくつかあります。

- 新しい行や列が自動的に含まれます。
- リストの最下部に合計、平均、カウントなどを表示するために総合行を簡単に追加できます。
- 右に追加された列は自動的にリストオブジェクトに取り込まれます。
- 行と列に基づくチャートは自動的に拡張されます。
- 行と列に割り当てられた名前付き範囲は自動的に拡張されます。
- リストは誤って行や列が削除されないように保護されています。

### **Microsoft Excelを使用してリストオブジェクトを作成する**

- リストオブジェクト作成のためのデータ範囲選択
- これはリスト作成ダイアログを表示します。
- データ用のリストオブジェクトを実装し、合計行を指定します（**データ**を選択し、次に**リスト**、最後に**合計行**を選択）。

### **Aspose.Cells APIを使用する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイルの各ワークシートへのアクセスを可能にする[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは {0} クラスで表されます。{1} クラスは、ワークシート管理のための多くのプロパティとメソッドを提供します。ワークシート内に {2} を作成するには、{4} クラスの {3} コレクションプロパティを使用します。各 {5} は実際には {6} クラスのオブジェクトであり、さらに {7} メソッドを使用してリストオブジェクトを追加し、セル範囲を指定します。指定されたセル範囲に基づいて、Aspose.Cellsがワークシート内に {8} を作成します。属性（例えば {9}）を {10} クラスの属性として使用し、表を要件に合わせてフォーマットします。

指定されたセル範囲に基づいて、ListオブジェクトはAspose.Cellsによって作成されます。リストを制御するために[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)クラスの属性（例：[**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--)、[**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--)など）を使用してください。

以下の例では、上記のセクションでMicrosoft Excelを使用して作成したのと同じ[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)をAspose.Cells APIを使用して作成しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **表の書式設定**

関連するデータのグループを管理および分析するには、セル範囲をリストオブジェクト（またはExcelテーブルとも呼ばれる）に変換することができます。 テーブルは、他の行や列のデータから独立して管理される関連データを含む行と列のシリーズです。 テーブルの各列には、ヘッダー行でフィルタリングが有効になっており、リストオブジェクトデータを迅速にフィルタリングまたは並べ替えることができます。 リストオブジェクトには特別な行（数値データで作業するために有用な集計関数の選択を提供するリスト内の特別な行）を追加することができます。 Aspose.Cellsには、リスト（またはテーブル）の作成と管理のためのオプションが用意されています。

### **リストオブジェクトの書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイルの各ワークシートへのアクセスを可能にする[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、ワークシートの管理に役立つ幅広いプロパティとメソッドを提供します。ワークシートに[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)を作成するには、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--)コレクションプロパティを使用します。各[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)は実際には[**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/)クラスのオブジェクトであり、さらに[**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-)メソッドを提供してListオブジェクトを追加し、その範囲を指定します。指定されたセル範囲に基づいて、Aspose.Cellsはワークシートに[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)を作成します。表を要件に合わせてフォーマットするには、[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)クラスの属性（例：[**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)）を使用してください。

以下の例では、サンプルデータをワークシートに追加し、[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)を追加してデフォルトスタイルを適用します。[**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)スタイルはMicrosoft Excel 2007/2010に対応しています。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **高度なトピック**
- [テーブルをODSに変換する](/cells/ja/nodejs-cpp/convert-table-to-ods/)
- [外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける](/cells/ja/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [クエリテーブルデータソースを持つテーブルの読み書き](/cells/ja/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください](/cells/ja/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表と範囲](/cells/ja/nodejs-cpp/tables-and-ranges/)

{{< app/cells/assistant language="nodejs-cpp" >}}
