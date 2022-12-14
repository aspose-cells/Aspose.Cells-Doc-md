---
title: Импорт Экспорт данных из документа
type: docs
weight: 10
url: /ru/net/import-export-data-from-document/
---
## **Импорт данных из документа**

Данные — это набор необработанных фактов, и мы создаем электронные таблицы или отчеты, чтобы представить эти необработанные факты в более осмысленном виде. Обычно мы сами добавляем данные в электронные таблицы, но иногда нам нужно повторно использовать существующие ресурсы данных, и здесь возникает необходимость импортировать данные в электронные таблицы из разных источников данных. В этом разделе мы обсудим некоторые методы импорта данных на рабочие листы из разных источников данных.

## **Импорт данных с помощью Aspose.Cells**

 Когда вы используете**Aspose.Cells** чтобы открыть файл Excel, все данные в файле импортируются автоматически, но Aspose.Cells также поддерживает импорт данных из разных источников данных. Некоторые из этих источников данных перечислены ниже:

- **Множество**
- **ArrayList**
- **Таблица данных**
- **столбец данных**
- **Просмотр данных**
- **DataGrid**
- **DataReader**
- **Вид сетки**

 Aspose.Cells предоставляет класс,**Рабочая тетрадь** который представляет файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cells.

Коллекция Cells предоставляет очень полезные методы для импорта данных из разных источников данных.

### **Импорт из массива**

 Разработчики могут импортировать данные из массива на свои рабочие листы, вызвав метод**ИмпортМассив** метод коллекции Cells. Существует много перегруженных версий метода ImportArray, но типичная перегрузка принимает следующие параметры:

- Массив представляет объект массива, содержимое которого необходимо импортировать.
- Номер строки представляет собой номер строки первой ячейки, в которую будут импортированы данные.
- Номер столбца, представляет номер столбца первой ячейки, в которую будут импортированы данные.
- Вертикально, логическое значение, указывающее, импортировать ли данные вертикально или горизонтально.

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Импорт из ArrayList**

 Разработчики могут импортировать данные из списка ArrayList в свои рабочие листы, вызвав метод**Импортмассивлист** метод коллекции Cells. Метод ImportArray принимает следующие параметры:**ArrayList** , представляет объект ArrayList, содержимое которого необходимо импортировать

- Номер строки представляет собой номер строки первой ячейки, в которую будут импортированы данные.
- Номер столбца представляет номер столбца первой ячейки, в которую будут импортированы данные.
- Является Вертикальным логическим значением, указывающим на импорт данных по вертикали или по горизонтали.

{{< highlight "csharp" >}}

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

 Разработчики могут импортировать данные из коллекции объектов на рабочий лист, используя**Импорт пользовательских объектов**. Вы можете предоставить список столбцов/свойств методу для отображения желаемого списка объектов.

{{< highlight "csharp" >}}

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

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

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

 Разработчики могут импортировать данные из**Таблица данных** к своим рабочим листам, позвонив в**Таблица ИмпортДанных** метод коллекции Cells. Существует множество перегруженных версий**Таблица ИмпортДанных** метод, но типичная перегрузка принимает следующие параметры:**Таблица данных** , представляет**Таблица данных** объект, содержимое которого нужно импортировать

- **Отображается ли имя поля**, указывает, следует ли импортировать имена столбцов DataTable на лист в качестве первой строки или нет.
- **Начало Cell** представляет имя начальной ячейки (например, «A1»), откуда импортируется содержимое DataTable.

{{< highlight "csharp" >}}

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

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Скачать пример кода**

- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Экспорт данных из документа**

 Aspose.Cells не только облегчает пользователям импорт данных в рабочие листы из внешних источников данных, но также позволяет им экспортировать данные своих рабочих листов в**Таблица данных** . Как мы знаем, что**Таблица данных** является частью ADO.NET и используется для хранения данных. Как только данные сохраняются в**Таблица данных**, его можно использовать любым способом в соответствии с требованиями пользователей.

## **Экспорт данных в DataTable (.NET) с использованием Aspose.Cells**

Разработчики могут легко экспортировать данные своего рабочего листа в объект DataTable, вызвав метод ExportDataTable или ExportDataTableAsString класса Cells. Оба метода используются в разных сценариях, которые более подробно обсуждаются ниже.

### **Столбцы, содержащие строго типизированные данные**

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

### **Столбцы, содержащие не строго типизированные данные**

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

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
