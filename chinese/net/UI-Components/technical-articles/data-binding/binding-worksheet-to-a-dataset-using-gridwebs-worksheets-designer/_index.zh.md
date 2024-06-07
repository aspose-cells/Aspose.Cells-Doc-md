---
title: 使用GridWeb工作表设计器将工作表与DataSet绑定
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb，bind，DataSet，Designer，designer
description: 本文介绍了如何使用工作表设计器在GridWeb中将工作表绑定到DataSet。
---

{{% alert color="primary" %}} 

本文讨论了使用Aspose.Cells.GridWeb提供的特殊工具，即工作表设计器，在GUI模式下将工作表绑定到数据库表的简单方法。 

{{% /alert %}} 
## **使用工作表设计器将工作表与数据库绑定**
	**步骤1：创建一个样本数据库**
1. 首先，我们创建本文中将使用的样本数据库。我们将使用Microsoft Access来创建一个包含名为Products的表的数据库。其模式如下所示。
   **Products表的设计信息** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Products 表中添加了一些虚拟记录。
   **Products 表中的记录** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **步骤 2：设计示例应用程序**
在 Visual Studio.NET 中创建并设计了一个 ASP.NET web 应用程序，如下所示。 
**设计的示例应用程序** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **步骤 3: 使用服务器资源管理器与数据库建立连接**
是时候连接到数据库了。我们可以通过 Visual Studio.NET 中的服务器资源管理器轻松完成这个任务。 

1. 在 **服务器资源管理器** 中选择 **数据连接**，然后右键单击。
1. 从菜单中选择 **添加连接**。
   **选择添加连接选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



将弹出“数据链接属性”对话框。 
**数据链接属性对话框** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



使用此对话框，您可以连接到任何数据库。默认情况下，它允许您连接到 SQL Server 数据库。在本例中，我们需要连接到 Microsoft Access 数据库。 

1. 点击 **提供程序** 选项卡。
从 **OLE 数据库提供程序** 列表中选择 **Microsoft Jet 4.0 OLE DB 提供程序**。
1. 单击 **下一步**。
   **选择 OLE DB 提供程序后单击“下一步”** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


打开 **连接** 选项卡页面。 

1. 选择 Microsoft Access 数据库文件（在我们的案例中是 db.mdb），然后单击 **确定**。
   **选择数据库文件后单击确定按钮** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

单击 **确定** 后，将在 **服务器资源管理器** 中创建到 Microsoft Access 数据库的数据库连接。双击连接以查看数据库中的所有表、视图和存储过程。

{{% /alert %}} 
### **步骤 4: 图形化创建数据库连接对象**
1. 使用 **服务器资源管理器** 浏览数据库中的表。
   数据库中只有一个表，即 Products。 
1. 将 **服务器资源管理器** 中的 Products 表拖放到 **Web 表单** 中。
   **从服务器资源管理器拖放 Products 表到 Web 表单** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



可能会出现对话框。
**确认在连接字符串中包含数据库密码的对话框** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



决定是否在连接字符串中包含数据库密码。在本例中，我们选择了**不包括密码**。 
已创建和添加了两个数据库连接对象（oleDbConnection1 和 oleDbDataAdapter1）。
**已创建并显示的数据库连接对象（oleDbConnection1 和 oleDbDataAdapter1）** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **第5步：生成数据集**
到目前为止，我们已经创建了数据库连接对象，但在连接到数据库后仍需要一个地方来存储数据。DataSet对象可以精确地存储数据，而且我们还可以在VS.NET IDE中轻松生成它。 

1. 选择**oleDbDataAdaper1**，然后右键单击。
1. 从菜单中选择**生成数据集**选项。
   **选择生成数据集选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



将显示生成数据集对话框。 
在这里，可以选择要创建的新DataSet对象的名称，以及应该向其中添加哪些表。 

1. 选择**将此数据集添加到设计器**选项。
1. 单击**确定**。
   **单击确定按钮生成 DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



会将一个dataSet11对象添加到设计器中。
**生成并添加到设计器中的DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **第6步：使用工作表设计器**
现在，是时候打开秘密了。 

1. 选择GridWeb控件，然后右键单击。
1. 从菜单中选择**工作表设计器**选项。 

   **选择工作表设计器选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



将显示工作表集合编辑器（也叫工作表设计器）。 
**工作表集合编辑器对话框** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



该对话框包含一些属性，可以配置将Sheet1绑定到数据库中的任何表。

1. 选择**DataSource**属性。
   上一步生成的dataSet11对象在菜单上列出。 
1. 选择dataSet11。
1. 单击**DataMember**属性。
   工作表设计器会自动显示dataSet11中表的列表。这里只有一个表，名为Products。
