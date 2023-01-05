---
title: Импорт из DataTable
type: docs
weight: 40
url: /ru/net/importing-from-datatable/
---
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

workbook.Save("Import From Data Table.xls");

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Import.to.Worksheet.Aspose.Cells.zip)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)
