---
title: Группировка данных
type: docs
weight: 10
url: /ru/net/grouping-data/
---
В некоторых отчетах Excel может потребоваться разбить данные на группы, чтобы их было легче читать и анализировать. Одной из основных целей разбиения данных на группы является выполнение вычислений (выполнение сводных операций) для каждой группы записей.

Смарт-маркеры Aspose.Cells позволяют группировать данные по полям и размещать сводные строки между наборами данных или группами данных. Например, при группировке данных по Customers.CustomerID можно добавлять сводную запись при каждом изменении группы.

В приведенных ниже примерах фрагментов кода показано, как сгруппировать данные в отчете Excel с помощью интеллектуальных маркеров.
## **Параметры**
Ниже приведены некоторые параметры интеллектуальных маркеров, используемые для группировки данных.
**группа:нормальная/объединить/повторить**

Мы поддерживаем три типа групп, которые вы можете выбрать.

- normal - значение группы по полю(ям) не повторяется для соответствующих записей в столбце; вместо этого они печатаются один раз для каждой группы данных.
- слияние — то же поведение, что и для обычного параметра, за исключением того, что он объединяет ячейки в группе по полю (полям) для каждого набора групп.
- Repeat — группировка по значению поля (полей) повторяется для соответствующих записей.

Если у вас несколько параметров, разделите их запятыми, но без пробела: параметр A, параметр B, параметр C.
### **Пример**
В этом примере показаны некоторые параметры группировки в действии. Он использует базу данных доступа Northwind.mdb Microsoft и извлекает данные из таблицы с именем «Сведения о заказе». Мы создаем файл конструктора с именем SmartMarker_Designer.xls в Microsoft Excel и помещаем смарт-маркеры в различные ячейки рабочих листов. Маркеры обрабатываются для заполнения рабочих листов. Данные размещаются и организуются по групповому полю.

Файл конструктора состоит из двух рабочих листов. В первую ставим умные маркеры с параметрами группировки, как показано на скриншоте ниже. Размещаются три смарт-маркера (с параметрами группировки):
&=Детали заказа.OrderID(группа:слияние,пропустить:1),
&=Сведения о заказе.Количество(подытог9:Сведения о заказе.Идентификатор заказа) и
&=Сведения о заказе.Цена за единицу (промежуточный итог9:Сведения о заказе.Идентификатор заказа) входят в A5, B5 и C5 соответственно.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Grouping Data OLE DB.xlsx";

//Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=~\\..\\..\\..\\Data\\Northwind.mdb");

//Open the connection object.

con.Open();

//Create a command object and specify the SQL query.

OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

//Create a data adapter object.

OleDbDataAdapter da = new OleDbDataAdapter();

//Specify the command.

da.SelectCommand = cmd;

//Create a dataset object.

DataSet ds = new DataSet();

//Fill the dataset with the table records.

da.Fill(ds, "Order Details");

//Create a datatable with respect to dataset table.

DataTable dt = ds.Tables["Order Details"];

//Create WorkbookDesigner object.

WorkbookDesigner wd = new WorkbookDesigner();

//Open the template file (which contains smart markers).

wd.Workbook = new Workbook(FileName);

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save(FileName);

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
