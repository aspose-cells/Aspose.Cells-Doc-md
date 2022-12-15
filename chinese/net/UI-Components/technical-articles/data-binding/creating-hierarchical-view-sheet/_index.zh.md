---
title: 创建分层视图表
type: docs
weight: 30
url: /zh/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

数据绑定是一个强大且用户友好的 GridWeb 特性。存储在数据库表中的数据被提取到数据集中并填充数据

表示数据表。使用数据绑定功能，您可以创建互连数据的分层视图（主子视图）和

将其显示在控件中，使其更加优雅。

本主题讨论创建分层视图表。工作表中的某些行具有子视图。当用户单击该行的**扩张**

按钮{{< emoticons/cross >}}，该行的子视图表向下展开。此功能对于构建分层视图报表非常有帮助。

**具有层次视图的表** 

![待办事项：图像_替代_文本](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **为数据表创建关系**
例如，您使用 ADO.Net API 并从数据库表中提取数据。要创建分层视图表，您必须设计一个数据集

基于一些表的对象，并首先在它们之间创建关系。使用VS.NET的**数据集设计器**创建关系。在

这个例子中，有三个DataTable：Customers、Orders、Order Details。该工作表默认显示所有客户信息。什么时候

用户展开一个客户，网格显示该客户下的所有订单。当用户展开订单时，网格显示详细信息

那个订单。数据是分层的：订单详细信息列在订单下，订单列在客户下。

为此，必须在数据表之间建立以下关系：

1. 在DataTable Orders上创建外键，键字段为CustomerID

![待办事项：图像_替代_文本](creating-hierarchical-view-sheet_2.png)




1. 在DataTable Order Details上创建外键，键字段为OrderID。

![待办事项：图像_替代_文本](creating-hierarchical-view-sheet_3.png)



数据集设计器现在看起来像这样：

![待办事项：图像_替代_文本](creating-hierarchical-view-sheet_4.png)
### **绑定工作表**
现在使用**工作表设计器**为工作表设置DataSource和DataMember，并配置数据字段绑定列。

该控件会自动为对应于其绑定对象（通常是 DataRowView 对象）具有的记录的每一行添加一个 + 图标

孩子的意见。单击 + 图标时，记录会展开以显示子视图。下面的示例使用**工作表设计器**绑定

工作表到根父 DataTable Customers。

![待办事项：图像_替代_文本](creating-hierarchical-view-sheet_5.png)
### **自定义子表绑定列**
该控件提供了一个名为 GridWeb.BindingChildView 的事件，开发人员使用该事件自定义子表的绑定列。这个例子

需要显示订单详情'**单价**货币格式的字段。添加事件处理程序以更改绑定列的数字格式。

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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
如中所述[使用 GridWeb 的工作表设计器将工作表绑定到数据集](/cells/zh/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
您需要将代码添加到 Page_Load 块以将数据从数据库加载到 DataSet，并将 DataSet 绑定到

下一步。

Aspose.Grid.Web.Data.WebWorksheet 类有一些有用的属性。

- 例如，属性 EnableCreateBindColumnHeader 用于在工作表或列中创建绑定列的标题

headers 显示绑定的列名称。它需要值**真的**或者**错误的**. 

- 属性 BindStartRow 和 BindStartColumn 指定源应绑定到的 GridWeb 控件工作表中的位置。
- 属性 EnableExpandChildView 用于禁用工作表的展开子视图。默认情况下，它设置为 true。

该类也有一些有用的方法。

- DataBind() 方法将工作表与源绑定。
- CreateNewBindRow() 添加一个新行并将其绑定到数据源。
- DeleteBindRow() 删除绑定行。
- SetRowExpand() 方法设置展开的行并以数据绑定方式显示子视图内容。
- GetRowExpand() 方法获取一个布尔值，指示该行是否展开。

在下面的代码中，DataSet 对象“dataSet21”填充了基于三个表的数据。 Customers 表被过滤，使其成为

分层显示中的第一个表。创建一个名为“sheet”的WebWorksheet对象，先清除sheet再设置

链接到数据源。

**C#**

{{< highlight "csharp" >}}

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

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

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

{{< highlight "csharp" >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) 处理 MyBase.Load

 '在这里放置用户代码来初始化页面

如果不是 IsPostBack 那么

BindWithoutInSheetHeaders()

万一

结束子

Private Sub BindWithoutInSheetHeaders()

 Dim db As DemoDatabase2 = New DemoDatabase2()

昏暗路径 As String = MapPath(".")

 path = path.Substring(0, path.LastIndexOf("\"))

 path = path.Substring(0, path.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

尝试

' 连接到数据库并获取数据。

 ' 客户表。

 db.OleDbDataAdapter1.Fill(DataSet21)

 ' 订单表。

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' 订单明细表。

 db.OleDbDataAdapter3.Fill(DataSet21)

 '过滤数据

DataSet21.Customers.DefaultView.RowFilter = "客户ID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

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
