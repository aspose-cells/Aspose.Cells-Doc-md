---
title: Столбцы, содержащие строго типизированные данные
type: docs
weight: 20
url: /ru/net/columns-containing-strongly-typed-data/
---

Мы знаем, что таблица Excel хранит данные в виде последовательности строк и столбцов. Если все значения в столбцах листа имеют строго определенный тип (это означает, что все значения в столбце должны иметь один и тот же тип данных), то мы можем экспортировать содержимое листа, вызвав метод **ExportDataTable** класса Cells. Метод **ExportDataTable** принимает следующие параметры для экспорта данных листа в объект **DataTable**: **Номер строки** , представляет номер строки первой ячейки, откуда будут экспортированы данные

- **Номер столбца** , представляет номер столбца первой ячейки, откуда будут экспортированы данные
- **Количество строк** , представляет количество строк для экспорта
- **Количество столбцов** , представляет количество столбцов для экспорта
- **Экспортировать названия столбцов** , логическое свойство, указывающее, должны ли данные в первой строке листа быть экспортированы как названия столбцов DataTable или нет

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
