---
title: 在工作表中实现 GridDesktop 数据绑定功能
type: docs
weight: 10
url: /zh/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

数据绑定是 Microsoft .NET 框架提供的一项令人兴奋的功能。我们知道Microsoft提供的DataGrid控件支持数据绑定，也就是说一个DataGrid可以绑定到任何Data Source（使用DataSet、DataTable和DataView对象）。此功能使开发人员的生活变得更加轻松。基于相同的概念，Aspose.Cells.GridDesktop 也支持数据绑定，它允许开发人员将工作表绑定到任何数据源。本文探讨了该功能。

{{% /alert %}} 
## **创建示例数据库**
1. 创建一个示例数据库以用于示例。我们使用 Microsoft Access 创建了一个带有 Products 表（架构如下）的示例数据库。

![待办事项：图片_替代_文本](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Products 表中添加了三个虚拟记录。
   **产品表中的记录** 

![待办事项：图片_替代_文本](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **创建示例应用程序**
现在在 Visual Studio 中创建一个简单的桌面应用程序并执行以下操作。

1. 将“GridControl”控件从工具箱中拖放到窗体上。
1. 从窗体底部的工具箱中拖放四个按钮并将它们的文本属性设置为**绑定工作表**, **添加行**, **删除行**和**更新数据库**分别。
## **添加命名空间和声明全局变量**
因为此示例使用 Microsoft Access 数据库，所以在代码顶部添加 System.Data.OleDb 命名空间。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


您现在可以使用打包在此名称空间下的类。

1. 声明全局变量。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **用数据库中的数据填充数据集**
现在连接到示例数据库以获取数据并将其填充到 DataSet 对象中。

1. 使用 OleDbDataAdapter 对象连接我们的示例数据库，并使用从数据库中的 Products 表中获取的数据填充数据集，如下面的代码所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **将工作表与数据集绑定**
将工作表与 DataSet 的 Products 表绑定：

1. 访问所需的工作表。
1. 将工作表与 DataSet 的 Products 表绑定。

将以下代码添加到**绑定工作表**按钮的点击事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **设置工作表的列标题**
绑定的工作表现在可以成功加载数据，但列标题默认标记为 A、B 和 C。最好将列标题设置为数据库表中的列名。

设置工作表的列标题：

1. 获取 DataSet 中 DataTable (Products) 每一列的标题。
1. 将标题分配给工作表列的标题。

附上写在**绑定工作表**按钮的点击事件，代码如下。通过这样做，旧的列标题（A、B 和 C）将替换为 ProductID、ProductName 和 ProductPrice。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **自定义列的宽度和样式**
为了进一步改善工作表的外观，可以设置列的宽度和样式。例如，有时，列标题或列内的值包含单元格中放不下的大量字符。为了解决此类问题，Aspose.Cells.GridDesktop 支持更改列宽。

将以下代码附加到**绑定工作表**按钮。列宽将根据新设置进行自定义。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop 还支持对列应用自定义样式。下面的代码，附加到**绑定工作表**按钮，自定义列样式以使其更美观。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


现在运行应用程序并单击**绑定工作表**按钮。
## **添加行**
要向工作表添加新行，请使用 Worksheet 类的 AddRow 方法。这将在底部附加一个空行，并将一个新的 DataRow 添加到数据源（此处，将一个新的 DataRow 添加到 DataSet 的 DataTable）。开发人员可以通过一次又一次地调用 AddRow 方法来添加任意数量的行。添加一行后，用户可以在其中输入值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **删除行**
Aspose.Cells.GridDesktop也支持调用Worksheet类的RemoveRow方法删除行。使用 Aspose.Cells.GridDesktop 删除行需要删除行的索引。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


将上面的代码添加到**删除行**按钮并运行应用程序。在删除该行之前会显示几条记录。选择一行并单击**删除行**按钮删除选定的行。
## **保存对数据库的更改**
最后，要将用户对工作表所做的任何更改保存回数据库，请使用 OleDbDataAdapter 对象的 Update 方法。 Update 方法采用工作表的数据源（DataSet、DataTable 等）来更新数据库。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. 将上面的代码添加到**更新数据库**按钮。
1. 运行应用程序。
1. 对工作表数据执行一些操作，可能会添加新行以及编辑或删除现有数据。
1. 然后点击**更新数据库**将更改保存到数据库。
1. 检查数据库，查看表记录是否已相应更新。
