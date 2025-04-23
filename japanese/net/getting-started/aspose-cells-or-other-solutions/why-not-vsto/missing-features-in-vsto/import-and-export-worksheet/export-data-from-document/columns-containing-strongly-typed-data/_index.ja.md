---
title: 強く型付けされたデータを含む列
type: docs
weight: 20
url: /ja/net/columns-containing-strongly-typed-data/
---

スプレッドシートはデータを行と列の連続として保存することを知っています。ワークシートの列のすべての値が強く型付けされている場合（つまり、ワークシートの列のすべての値が同じデータ型でなければならない）、Cells クラスの **ExportDataTable** メソッドを呼び出すことでワークシートの内容をエクスポートできます。**ExportDataTable** メソッドは、**DataTable** オブジェクトとしてワークシートのデータをエクスポートするために次のパラメーターを取ります： **行番号**、データのエクスポートを開始する最初のセルの行番号を表します

- **列番号**、データのエクスポートを開始する最初のセルの列番号を表します
- **行数**、エクスポートする行の数を表します
- **列数**、エクスポートする列の数を表します
- **エクスポートする列名**、ワークシートの最初の行のデータを DataTable の列名としてエクスポートするかどうかを表すブール値プロパティ

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
