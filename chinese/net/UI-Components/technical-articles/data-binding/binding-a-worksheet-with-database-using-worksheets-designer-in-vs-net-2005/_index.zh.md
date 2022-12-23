---
title: 在 VS.Net 2005 中使用工作表设计器将工作表与数据库绑定
type: docs
weight: 40
url: /zh/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

本文讨论将工作表与数据库表绑定的最简单方法**Visual Studio.Net 2005**使用 Aspose.Cells.GridWeb 提供的特殊工具命名为**工作表设计器**.这篇文章一定会让你感受到借助Aspose.Cells.GridWeb中的数据绑定功能是多么容易**工作表设计器** .

{{% /alert %}}

## **在 VS.Net 2005 中使用工作表设计器将工作表与数据库绑定**

本文的目的是让所有开发人员了解如何在中创建数据绑定应用程序**VS.Net 2005**并了解其用途和作用**工作表设计器**编辑。学习和理解任何事物的最佳方式是通过示例。因此，在本文中，我们最好创建一个示例应用程序来演示**工作表设计器**在将工作表与数据库绑定时。让我们一步步创建一个应用程序。

### **第 1 步：创建示例数据库**

首先，我们将创建一个将在本文中使用的示例数据库。我们使用 MS Access 创建了一个示例数据库，其中包含**产品**其架构如下所示的表：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**数字：**的设计资料**产品**桌子

很少有虚拟记录被添加到**产品**表格如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**数字：**记录在**产品**桌子

### **第 2 步：设计示例应用程序**

一个**ASP.NET 网络应用程序**在 Visual Studio.NET 2005 中创建和设计，如下图所示。这些屏幕截图对于不太熟悉在 Visual Studio.Net 2005 中使用 Aspose.Cells.GridWeb 的开发人员很有用。

首先启动 VS.Net 2005。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**数字：**启动 VS.Net 2005

从文件|新建|网站...菜单创建一个新网站。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**数字：**创建一个新网站

单击文件|新建|网站...菜单选项后，**新网站**显示对话框。点击**浏览**按钮在里面。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**数字：**新网站对话框

点击后**浏览**按钮，选择本地 IIS 中的位置文件夹。您可以创建一个新文件夹并将其设为虚拟文件夹，如图所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**数字：**创建新文件夹


点击后**打开**中的按钮**选择地点**对话，**新网站**对话框看起来像。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**数字：**设置项目位置

现在项目已创建

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**数字：**创建项目

### **XHTML 和 HTML 模式**

**Aspose.Cells.GridWeb**完全支持自 VS.Net 2005 以来默认实现的 XHTML 模式**Xhtml模式**的财产**网格网**控制设置为**真的**默认情况下，当您将控件放置在网页上时。但是如果你想在 VS.Net 2005 中为控件实现 HTML 模式，你可能会很容易做到。你必须修改**<!文档类型>**在网页的源代码中标记一点并设置**Xhtml模式**的财产**网格网**控制到**错误的** .

#### **在本主题中，我们将使用 HTML 模式进行控制。所以按照下面的步骤**

##### **1、切换到网页的Source视图，在源代码中找到如下<!DOCTYPE>标签。**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

找到该标签后，请在源代码中选择该完整标签，如下所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**数字：**选择**<!DOCTYPE> 标签**

更换**<!文档类型>**使用以下标记从源代码中标记。

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**数字：**修改**<!DOCTYPE> 标签**

##### **2. 将 GridWeb 控件添加到 Web 窗体之后。您应该选择该控件并从“属性”窗口中选择 XhtmlMode 属性以将其设置为 False。**

**将 GridWeb 添加到 WebForm** 

右击**工具箱**并选择**选择项目...**从菜单中。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**数字：**选择项目

现在选择**网格网**组件并单击**好的**

{{% alert color="primary" %}}

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**数字：**选择**网格网**组件对话框中的组件

现在**网格网**添加如下图所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**数字：** **网格网**添加到工具箱中

放置**网格网**在 Web 表单上，如下所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**数字：**配售**网格网**在网页上

{{% /alert %}} {{% alert color="primary" %}}

**程序**：选择控件，现在，选择**Xhtml模式**财产来自**特性**窗口并将其设置为**错误的**价值。

{{% /alert %}}

##### **第 3 步：使用服务器资源管理器连接数据库并设置连接对象**

首先我们将 MS Access 数据库添加到我们之前创建的项目中**步骤1** .你可能会看到**数据库文件**文件被添加到项目中。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**数字：**将数据库添加到项目文件夹