1. 选择Products表。
   **设置DataSource和DataMember属性** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. 选择**BindColumns**属性。
   **单击BindColumns属性** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



单击**BindColumns**属性会打开BindColumn集合编辑器。
**BindColumn集合编辑器** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



在 BindColumn 集合编辑器中，**Products** 表的所有列都会自动添加到 BindColumns 集合中。 

1. 选择任意列并自定义其属性。
   例如，您可以修改每个列的标题。
   **修改 ProductID 列的标题** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. 完成修改后，点击 **确定**。
1. 点击 **确定** 关闭所有对话框。
   最后，将返回到 WebForm1.aspx 页面。 
   **从 Worksheets Designer 返回到 WebForm1.aspx 页面** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


上述显示了 Products 表的列名。列的宽度较小，因此某些列的完整名称不完全可见。 
### **步骤 7：向 Page_Load 事件处理程序添加代码**
我们已使用 Worksheets Designer，现在只需向 Page_Load 事件处理程序添加代码，用于使用 oleDbDataAdapter1 从数据库中填充 dataSet11 对象，并通过调用其 DataBind 方法将 GridWeb 控件绑定到 dataSet11。 

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

**VB.NET**

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

1. 检查添加到 Page_Load 事件处理程序的代码。
   **添加到 Page_Load 事件处理程序的代码** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **步骤 8：运行应用程序**
编译并运行应用程序：要么按 **Ctrl+F5**，要么点击 **启动**。 
**运行应用程序** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



编译后，WebForm1.aspx 页面在浏览器窗口中打开，并加载了所有来自数据库的数据。
**从数据库加载到 GridWeb 控件的数据** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **使用 GridWeb 控件**
当数据加载到 GridWeb 控件中时，用户可以控制数据。 GridWeb 提供多种不同类型的数据操纵功能。 
### **数据验证**
Aspose.Cells.GridWeb 会根据数据库中定义的数据类型自动为所有绑定列创建适当的验证规则。将鼠标悬停在单元格上可查看单元格的验证类型。
**检查单元格的验证类型** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **删除行**
要删除行，请选择行（或行中的任意单元格），右键单击并选择 **删除行**。
**从菜单中选择删除行选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


该行将立即被删除。
**删除行后的网格数据** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **编辑行**
编辑单元格或行中的数据，然后点击 **保存** 或 **提交** 以保存更改。 
### **添加行**
1. 要添加一行，请右键单击单元格，然后选择**添加行**。
   **从菜单中选择添加行选项** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



在其他行的末尾，工作表上添加了一行新行。
**网格中添加了新行** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. 为新行添加值。
1. 单击**保存**或**提交**以确认更改。
   **点击*保存*按钮保存数据更改** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **设置数字格式**
目前，**产品价格**列中的价格显示为数字值。 可以使其看起来像货币。

1. 返回到Visual Studio.NET。
1. 打开BindColumn集合编辑器。
   **Product Price**列的**NumberType**属性设置为**常规**。
   **NumberType属性设置为常规** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. 单击**DropDownList**，然后从列表中选择**Currency4**。
   **NumberType属性更改为Currency4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. 再次运行应用程序。
   **Product Price**列中的值现在是货币。
   **产品价格采用货币数字格式** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **编辑数据**
到目前为止，应用程序仅允许用户查看表数据。 用户可以在GridWeb控件中编辑数据，但是在关闭浏览器并打开数据库时，没有任何更改。 所做的更改未保存到数据库。 

以下示例向应用程序添加了代码，以便GridWeb可以将更改保存到数据库。 

1. 打开**属性**面板，然后从列表中选择GridWeb控件的**SaveCommand**事件。
   **选择GridWeb的SaveCommand事件** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. 双击**SaveCommand**事件，VS.NET将创建GridWeb1_SaveCommand事件处理程序。
1. 向此事件处理程序添加代码，以更新与oleDbDataAdapter1绑定到工作表的DataSet中的任何修改数据的数据库。 

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

**VB.NET**

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

还可以检查添加到GridWeb1_SaveCommand事件处理程序的代码
**添加到GridWeb1_SaveCommand事件处理程序的代码** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

现在通过**保存**按钮保存更改到数据库。
## **结论**
{{% alert color="primary" %}} 

数据绑定是Aspose.Cells.GridWeb的一个重要功能。 使用Aspose.Cells.GridWeb提供的Worksheets Designer实用程序很容易将工作表绑定到数据库。 Aspose.Cells.GridWeb在创建强大的网格解决方案时节省时间和精力。 

{{% /alert %}}
