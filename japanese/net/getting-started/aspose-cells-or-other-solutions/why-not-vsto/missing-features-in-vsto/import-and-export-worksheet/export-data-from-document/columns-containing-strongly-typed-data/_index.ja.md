---
title: 厳密に型指定されたデータを含む列
type: docs
weight: 20
url: /ja/net/columns-containing-strongly-typed-data/
---
スプレッドシートはデータを一連の行と列として保存することがわかっています。ワークシートの列のすべての値が厳密に型指定されている場合 (つまり、列のすべての値が同じデータ型である必要があることを意味します)、**ExportDataTable** Cells クラスのメソッド。**ExportDataTable**メソッドは、次のパラメーターを使用して、ワークシート データを次のようにエクスポートします。**データ表**物体：**行番号** 、データがエクスポートされる最初のセルの行番号を表します

- **列番号**、データがエクスポートされる最初のセルの列番号を表します
- **行の数**、エクスポートする行数を表します
- **列の数**、エクスポートする列の数を表します
- **列名のエクスポート**、ワークシートの最初の行のデータを DataTable の列名としてエクスポートするかどうかを示すブール プロパティ

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