现在，我们去**组件设计器**使用网页的右键单击菜单选项打开 Web 表单的窗口。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**数字：**选择**查看组件设计器**选项

组件设计器窗口如下所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**数字：**组件设计器窗口

双击**OleDb连接**数据面板中的组件将 oleDbConnection1 对象放置到窗口中。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**数字：** oleDbConnection1 对象

现在，是时候连接数据库了。我们可以通过使用轻松地做到这一点**服务器资源管理器**在 Visual Studio.NET 2005 中。只需选择**数据连接**在**服务器资源管理器**并右键单击。您会看到一个上下文菜单出现在您的面前。选择**添加连接...**菜单中的选项如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**数字：**选择**添加连接...**菜单选项


选择后**添加连接...**菜单选项，**添加连接**对话框将打开并且**浏览**选择数据库文件，如下所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**数字：**选择数据库文件

您可以测试连接。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**数字：**测试连接

您可以浏览连接以检查表及其字段。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**数字：**检查连接的表及其字段

现在如果你选择**oleDbConnection1**中的对象**组件设计器**窗口，您可以选择与刚刚创建的现有连接相关的连接字符串，它位于**oleDbConnection1**属性窗口中的对象。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**数字：**选择对象的连接字符串

最后将对象的修饰符更改为**受保护**以获得更好的可访问性。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**数字：**设置对象的修饰符

##### **第 4 步：配置数据适配器对象**

现在，添加一个**OleDb数据适配器**从工具箱的数据面板中选择组件来配置它。双击**OleDb数据适配器**在工具箱的数据面板中，它将启动其配置向导并选择现有连接，如图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**数字：**数据适配器配置向导

点击后**下一个**按钮，单击**查询生成器**添加**产品**表，选择所有列并单击**好的**按钮。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**数字：**添加产品表

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**数字：**查询生成器

现在点击**结束**按钮完成向导。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**数字：**完成向导

配置向导后，oleDbDataAdapter1 会自动添加到窗口中，如下所示。此外，您可以将其修饰符设置为**受保护**.

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**数字：**在设计器窗口中检索 OleDbDataAdapter 对象

##### **第五步：生成数据集**

因为我们已经创建了数据库连接和数据适配器对象，但我们仍然需要一些东西，我们可以在连接数据库后存储数据。一种**数据集**对象可以精确存储数据，我们也可以使用 VS.NET 2005 IDE 轻松生成它。为此，请选择**oleDbDataAdaper1**并右键单击。将弹出一个上下文菜单，其中包含一些选项。选择**产生** **数据集...**菜单中的选项，如下图所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**数字：**选择**产生** **数据集...**菜单选项

选择后**产生** **数据集...**菜单中的选项，一个**生成数据集**对话框将打开。使用此对话框，我们可以选择新的名称**数据集**要创建的对象以及应添加到哪些表**数据集**.查看**将此数据集添加到设计器**选项并单击**好的**按钮如下图所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**数字：**点击**好的**生成按钮**数据集**

现在，你可以看到一个**数据集11**添加到设计器的对象如下图所示。将对象修改器设置为**受保护**.

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**数字：** **数据集**生成并添加到设计器窗口

在 .cs 文件中自动生成与连接、数据适配器、数据集对象相关的某些代码。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**数字：**生成代码

##### **第 6 步：使用工作表设计器**

现在，是时候揭开秘密了。选择控件并单击鼠标右键。将打开一个上下文菜单。从菜单中选择 Worksheets Designer... 选项，如下图所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**数字：**选择**工作表设计器...**菜单选项

在那之后**工作表集合编辑器**对话框（也称为**工作表设计器** 将被打开，你可以看到几个可以配置绑定的属性**工作表1**与数据库中的任何表。让我们选择**数据源**财产。写**数据集11**在其中（我们在上一步中生成并添加到设计器窗口）。然后点击**数据成员**财产。写**产品**这里作为表名如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**数字：**环境**数据源**和**数据成员**特性

现在，您可以配置**绑定列**财产。点击后，现在可以添加绑定列并设置**标题** , **数据字段**（它应该与**产品**表字段）和其他属性。您可以设置**自动创建**到**真的**并申请**验证**并设置**数字类型**不同的领域为您的要求。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**数字：**点击**绑定列**财产

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**数字：** **BindColumn 集合编辑器**对话

##### **第 7 步：为网页添加一些代码行**

我们用过**工作表设计器**很容易，现在我们只需要添加几行代码

