---
title: 包含非强类型数据的列
type: docs
weight: 10
url: /zh/net/columns-containing-non-strongly-typed-data/
---
如果工作表列中的所有值都不是强类型的（这意味着列中的值可能具有不同的数据类型），那么我们可以通过调用导出工作表内容**ExportDataTableAsString** Cells 类的方法。**ExportDataTableAsString**方法采用与**导出数据表**将工作表数据导出为的方法**数据表**目的。

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

以下是屏幕截图：

![待办事项：图片_替代_文本](picture1.png)

![待办事项：图片_替代_文本](picture2.png)

## **下载示例代码**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
