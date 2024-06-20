---
title: Группировка данных в Aspose.Cells
type: docs
weight: 10
url: /ru/net/grouping-data-in-aspose-cells/
---

В некоторых отчетах Excel может потребоваться разбить данные на группы для удобства их чтения и анализа. Одной из основных целей разделения данных на группы является выполнение расчетов (выполнение сводных операций) для каждой группы записей.

Умные маркеры Aspose.Cells позволяют группировать ваши данные по полю(полям) и размещать сводные строки между наборами данных или группами данных. Например, если группировать данные по Customers.CustomerID, можно добавить сводную запись каждый раз, когда меняется группа.

Приведенные ниже фрагменты кода примеров показывают, как группировать данные в отчете Excel с использованием умных маркеров.
## **Параметры**
Ниже приведены некоторые параметры умного маркера, используемые для группировки данных.
**group:normal/merge/repeat**

Мы поддерживаем три типа групп, из которых вы можете выбрать.

- normal - Значение поля(полей) группировки не повторяется для соответствующих записей в столбце; вместо этого оно печатается один раз для каждой группы данных.
- merge - То же поведение, что и для параметра normal, за исключением того, что он объединяет ячейки в поле(полях) группировки для каждого набора групп.
- repeat - Значение поля(полей) группировки повторяется для соответствующих записей.

Если у вас есть несколько параметров, разделите их запятыми, но без пробела: параметрА,параметрB,параметрC
### **Пример**
В этом примере показано некоторые из параметров группировки в действии. Он использует базу данных Microsoft Access Northwind.mdb и извлекает данные из таблицы с именем "Order Details". Мы создаем файл дизайнера с именем SmartMarker_Designer.xls в Microsoft Excel и размещаем умные маркеры в различные ячейки на листах. Маркеры обрабатываются для заполнения листов. Данные размещаются и организуются по полю группы.

В файле дизайнера два листа. На первом мы размещаем умные маркеры с параметрами группировки, как показано на скриншоте ниже. Три умных маркера (с параметрами группировки) размещены:
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID), и
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) помещаются в A5, B5 и C5 соответственно.

{{< highlight csharp >}}

 //Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

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

wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save("outSmartMarker_Designer.xls");

{{< /highlight >}}
## **Загрузить образец кода**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
