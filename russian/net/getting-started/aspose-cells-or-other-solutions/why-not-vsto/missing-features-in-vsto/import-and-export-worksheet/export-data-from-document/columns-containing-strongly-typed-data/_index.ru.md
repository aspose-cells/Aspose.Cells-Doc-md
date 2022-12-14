---
title: Столбцы, содержащие строго типизированные данные
type: docs
weight: 20
url: /ru/net/columns-containing-strongly-typed-data/
---
 Мы знаем, что электронная таблица хранит данные в виде последовательности строк и столбцов. Если все значения в столбцах рабочего листа строго типизированы (это означает, что все значения в столбце должны иметь один и тот же тип данных), мы можем экспортировать содержимое рабочего листа, вызвав метод**Таблица ЭкспортДанных** метод класса Cells.**Таблица ЭкспортДанных** метод принимает следующие параметры для экспорта данных листа как**Таблица данных** объект:**Номер строки** , представляет номер строки первой ячейки, из которой будут экспортированы данные.

- **Номер столбца** , представляет номер столбца первой ячейки, из которой будут экспортированы данные
- **Количество рядов** , представляет количество строк для экспорта
- **Число столбцов** представляет количество столбцов для экспорта
- **Экспорт имен столбцов** , логическое свойство, указывающее, следует ли экспортировать данные в первой строке рабочего листа как имена столбцов таблицы данных или нет.

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
