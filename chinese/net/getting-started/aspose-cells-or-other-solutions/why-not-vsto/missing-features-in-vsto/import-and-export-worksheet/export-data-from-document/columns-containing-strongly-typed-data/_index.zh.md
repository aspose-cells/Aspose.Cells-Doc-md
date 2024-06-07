---
title: 包含强类型数据的列
type: docs
weight: 20
url: /zh/net/columns-containing-strongly-typed-data/
---

我们知道电子表格将数据存储为行和列的序列。如果工作表的列中所有值都是强类型的（也就是说，列中的所有值必须具有相同的数据类型），那么我们就可以通过调用Cells类的ExportDataTable方法导出工作表内容。ExportDataTable方法接受以下参数将工作表数据导出为DataTable对象: 行号，表示将从哪个单元格开始导出数据的行号

- 列号，表示将从哪个单元格开始导出数据的列号
- 行数，表示要导出的行数
- 列数，表示要导出的列数
- 导出列名，一个布尔属性，指示是否应将工作表的第一行数据导出为DataTable的列名

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
