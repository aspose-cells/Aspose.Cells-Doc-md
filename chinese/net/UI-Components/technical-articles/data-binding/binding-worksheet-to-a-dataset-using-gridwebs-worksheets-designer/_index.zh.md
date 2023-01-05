---
title: 使用 GridWebs 工作表设计器将工作表绑定到数据集
type: docs
weight: 20
url: /zh/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

本文讨论了一种使用 Aspose.Cells.GridWeb（工作表设计器）提供的特殊工具以 GUI 模式将工作表绑定到数据库表的简单方法。

{{% /alert %}} 
## **使用工作表设计器将工作表与数据库绑定**
	**第 1 步：创建示例数据库**
1. 首先，我们创建将在本文中使用的示例数据库。我们正在使用 Microsoft Access 创建一个数据库，其中包含一个名为 Products 的表。它的架构如下所示。
   **Products表的设计信息** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Products 表中添加了一些虚拟记录。
   **产品表中的记录** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **第 2 步：设计示例应用程序**
在 Visual Studio.NET 中创建和设计了一个 ASP.NET Web 应用程序，如下所示。
**设计的示例应用程序** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **第 3 步：使用服务器资源管理器连接数据库**
是时候连接到数据库了。我们可以使用 Visual Studio.NET 中的服务器资源管理器轻松完成。

1. 选择**数据连接**在**服务器资源管理器**并右击。
1. 选择**添加连接**从菜单中。
   **选择添加连接选项** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



显示数据链接属性对话框。
**数据链接属性对话框** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



使用此对话框，您可以连接到任何数据库。默认情况下，它允许您连接到 SQL Server 数据库。对于此示例，我们需要连接 Microsoft Access 数据库。

1. 点击**供应商**标签。
1. 选择**Microsoft Jet 4.0 OLE DB 提供程序**来自**OLE DB 供应商**列表。
1. 点击**下一个**.
   **选择 OLE DB 提供程序后单击下一步** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


这**联系**标签页打开。

1. 选择 Microsoft Access 数据库文件（在我们的示例中为 db.mdb）并单击**好的**.
   **选择数据库文件后单击确定按钮** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

点击后**好的** 将在 Microsoft Access 数据库中创建数据库连接**服务器资源管理器**.双击连接可以看到数据库中的所有表、视图和存储过程。

{{% /alert %}} 
### **第 4 步：以图形方式创建数据库连接对象**
1. 使用浏览数据库中的表**服务器资源管理器**.
只有一张表，Products。
1. 将 Products 表从**服务器资源管理器**到**网页表格**.
   **将 Products 表从 Server Explorer 拖放到 Web 表单** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



可能会出现一个对话框。
**确认在连接字符串中包含数据库密码的对话框** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



决定是否要在连接字符串中包含数据库密码。对于这个例子，我们选择**不包括密码**. 
已创建并添加了两个数据库连接对象（oleDbConnection1 和 oleDbDataAdapter1）。
**创建并显示数据库连接对象 (oleDbConnection1 & oleDbDataAdapter1)** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **第五步：生成数据集**
到目前为止，我们已经创建了数据库连接对象，但在连接到数据库后仍然需要在某个地方存储数据。 DataSet 对象可以精确存储数据，我们也可以使用 VS.NET IDE 轻松生成它。

1. 选择**oleDbDataAdaper1**并右击。
1. 选择**生成数据集**菜单中的选项。
   **选择生成数据集选项** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



显示生成数据集对话框。
在这里，可以为要创建的新 DataSet 对象选择一个名称，以及应该向其中添加哪些表。

1. 选择**将此数据集添加到设计器**选项。
1. 点击**好的**.
   **单击确定按钮生成数据集** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



dataSet11 对象被添加到设计器中。
**生成数据集并添加到设计器** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **第 6 步：使用工作表设计器**
现在，是时候揭开秘密了。

1. 选择 GridWeb 控件并单击鼠标右键。
1. 选择**工作表设计器**菜单中的选项。

   **选择工作表设计器选项** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



显示工作表集合编辑器（也称为工作表设计器）。
**工作表集合编辑器对话框** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



该对话框包含多个属性，可以配置这些属性以将 Sheet1 绑定到数据库中的任何表。

1. 选择**数据源**财产。
菜单上列出了上一步中生成的 dataSet11 对象。
1. 选择数据集 11。
1. 点击**数据成员**财产。
 Worksheets Designer 自动显示 dataSet11 中的表列表。只有一张表，Products。
1. 选择产品表。
   **设置数据源和数据成员属性** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. 检查**绑定列**财产。
   **单击 BindColumns 属性** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



点击**绑定列**属性打开 BindColumn 集合编辑器。
**BindColumn 集合编辑器** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



