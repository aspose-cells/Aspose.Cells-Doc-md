---
title: 数据分组
type: docs
weight: 10
url: /zh/net/grouping-data/
---

在一些 Excel 报告中，您可能需要将数据分成组，以便更容易阅读和分析。将数据分成组的主要目的之一是对每组记录运行计算（执行摘要操作）。

Aspose.Cells 智能标记允许您按字段对数据进行分组，并在数据集或数据组之间放置汇总行。例如，如果按 Customers.CustomerID 对数据进行分组，则每次分组更改时，都可以添加汇总记录。

接下来的示例代码片段演示了如何使用智能标记在 Excel 报告中进行数据分组。
## **参数**
以下是用于数据分组的一些智能标记参数。
**group:normal/merge/repeat**

我们支持三种您可以选择的分组类型。

- normal - 不会为相应记录中的字段值重复打印对应的分组；相反，它们将在每个数据组中打印一次。
- merge - 与 normal 参数的行为相同，但它会合并每个组集中的分组字段中的单元格。
- repeat - 为相应记录中的字段值重复打印对应的分组。

如果有多个参数，请用逗号分隔它们，但不要有空格：parameterA,parameterB,parameterC
### **示例**
此示例展示了一些分组参数的实际应用。它使用了 Northwind.mdb Microsoft Access 数据库，并从名为 "Order Details" 的表中提取数据。我们在 Microsoft Excel 中创建了一个名为 SmartMarker_Designer.xls 的设计文件，并在工作表的各种单元格中放置智能标记。然后对标记进行处理以填充工作表。数据是通过一个组字段放置和组织的。

设计文件有两个工作表。在第一个工作表中，我们像下面的截图所示，使用了带有分组参数的智能标记。我们放置了三个带有分组参数的智能标记：
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID)，以及
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) 分别放入 A5、B5 和 C5。

{{< highlight csharp >}}

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
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
