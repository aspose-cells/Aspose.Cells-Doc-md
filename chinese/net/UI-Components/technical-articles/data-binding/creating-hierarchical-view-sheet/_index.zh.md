---
title: 创建分层视图表单
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb，分层
description: 本文介绍如何在GridWeb中创建分层视图。
---

{{% alert color="primary" %}} 

数据绑定是一项强大且用户友好的GridWeb功能。从数据库表中获取的数据存储在 DataSet 中，并填充数据 

代表数据表。使用数据绑定功能，您可以创建连接数据的分层视图（主-子视图），并 

在控件中显示，使其更加优雅。 

本主题讨论创建分层视图表。表单中的某些行具有子视图。用户单击行的**展开**

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**具有分层视图的表格** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **为DataTable创建关系**
例如，您使用 ADO.Net API 从数据库表中提取数据。要创建分层视图工作表，您必须设计一个基于一些表的 DataSet 对象，并首先在它们之间创建关系。使用 VS.NET 的 **DataSet Designer** 来创建关系。在

这个例子中，有三个 DataTables：Customers、Orders、Order Details。该工作表默认显示所有客户信息。当用户展开客户时，网格显示该客户已经下的所有订单。当用户展开一个订单时，网格显示该订单的详情 

数据是分层的：订单细节在订单下方列出，订单在客户下方列出。 

要使其工作，必须在数据表之间建立以下关系： 

1. 在 DataTable Orders 上创建一个外键，关键字段是 CustomerID

1. 在 DataTable Order Details 上创建一个外键，关键字段是 OrderID。

1. 在 DataTable Orders 上创建一个外键，关键字段是 CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. 在 DataTable Order Details 上创建一个外键，关键字段是 OrderID。 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



现在 DataSet Designer 看起来像这样： 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **绑定工作表**
现在使用 **Worksheets Designer** 来设置工作表的 DataSource 和 DataMember，并配置数据字段绑定列。 

控件会自动为每一行添加一个 + 图标，对应于一个具有子视图的绑定对象的记录（通常是 DataRowView 对象）。当单击 + 图标时，记录会展开显示子视图。下面的示例使用 **Worksheets Designer** 来将工作表绑定到根父 DataTable Customers。 

自定义子表的绑定列 

控件提供了一个名为 GridWeb.BindingChildView 的事件，开发人员可以用它来自定义子表的绑定列。这个示例需要在货币格式中显示订单详情的 **UnitPrice** 字段。添加一个事件处理程序来改变绑定列的数字格式。 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **自定义子表绑定列**
控件提供名为 GridWeb.BindingChildView 的事件，开发人员用于自定义子表的绑定列。本示例 

需要以货币格式显示订单明细的**UnitPrice**字段。添加事件处理程序以更改绑定列的数字格式。 

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

在工作表中实现 GridDesktop 数据绑定功能

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
### **从数据库加载数据并绑定**
如[使用 GridWeb 的工作表设计器将工作表绑定到 DataSet](/cells/zh/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/)中所述，
您需要在 Page_Load 块中添加代码，从数据库加载数据到 DataSet，并在下一步中将 DataSet 绑定到工作表中 

。 

Asppose.Grid.Web.Data.WebWorksheet 类有一些有用的属性。

- 例如，属性 EnableCreateBindColumnHeader 用于在工作表中创建绑定列的标题，或者列标题显示绑定列的名称

。它接受值 true 或 false。 

- 属性 BindStartRow 和 BindStartColumn 指定源应绑定到 GridWeb 控件工作表中的位置。
- 属性 EnableExpandChildView 用于禁用工作表的扩展子视图。默认情况下，它设置为 true。

该类还具有一些有用的方法。 

- DataBind() 方法将工作表与源绑定。
- CreateNewBindRow() 添加新行并将其绑定到数据源。
- DeleteBindRow() 删除绑定行。
- SetRowExpand() 方法设置扩展行并在数据绑定模式下显示子视图内容。
- GetRowExpand() 方法获取表示行是否已展开的布尔值。

在下面的代码中，DataSet 对象 "dataSet21" 基于三个表填充数据。筛选 Customers 表以使其成为分层显示中的第一个表。创建名为 "sheet" 的 WebWorksheet 对象，首先清除工作表，然后将其设置为 

与数据源关联。 

**VB.NET** 

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

在工作表中实现 GridDesktop 数据绑定功能

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
