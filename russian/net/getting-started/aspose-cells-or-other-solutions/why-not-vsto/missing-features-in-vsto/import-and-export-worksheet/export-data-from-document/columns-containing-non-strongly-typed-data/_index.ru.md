---
title: Столбцы, содержащие неструктурированные данные
type: docs
weight: 10
url: /ru/net/columns-containing-non-strongly-typed-data/
---

Если все значения в столбцах листа не имеют строго определенного типа (это означает, что значения в столбце могут иметь разные типы данных), то мы можем экспортировать содержимое листа, вызвав метод **ExportDataTableAsString** класса Cells. Метод **ExportDataTableAsString** принимает те же параметры, что и метод **ExportDataTable**, для экспорта данных листа в объект **DataTable**.

{{< highlight csharp >}}

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

Ниже приведены скриншоты:

![todo:image_alt_text](picture1.png)

![todo:image_alt_text](picture2.png)

## **Загрузить образец кода**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
