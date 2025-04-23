---  
title: Node.js経由のC++を使ったLightCells APIの使用  
linktitle: LightCells APIの使用  
type: docs  
weight: 160  
url: /ja/nodejs-cpp/using-lightcells-api/  
description: LightCells APIを使った大規模Excelファイルの読書と書き込み方の学習。パフォーマンスと効率性を向上させ、メモリ消費を抑えます。  
---  

{{% alert color="primary" %}}  

大量のデータやコンテンツを含む大規模なMicrosoft Excelファイルの読み書きが必要な場合があります。LightCells APIは、メモリを少なく使用し、性能と効率を向上させるために役立ちます。  

{{% /alert %}}  
# イベント駆動アーキテクチャ  
Aspose.Cellsは、セルのコレクションなどの完全なデータモデルブロックをメモリに構築せずに、イベント駆動モードでセルデータを1つずつ操作するために、LightCells APIを提供しています。  

ワークブックを保存するには、セルの内容を1つずつ提供し、コンポーネントがそれを直接出力ファイルに保存します。  

テンプレートファイルを読み込む際に、コンポーネントはすべてのセルを解析し、その値を1つずつ提供します。  

両手順ともに、1つのセルオブジェクトだけを処理して廃棄します；Workbookオブジェクトにはコレクションは保持しません。このモードでは、大量のデータセットを持つMicrosoft Excelファイルのインポートとエクスポートにおいてメモリ節約が可能です。  

LightCells APIは、XLSXファイルとXLSファイルでセルを同じように処理します（実際にはすべてのセルをメモリに読み込むのではなく、1つのセルを処理してから破棄します）が、XLSXファイルではXLSファイルよりもメモリを効果的に節約します。これは2つのフォーマットの異なるデータモデルと構造のためです。  

しかし、**XLSファイルの場合**は、メモリをより多く節約するために、開発者は一時データの保存場所を指定できます。一般的に、**LightCells APIを使ったXLSXファイルの保存は、通常の方法より50%以上のメモリ節約**になる場合があります；**XLSの保存は約20-40%のメモリ節約**になります。  

## 大規模なExcelファイルの書き込み  
Aspose.Cellsは、`LightCellsDataProvider`インターフェースを提供しており、これはプログラムに実装が必要です。このインターフェースは、大規模なスプレッドシートファイルを軽量モードで保存するためのデータプロバイダを表します。  

このモードでブックを保存する際には、`StartSheet(int)`が全てのワークシート保存時にチェックされます。一つのシートについては、`StartSheet(int)`がtrueの場合、そのシートの行とセルのすべてのデータとプロパティがこの実装によって提供されます。最初に、`NextRow()`を呼び出して保存する次の行のインデックスを取得します。有効な行インデックスが返される（行のインデックスは昇順である必要があります）と、その行を表すRowオブジェクトが`StartRow(Row)`で設定されるために提供されます。  

1つの行については、`NextCell()`が最初にチェックされます。有効な列のインデックスが返される（その列のインデックスが昇順である必要があります）場合、そのセルを表すCellオブジェクトが`StartCell(Cell)`でデータとプロパティを設定するために提供されます。セルのデータを設定した後、そのセルは直接生成されたスプレッドシートファイルに保存され、次のセルがチェック・処理されます。  
### 大きなExcelファイルを書く例  
LightCells APIの動作を確認するために、以下のサンプルコードを参照してください。必要に応じてコードセグメントを追加、削除、または更新してください。  

プログラムは、**10,000（10000x30のマトリックス）レコード**を持つ大きなファイルをワークシートに作成し、ダミーデータで埋めます。`Main()`メソッドの`rowsCount`と`colsCount`変数を変更して、自分のマトリックスを指定できます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## 大規模なExcelファイルの読み込み  
Aspose.Cellsは、`LightCellsDataHandler`インターフェースを提供しており、プログラムに実装が必要です。このインターフェースは、大きなスプレッドシートファイルを軽量モードで読み取るためのデータプロバイダを表します。  

このモードでワークブックを読む場合、`StartSheet`が各ワークシートを読む際にチェックされます。シートについては、`StartSheet`がtrueの場合、そのシートのすべてのデータとセルのプロパティがこのインターフェースの実装によって確認・処理されます。各行については、`StartRow`を呼び出して処理が必要かどうかを判断します。処理が必要な行は、そのプロパティが最初に読まれ、開発者は`ProcessRow`にアクセスして処理します。行のセルも処理が必要なら、`ProcessRow`がtrueを返し、その後、各セルに対して`StartCell`が呼び出されます。  
### 大規模Excelファイルの読み取り例  
LightCells APIの動作を確認するために、以下のサンプルコードを参照してください。必要に応じてコードセグメントを追加、削除、または更新してください。  

プログラムは、大きなファイルに何百万ものレコードがあるシートを読み取ります。各シートの読み取りには少し時間がかかります。サンプルコードはファイルを読み取り、各ワークシートのセルの総数、文字列の数、式の数を取得します。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

