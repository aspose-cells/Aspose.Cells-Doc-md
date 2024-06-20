---
title: Импорт экспорт данных из документа
type: docs
weight: 10
url: /ru/net/import-export-data-from-document/
---

## **Импортировать данные из документа**

Данные - это набор исходных фактов, и мы создаем таблицы электронных документов или отчеты для представления этих исходных фактов более осмысленным образом. Обычно мы добавляем данные в таблицы электронных документов сами, но иногда нам нужно повторно использовать существующие ресурсы данных, и здесь возникает необходимость импортировать данные в таблицы электронных документов из различных источников данных. В этой теме мы рассмотрим некоторые техники импорта данных на рабочие листы из различных источников данных.

## **Импорт данных с использованием Aspose.Cells**

Когда вы используете **Aspose.Cells** для открытия Excel-файла, все данные в файле автоматически импортируются, но Aspose.Cells также поддерживает импорт данных из различных источников данных. Ниже приведены некоторые из этих источников данных:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells предоставляет класс **Workbook**, который представляет собой файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cells.

Коллекция Cells предоставляет очень полезные методы для импорта данных из различных источников данных.

### **Импорт из массива**

Разработчики могут импортировать данные из массива в их листы, вызвав метод **ImportArray** коллекции Cells. Есть множество версий перегруженного метода ImportArray, но типичная перегрузка принимает следующие параметры:

- Массив, представляет объект массива, который необходимо импортировать
- Номер строки, представляет номер строки первой ячейки, куда будут импортированы данные
- Номер столбца, представляет номер столбца первой ячейки, куда будут импортированы данные
- Вертикальная ориентация, логическое значение, указывающее, импортировать данные вертикально или горизонтально

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Импорт из ArrayList**

Разработчики могут импортировать данные из ArrayList в их листы, вызвав метод **ImportArrayList** коллекции Cells. Метод ImportArray принимает следующие параметры: **ArrayList** , представляет объект ArrayList, чьи содержимое нужно импортировать

- Номер строки , представляет номер строки первой ячейки, куда будут импортированы данные
- Номер столбца , представляет номер столбца первой ячейки, куда будут импортированы данные
- Это вертикальное, логическое значение, которое указывает импортировать данные вертикально или горизонтально

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **Импорт из пользовательских объектов**

Разработчики могут импортировать данные из коллекции объектов в лист Excel с использованием **ImportCustomObjects**. Вы можете предоставить список столбцов/свойств для метода, чтобы отобразить ваш список желаемых объектов.

{{< highlight csharp >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **Импорт из DataTable**

Разработчики могут импортировать данные из **DataTable** в свои листы Excel, вызывая метод **ImportDataTable** из коллекции Cells. Существует множество перегруженных версий метода **ImportDataTable**, но типичная перегрузка принимает следующие параметры: **DataTable**, представляет объект **DataTable**, содержимое которого необходимо импортировать.

- **Показывать название поля**, указывает, должны ли имена столбцов DataTable быть импортированы ​​в лист Excel ​​как первая строка или нет
- **Начальная ячейка**, представляет имя начальной ячейки (т. е. "A1") для импорта содержимого DataTable

{{< highlight csharp >}}

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

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Загрузить образец кода**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Экспорт данных из документа**

Aspose.Cells позволяет не только импортировать данные на рабочие листы из внешних источников данных, но также позволяет экспортировать данные рабочего листа в **DataTable**. Как известно, **DataTable** является частью ADO.NET и используется для хранения данных. После того как данные сохранены в **DataTable**, их можно использовать любым образом в соответствии с требованиями пользователей.

## **Экспорт данных в DataTable (.NET) с помощью Aspose.Cells**

Разработчики могут легко экспортировать данные рабочего листа в объект DataTable, вызвав метод ExportDataTable или ExportDataTableAsString класса Cells. Оба метода используются в различных сценариях, которые подробно обсуждаются ниже.

### **Столбцы, содержащие строго типизированные данные**

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

### **Столбцы, содержащие нестрого типизированные данные**

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

## **Загрузить образец кода**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
