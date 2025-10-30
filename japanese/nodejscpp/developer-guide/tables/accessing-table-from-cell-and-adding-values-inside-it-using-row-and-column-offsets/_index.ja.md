---  
title: セルからテーブルにアクセスし、行と列のオフセットを使って値を追加するNode.jsをC++経由での方法  
linktitle: セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加する  
type: docs  
weight: 230  
url: /ja/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

通常、テーブルまたはリストオブジェクト内に値を追加する場合は [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) メソッドを使用します。ただし、時々、行と列のオフセットを使用してテーブルまたはリストオブジェクト内に値を追加する必要があることがあります。  

セルからテーブルまたはリストオブジェクトにアクセスするには[**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)メソッドを使用します。値を追加するには、行と列のオフセットを使用して[**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)メソッドを利用します。  

{{% /alert %}}  

以下のスクリーンショットは、コード内で使用されるソースExcelファイルを示しています。空のテーブルが含まれ、テーブル内のセルD5がハイライトされています。このテーブルにセルD5からアクセスし、[**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)メソッドを使用して値を追加し、その後[**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)および[**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)メソッドを使って値を追加します。  

## 例  

### ソースファイルと出力ファイルの比較のスクリーンショット  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

以下のスクリーンショットは、コードによって生成された出力エクセルファイルを示しています。セル D5 に値が設定されており、テーブル内のオフセット 2,2 のセル F6 にも値が設定されています。  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加するNode.jsコード  

以下のサンプルコードは、上記のスクリーンショットに示されているソースエクセルファイルを読み込み、テーブル内に値を追加し、それに基づいて出力エクセルファイルを生成します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
