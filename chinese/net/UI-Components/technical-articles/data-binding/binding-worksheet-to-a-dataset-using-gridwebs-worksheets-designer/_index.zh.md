---
title: 使用 GridWeb 工作表设计器将工作表绑定到 DataSet
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: 本文介绍了如何使用Worksheets Designer将工作表绑定到GridWeb中的DataSet。
---

{{% alert color="primary" %}} 

本文讨论了使用Aspose.Cells.GridWeb提供的特殊工具，在GUI模式下以一种简单的方法将工作表绑定到数据库表，即Worksheets Designer。 

{{% /alert %}} 
## **使用Worksheets Designer绑定工作表与数据库**
	**步骤1：创建示例数据库**
1. 首先，创建本文中将使用的示例数据库。我们使用Microsoft Access创建一个数据库，其中包含一个名为Products的表。其模式如下所示。
   **Products表的设计信息** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. 向Products表中添加了一些虚拟记录。
   **Products表中的记录** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **步骤2：设计示例应用程序**
使用Visual Studio.NET创建并设计了一个ASP.NET web应用程序，如下所示。 
**设计的示例应用程序** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **步骤3：使用服务器资源管理器连接数据库**
现在是连接到数据库的时候了。我们可以使用Visual Studio.NET中的服务器资源管理器轻松完成。 

1. 在服务器资源管理器中选择**数据连接**，然后右键单击。
1. 从菜单中选择**添加连接**。
   **选择添加连接选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



将显示数据链接属性对话框。 
**数据链接属性对话框** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



使用此对话框，您可以连接到任何数据库。默认情况下，它允许您连接到SQL Server数据库。在本示例中，我们需要连接到Microsoft Access数据库。 

1. 点击**提供程序**选项卡。
1. 从**OLE DB提供程序**列表中选择**Microsoft Jet 4.0 OLE DB提供程序**。
1. 点击**下一步**。
   **在选择OLE DB提供程序后点击下一步** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


打开**连接**选项卡页面。 

1. 选择Microsoft Access数据库文件（在我们的案例中是db.mdb）然后点击**确定**。
   **选择数据库文件后点击确定按钮** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

点击**确定**后，将在**服务器资源管理器**中创建到Microsoft Access数据库的数据库连接。双击连接以查看数据库中的所有表、视图和存储过程。

{{% /alert %}} 
### **步骤4：图形方式创建数据库连接对象**
1. 使用**服务器资源管理器**浏览数据库中的表。
   只有一个名为Products的表。 
1. 从**服务器资源管理器**将Products表拖放到**Web表单**。
   **从服务器资源管理器拖放Products表到Web表单** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



可能会弹出对话框。
**确认是否在连接字符串中包含数据库密码的对话框** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



决定是否在连接字符串中包含数据库密码。在本例中，我们选择**不包括密码**。 
创建并添加了两个数据库连接对象（oleDbConnection1和oleDbDataAdapter1）。
**创建和显示数据库连接对象（oleDbConnection1和oleDbDataAdapter1）** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **步骤5：生成数据集**
到目前为止，我们已经创建了数据库连接对象，但仍然需要一个地方来存储连接到数据库后的数据。DataSet对象可以精确地存储数据，我们还可以在VS.NET IDE中轻松地生成它。 

1. 选择**oleDbDataAdaper1**并右键单击。
1. 从菜单中选择**生成 DataSet** 选项。
   **选择生成 DataSet 选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



会显示生成 DataSet 对话框。 
在这里，可以选择要创建的新 DataSet 对象的名称，以及应将哪些表添加到其中。 

1. 选择**将此数据集添加到设计器** 选项。
1. 点击**确定**。
   **单击确定按钮生成 DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



向设计器中添加了一个 dataSet11 对象。
**生成 DataSet 并添加到设计器** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **步骤6：使用工作表设计器**
现在，是时候揭开秘密了。 

1. 选择 GridWeb 控件并右键单击。
1. 从菜单中选择**工作表设计器** 选项。 

   **选择工作表设计器选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



会显示工作表集合编辑器（也称为工作表设计器）。 
**工作表集合编辑器对话框** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



该对话框包含一些属性，可以配置这些属性将 Sheet1 绑定到数据库中的任何表。

1. 选择**DataSource** 属性。
   在上一步生成的 dataSet11 对象在菜单上列出。 
1. 选择 DataSet11。
1. 单击 **DataMember** 属性。
   Worksheets 设计器会自动显示 dataSet11 中表的列表。这里只有一个表，Products。
1. 选择 Products 表。
   **设置 DataSource 和 DataMember 属性** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. 检查 **BindColumns** 属性。
   **单击 BindColumns 属性** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



