---  
title: Node.jsをC++経由で使用して、テーブルと範囲を操作する  
linktitle: テーブルおよび範囲  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/tables-and-ranges/  
---  

## **紹介**  

Microsoft Excelでテーブルを作成し、その機能を使用せずにテーブルのデータを保持したい場合があります。代わりに、テーブルのように見えるものが欲しい場合があります。フォーマットを失わずにテーブル内のデータを保持するには、テーブルを通常のデータの範囲に変換します。  
Aspose.Cellsは、テーブルやリストオブジェクトのMicrosoft Excelのこの機能をサポートしています。  

## **Microsoft Excel の使用**  

表をフォーマットを保持したまま範囲に素早く変換するには、**範囲に変換** 機能を使用します。Microsoft Excel 2007/2010では:  

1. 表内のどこかをクリックして、アクティブなセルが表の列内にあることを確認します。  
1. **デザイン** タブの **ツール** グループで、**範囲に変換** をクリックします。  

## **Aspose.Cellsの使用**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

表を範囲に変換した後は、表の機能は利用できなくなります。たとえば、行ヘッダーにはソートとフィルターの矢印が含まれなくなり、数式で使用されたテーブル名を参照する構造化参照は通常のセル参照に変わります。  

{{% /alert %}}  

## **オプションで範囲にテーブルを変換**  

Aspose.Cellsは、[**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) クラスを介してテーブルを範囲に変換する際に追加のオプションを提供します。[**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) クラスは、テーブル行の最後のインデックスを設定できる [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) プロパティを提供します。指定した行インデックスまでテーブルの書式設定が保持され、その後の書式設定が削除されます。  

以下のサンプルコードは、[**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) クラスの使用例を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

