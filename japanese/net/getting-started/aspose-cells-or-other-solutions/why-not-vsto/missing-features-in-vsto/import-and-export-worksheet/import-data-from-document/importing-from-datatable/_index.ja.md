---
title: DataTable からのインポート
type: docs
weight: 40
url: /ja/net/importing-from-datatable/
---
開発者は、**データ表**を呼び出してワークシートに**ImportDataTable**Cells コレクションのメソッド。には多くのオーバーロードされたバージョンがあります**ImportDataTable**メソッドですが、典型的なオーバーロードは次のパラメーターを取ります。**データ表**は、**データ表**コンテンツをインポートする必要があるオブジェクト

- **フィールド名は表示されますか**は、DataTable の列の名前を最初の行としてワークシートにインポートするかどうかを指定します
- **スタート Cell**は、DataTable の内容をインポートする開始セル (つまり "A1") の名前を表します

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save("Import From Data Table.xls");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Import.to.Worksheet.Aspose.Cells.zip)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)
