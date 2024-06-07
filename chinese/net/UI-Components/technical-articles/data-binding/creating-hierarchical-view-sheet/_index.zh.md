---
title: 创建分层视图表
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb,分层
description: 本文介绍了如何在GridWeb中创建分层视图。
---

{{% alert color="primary" %}} 

数据绑定是GridWeb的一个强大且用户友好的功能。 从数据库表中获取的数据填充到一个DataSet中，以表示数据表。使用数据绑定功能，您可以创建一个相互连接的数据的分层视图（主-子视图）并在控件中显示，使其更加优雅。 

本主题讨论了如何创建一个分层视图表。该表中的一些行具有子视图。当用户单击行的“展开”时 

在控件中显示它，以使其更为优雅。 

，则显示它。**存在一个带有分层视图的表格**

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**具有分层视图的表格** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **为数据表创建关系**
例如，您可以使用ADO.Net API从数据库表中提取数据。要创建分层视图表，必须首先设计一个基于某些表的DataSet对象，并在它们之间创建关系。使用VS.NET的**数据集设计器**来创建关系。在

例如，这里有三个数据表：Customers, Orders, Order Details. 表格默认显示所有客户信息。当用户展开客户时，网格显示该客户下的所有订单。当用户展开一个订单时，网格显示该订单的详细信息。数据是分层的：订单详情列在订单下面，订单列在客户下面。 

要使其工作，必须在数据表之间建立以下关系： 

1.在DataTable Orders上创建外键，关键字段为CustomerID 

订单数据中，数据是分层的：订单详细信息列在订单下面，订单则列在顾客下面。

为使此功能生效，数据表之间必须建立如下关系：

1. 在数据表Orders上创建外键，键字段为CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1.在DataTable Order Details上创建外键，关键字段为OrderID。 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



数据集设计器现在如下所示： 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **绑定表**
现在使用**工作表设计器**为工作表设置数据源和数据成员，并配置数据字段绑定列。 

控件会为每一行自动添加一个+图标，该行对应的记录具有子视图。当单击+图标时，记录会展开显示子视图。以下示例使用**工作表设计器**将工作表绑定到根父DataTable Customers。 

自定义子表绑定列 

控件提供了一个名为GridWeb.BindingChildView的事件，开发人员可以使用该事件来自定义子表的绑定列。以下示例 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **自定义子表绑定列**
需要以货币格式显示订单详细信息的**UnitPrice**字段。添加事件处理程序以更改绑定列的数字格式。 

需要以货币格式显示订单详细信息的**UnitPrice**字段。添加事件处理程序以更改绑定列的数字格式。 

**C#**

{{< highlight csharp >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **从数据库加载数据并绑定数据**
从数据库加载数据并绑定
如[在GridWeb的工作表设计器中将工作表绑定到一个数据集](/cells/zh/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/)所述，您需要在Page_Load块中添加代码，从数据库加载数据到DataSet，并在下一步中将DataSet绑定到工作表。 

Asppose.Grid.Web.Data.WebWorksheet类具有一些有用的属性。 

Asppose.Grid.Web.Data.WebWorksheet类具有一些有用的属性。

- 例如，EnableCreateBindColumnHeader属性用于在表格内创建绑定列的标题，或者列

headers显示绑定列名称。它接受true或false。 

- BindStartRow和BindStartColumn属性指定GridWeb控件中源绑定的位置。
- EnableExpandChildView属性用于禁用工作表的展开子视图。默认情况下设置为true。

该类还具有一些有用的方法。 

- DataBind()方法将表格与源绑定。
- CreateNewBindRow()添加一个新行并将其绑定到数据源。
- DeleteBindRow()删除一个绑定行。
- SetRowExpand()方法设置展开的行并在数据绑定模式下显示子视图内容。
- GetRowExpand()方法获取一个布尔值，指示行是否展开。

在下面的代码中，DataSet对象"dataSet21"根据三个表中的数据填充。筛选顾客表以使其成为 

分层显示中的第一个表。创建了一个名为"sheet"的WebWorksheet对象，首先清除该表，然后将其设置为 

链接到数据源。 

**C#**

{{< highlight csharp >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
