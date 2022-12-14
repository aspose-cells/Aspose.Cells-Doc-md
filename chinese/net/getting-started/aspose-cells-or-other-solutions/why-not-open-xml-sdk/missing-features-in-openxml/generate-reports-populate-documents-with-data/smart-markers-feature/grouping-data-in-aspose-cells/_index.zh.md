---
title: 分组数据在 Aspose.Cells
type: docs
weight: 10
url: /zh/net/grouping-data-in-aspose-cells/
---
在某些 Excel 报告中，您可能需要将数据分组以使其更易于阅读和分析。将数据分组的主要目的之一是对每组记录运行计算（执行汇总操作）。

Aspose.Cells 智能标记允许您按字段对数据进行分组，并在数据集或数据组之间放置摘要行。例如，如果按 Customers.CustomerID 对数据进行分组，您可以在每次组更改时添加一条摘要记录。

下面的示例代码片段显示了如何使用智能标记对 Excel 报告中的数据进行分组。
## **参数**
以下是一些用于分组数据的智能标记参数。
**组：正常/合并/重复**

我们支持三种类型的组，您可以在其中进行选择。

- normal - group by field(s) 值不会对列中的相应记录重复；相反，它们每个数据组打印一次。
- merge - 与 normal 参数相同的行为，除了它按每个组集的字段合并组中的单元格。
- repeat - 对相应记录重复按字段分组的值。

如果您有多个参数，请用逗号分隔它们，但不要使用空格：parameterA,parameterB,parameterC
### **例子**
此示例显示了一些实际的分组参数。它使用 Northwind.mdb Microsoft Access 数据库并从名为“Order Details”的表中提取数据。我们在 Microsoft Excel 中创建一个名为 SmartMarker_Designer.xls 的设计器文件，并将智能标记放入工作表中的各个单元格中。处理标记以填充工作表。数据按组字段放置和组织。

设计器文件有两个工作表。首先，我们放置带有分组参数的智能标记，如下面的屏幕截图所示。放置了三个智能标记（带有分组参数）：
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID), and
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID)分别进入A5、B5、C5。

{{< highlight "csharp" >}}

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
## **下载示例代码**
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