单击 **BindColumns** 属性会打开 BindColumn 集合编辑器。
**BindColumn 集合编辑器** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



在 BindColumn 集合编辑器中，Products 表的所有列都会被自动添加到 BindColumns 集合中。 

1. 选择任意列并自定义其属性。
   例如，您可以修改每个列的标题。
   **修改 ProductID 列的标题** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. 完成更改后，单击 **OK**。
1. 通过单击 **OK** 关闭所有对话框。
   最后，您将返回到 WebForm1.aspx 页面。 
   **在使用 Worksheets 设计器后返回到 WebForm1.aspx 页面** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


上面显示了 Products 表的列名。由于某些列的宽度很小，因此某些列的完整名称并不完全可见。 
### **步骤 7：向 Page_Load 事件处理程序添加代码**
我们已经使用了 Worksheets 设计器，现在只需要向 Page_Load 事件处理程序添加代码，以便使用 oleDbDataAdapter1 从数据库中填充 dataSet11 对象，并通过调用其 DataBind 方法将 GridWeb 控件绑定到 dataSet11。 

1. 添加代码： 

**C#**

{{< highlight csharp >}}

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

在工作表中实现 GridDesktop 数据绑定功能

{{< highlight csharp >}}

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

1. 检查代码添加到 Page_Load 事件处理程序。
   **添加到 Page_Load 事件处理程序的代码** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **第8步：运行应用程序**
编译并运行应用程序：按 **Ctrl+F5** 或单击 **开始**。 
**运行应用程序** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



编译后，WebForm1.aspx 页面将在浏览器窗口中打开，并从数据库加载所有数据。
**从数据库加载到 GridWeb 控件中的数据** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **使用 GridWeb 控件**
当数据加载到 GridWeb 控件中时，它为用户提供对数据的控制。GridWeb 提供了多种不同类型的数据操作功能。 
### **数据有效性**
Aspose.Cells.GridWeb 根据数据库中定义的数据类型自动为所有绑定列创建相应的验证规则。将光标悬停在单元格上可查看单元格的验证类型。
**检查单元格的验证类型** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **删除行**
要删除行，请选择一行（或行中的任何单元格），右键单击并选择 **删除行**。
**从菜单中选择删除行选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


该行将立即被删除。
**网格数据（删除一行后）** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **编辑行**
编辑单元格或行上的数据，然后单击**保存**或**提交**以保存更改。 
### **添加行**
1. 要添加一行，右键单击单元格，然后选择**添加行**。
   **从菜单中选择添加行选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



在其他行的末尾添加了一个新行到表格中。
**表格中添加了新行** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. 向新行添加值。
1. 单击**保存**或**提交**确认更改。
   **点击*保存*按钮保存数据更改** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **设置数值格式**
目前，**产品价格**列中的价格显示为数字值。可以将它们显示为货币。

1. 返回到 Visual Studio.NET。
1. 打开 BindColumn Collection Editor。
   **产品价格**列的**NumberType**属性设置为**常规**。
   **将 NumberType 属性设置为常规** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. 单击**DropDownList**，然后从列表中选择**Currency4**。
   **NumberType 属性更改为 Currency4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. 再次运行应用程序。
   **产品价格**列中的值现在为货币。
   **产品价格**以货币数值格式显示 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **编辑数据**
到目前为止，该应用程序仅允许用户查看表格数据。用户可以在GridWeb控件中编辑数据，但是在关闭浏览器并打开数据库后，没有任何更改。所做的更改并未保存到数据库。 

以下示例向应用程序添加代码，以便GridWeb可以将更改保存到数据库。 

1. 打开**属性**窗格，并从列表中选择GridWeb控件的SaveCommand事件。
   **选择GridWeb的SaveCommand事件** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. 双击**SaveCommand**事件，VS.NET将创建GridWeb1_SaveCommand事件处理程序。
1. 在此事件处理程序中添加代码，用于使用oleDbDataAdapter1将工作表中绑定的 DataSet 中的任何修改的数据更新到数据库。 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

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

在工作表中实现 GridDesktop 数据绑定功能

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

您还可以检查添加到GridWeb1_SaveCommand事件处理程序的代码
**添加到GridWeb1_SaveCommand事件处理程序的代码** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

现在使用**保存**按钮保存更改到数据库，这些更改一定会保存。
## **结论**
{{% alert color="primary" %}} 

数据绑定是Aspose.Cells.GridWeb的一个重要功能。通过Aspose.Cells.GridWeb提供的工作表设计器实用程序，很容易将工作表绑定到数据库。在创建强大的网格解决方案时，Aspose.Cells.GridWeb能节省时间和精力。 

{{% /alert %}}