首先我们将添加**启动时**要初始化的事件相关代码**初始化组件**初始化和创建连接、命令、数据适配器和数据集对象的方法。这几行代码不是自动生成的代码，所以我们必须手动添加它们。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**数字：**添加一些代码1

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**数字：**添加一些代码2

现在我们在**页面加载**填充事件处理程序**数据集11**对象与数据库中的数据（使用**oleDbDataAdapter1** ) 和绑定**网格网**控制与**数据集11**通过调用它的**数据绑定**方法。

{{% alert color="primary" %}}   {{% /alert %}}

##### **例子：**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

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

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

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

您还可以检查添加到的代码**页面加载**事件处理程序如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**数字：**代码添加到**页面加载**事件处理器

到目前为止，我们已经构建了一个非常有用的数据库应用程序。但是，此应用程序只能让您查看表的数据。尽管您可以在**网格网**控制但何时关闭浏览器窗口并打开数据库。你会发现什么都没有改变。这意味着，您所做的更改不会保存到数据库中。所以，有些事情你必须做。

现在我们将向我们的应用程序添加一些代码，以便**网格网**可以将其更改保存到实际数据库中。让我们打开**特性**窗格并选择**保存命令**事件的**网格网**从其事件列表中进行控制。如果你双击**保存命令**事件然后 VS.NET 2005 IDE 将创建**GridWeb1_SaveCommand**你的事件处理程序。向此事件处理程序添加一些代码，以使用包含在中的修改后的数据更新数据库**数据集**（与工作表绑定）使用**oleDbDataAdapter1**.

##### **例子：**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

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

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

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

您还可以检查添加到的代码**GridWeb1_SaveCommand**事件处理程序如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**数字：**代码添加到**GridWeb1_SaveCommand**事件处理器

现在，如果您要使用以下方法将更改保存到数据库**救球**的按钮**网格网**，他们一定会得救。

##### **第 8 步：运行您的应用程序**

最后，我们可以通过按**Ctrl+F5**或点击**开始**按钮。在调试对话框中，您可以指定适当的调试选项并单击**好的**按钮如下图所示。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**数字：**运行应用

编译后，**默认.aspx**我们的 Web 应用程序的页面将在一个新的浏览器窗口中打开，我们可以在其中看到从数据库加载的所有数据，如下所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**数字：**数据载入**网格网**从数据库控制

当数据加载到**网格网**control 那么你会觉得 Aspose.Cells.GridWeb 为其用户提供了数据的隐式控制。让我们检查一下提供了什么样的数据操作功能**网格网**给它的用户。

##### **数据验证**

Aspose.Cells.GridWeb 根据数据库中定义的数据类型自动为所有绑定列创建适当的验证规则。您可以通过将鼠标指针悬停在单元格上来查看单元格的验证类型，如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**数字：**检查单元格的验证类型

在上图中，我们可以看到选中的单元格包含**\<整数>**验证类型，这意味着用户只能向其输入整数值，否则会发生验证错误。而且，**\<必填>**表明的价值**产品编号**需要用户提交。

##### **删除行**

要删除一行，您应该首先选择一行（或该行的任何单元格）并选择**删除行**右键菜单中的选项如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**数字：**选择**删除行**菜单选项

选择后**删除行**从菜单中删除该行**网格网**.现在点击**救球**的按钮**网格网**删除原始数据库表中的该记录。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**数字：**网格数据（删除一行后）

##### **编辑行**

您还可以编辑单元格或行中的数据，然后单击**救球**按钮以保存您的更改。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**数字：**网格数据（编辑记录1）

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**数字：**网格数据（编辑记录2）

##### **添加行**

要添加一行，请选择**添加行**右键菜单中的选项如下图所示：

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**数字：**选择**添加行**菜单选项

选择后，新行将添加到行末尾的工作表中**添加行**菜单中的选项。在新添加的行的左侧，您会注意到一个**星号**标记，表示该行是新添加的。

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**数字：**新行添加到网格

在新行中输入值后，单击**救球**按钮确认原始数据库表的更改如下所示

![待办事项：图片_替代_文本](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**数字：**通过单击保存对数据库表的更改**救球**按钮

{{% alert color="primary" %}}   {{% /alert %}}

##### **结论**

{{% alert color="primary" %}}

**数据绑定**是 Aspose.Cells.GridWeb 的一个重要特征。开发人员使用以下方法将工作表与数据库绑定真的很容易**工作表设计器**Aspose.Cells.GridWeb 提供的实用程序。 Aspose.Cells.GridWeb 非常有助于开发人员在创建强大的网格解决方案时节省时间和精力。

{{% /alert %}}