在 BindColumn 集合编辑器中，所有列的**产品**表会自动添加到 BindColumns 集合中。

1. 选择任意列并自定义其属性。
例如，您可以修改每个列的标题。
   **修改 ProductID 列的 Caption** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. 进行更改后，单击**好的**.
1. 通过单击关闭所有对话框**好的**.
最后，您将返回到 WebForm1.aspx 页面。
   **使用工作表设计器后返回 WebForm1.aspx 页面** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


上面显示了 Products 表的列名称。列的宽度很小，因此某些列的完整名称不完全可见。
### **第 7 步：将代码添加到 Page_Load 事件处理程序**
我们已经使用了 Worksheets Designer，现在只需将代码添加到 Page_Load 事件处理程序，以便用数据库中的数据填充 dataSet11 对象（使用 oleDbDataAdapter1）并通过调用其 DataBind 方法将 GridWeb 控件绑定到 dataSet11。

1. 添加代码：

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing Page_Load event handler

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub



{{< /highlight >}}

1. 检查添加到 Page_Load 事件处理程序的代码。
   **添加到 Page_Load 事件处理程序的代码** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **第 8 步：运行应用程序**
编译并运行应用程序：或者按**Ctrl+F5**或点击**开始**. 
**运行应用程序** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



编译后，WebForm1.aspx 页面在浏览器窗口中打开，其中包含从数据库加载的所有数据。
**从数据库加载到 GridWeb 控件的数据** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **使用 GridWeb 控件**
当数据加载到 GridWeb 控件时，它为用户提供了对数据的控制。 GridWeb 提供了许多不同类型的数据操作功能。
### **数据验证**
Aspose.Cells.GridWeb 根据数据库中定义的数据类型自动为所有绑定列创建适当的验证规则。通过将光标悬停在单元格上来查看单元格的验证类型。
**检查单元格的验证类型** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

此处，所选单元格包含**<内部>**验证，这意味着用户只能向其中输入整数值。如果他们输入另一个值，则会发生验证错误。而且，**<必填>**显示必须提交值 Product ID。
### **删除行**
要删除一行，请选择一行（或行中的任何单元格），右键单击并选择**删除行**.
**从菜单中选择删除行选项** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


该行将立即被删除。
**网格数据（删除一行后）** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **编辑行**
编辑单元格或行中的数据，然后单击**救球**要么**提交**保存更改。
### **添加行**
1. 要添加一行，请右键单击一个单元格并选择**添加行**.
   **从菜单中选择添加行选项** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



新行将添加到工作表中其他行的末尾。
**新行添加到网格** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



新行的左边是一个星号{{< emoticons/cross >}} 表明该行是新的。

1. 将值添加到新行。
1. 点击**救球**要么**提交**确认更改。
   **单击 *Save 保存对数据的更改**按钮*

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **设置数字格式**
目前，价格在**产品价格**列显示为数值。可以使它们看起来像货币。

1. 返回到 Visual Studio.NET。
1. 打开 BindColumn 集合编辑器。
这**数字类型**的财产**产品价格**列设置为**一般的**.
   **NumberType 属性设置为常规** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. 点击**下拉列表**并选择**货币4**从列表中。
   **NumberType 属性更改为 Currency4** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. 再次运行应用程序。
中的值**产品价格**列现在是货币。
   **产品价格货币数字格式** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **编辑数据**
到目前为止，该应用程序仅允许其用户查看表数据。用户可以在 GridWeb 控件中编辑数据，但是当关闭浏览器并打开数据库时，没有任何改变。所做的更改不会保存到数据库中。

以下示例将代码添加到应用程序，以便 GridWeb 可以保存对数据库的更改。

1. 打开**特性**窗格并从列表中选择 GridWeb 控件的 SaveCommand 事件。
   **选择 GridWeb 的 SaveCommand 事件** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. 双击**保存命令**事件和 VS.NET 创建 GridWeb1_SaveCommand 事件处理程序。
1. 将代码添加到此事件处理程序，它将使用 oleDbDataAdapter1 绑定到工作表的 DataSet 中的任何修改数据更新数据库。

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

您还可以检查添加到 GridWeb1_SaveCommand 事件处理程序的代码
**添加到 GridWeb1_SaveCommand 事件处理程序的代码** 

![待办事项：图片_替代_文本](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

使用将更改保存到数据库**救球**按钮现在肯定会保存它们。
## **结论**
{{% alert color="primary" %}} 

数据绑定是Aspose.Cells.GridWeb的一个重要特性。使用 Aspose.Cells.GridWeb 提供的工作表设计器实用程序可以轻松地将工作表绑定到数据库。 Aspose.Cells.GridWeb 在创建强大的网格解决方案时节省了时间和精力。

{{% /alert %}}
