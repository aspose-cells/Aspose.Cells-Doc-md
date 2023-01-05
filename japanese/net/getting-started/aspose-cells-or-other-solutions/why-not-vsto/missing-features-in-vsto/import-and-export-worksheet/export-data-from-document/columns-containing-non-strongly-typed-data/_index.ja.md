---
title: 厳密に型指定されていないデータを含む列
type: docs
weight: 10
url: /ja/net/columns-containing-non-strongly-typed-data/
---
ワークシートの列のすべての値が厳密に型指定されていない場合 (つまり、列の値のデータ型が異なる可能性があることを意味します)、**ExportDataTableAsString** Cells クラスのメソッド。**ExportDataTableAsString**メソッドは、のと同じパラメータのセットを取ります**ExportDataTable**ワークシートデータをエクスポートするメソッド**データ表**物体。

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

以下はスクリーンショットです。

![todo:画像_代替_文章](picture1.png)

![todo:画像_代替_文章](picture2.png)

## **サンプルコードをダウンロード**

- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
