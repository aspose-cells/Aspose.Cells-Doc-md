---
title: Столбцы, содержащие не строго типизированные данные
type: docs
weight: 10
url: /ru/net/columns-containing-non-strongly-typed-data/
---
 Если все значения в столбцах рабочего листа не являются строго типизированными (это означает, что значения в столбце могут иметь разные типы данных), мы можем экспортировать содержимое рабочего листа, вызвав метод**Экспортдататаблеасстринг** метод класса Cells.**Экспортдататаблеасстринг** метод принимает тот же набор параметров, что и**Таблица ЭкспортДанных** метод экспорта данных рабочего листа как**Таблица данных** объект.

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

Ниже приведены скриншоты:

![дело:изображение_альтернативный_текст](picture1.png)

![дело:изображение_альтернативный_текст](picture2.png)

## **Скачать пример кода**

- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
