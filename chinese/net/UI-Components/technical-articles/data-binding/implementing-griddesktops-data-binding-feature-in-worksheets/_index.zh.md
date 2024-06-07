---
title: 实现GridDesktop工作表中的数据绑定特性
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop，数据绑定，数据，绑定
description: 本文介绍了如何在GridDesktop中进行数据绑定。
---

{{% alert color="primary" %}} 

数据绑定是由Microsoft .NET Framework提供的一项令人兴奋的特性。我们知道，Microsoft提供的DataGrid控件支持数据绑定，这意味着DataGrid可以绑定到任何数据源（使用DataSet、DataTable和DataView对象）。这个特性使开发人员的工作变得更轻松。基于相同的概念，Aspose.Cells.GridDesktop也支持数据绑定，允许开发人员将工作表绑定到任何数据源。本文探讨了这一特性。

{{% /alert %}} 
## **创建一个示例数据库**
1. 创建一个示例数据库以便用于示例。我们使用Microsoft Access创建了一个带有Products表（下面的模式）的示例数据库。 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. 向Products表中添加三条虚拟记录。
   产品表中的记录 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **创建一个示例应用程序**
现在在Visual Studio中创建一个简单的桌面应用程序，并执行以下操作。

1. 从工具箱中拖动"GridControl"控件并将其放置在表单上。
2. 从工具箱中拖动四个按钮放置在表单底部，并将它们的文本属性分别设置为**Bind Woksheet**，**Add Row**，**Delete Row**和**Update to Database**。
## **添加命名空间和声明全局变量**
因为这个示例使用了Microsoft Access数据库，在代码顶部添加System.Data.OleDb命名空间。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


现在您可以使用该命名空间下打包的类。

1. 声明全局变量。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **用数据库填充DataSet中的数据**
现在连接到示例数据库，获取并填充数据到一个 DataSet 对象。

1. 使用 OleDbDataAdapter 对象连接到我们的示例数据库，并使用从数据库中获取的数据填充一个 DataSet 中的 Products 表，如下面的代码所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **将工作表与 DataSet 绑定**
将工作表与 DataSet 的 Products 表绑定：

1. 访问所需的工作表。
1. 将工作表与 DataSet 的 Products 表绑定。

将以下代码添加到**绑定工作表**按钮的单击事件。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **设置工作表的列标题**
绑定的工作表现在成功加载数据，但默认情况下列标题标记为 A、B 和 C。最好将列标题设置为数据库表中的列名。

设置工作表的列标题：

1. 获取 DataSet（Products）中每列的标题。
1. 将标题分配给工作表列的标题。

将在**绑定工作表**按钮的单击事件中编写的代码附加以下代码片段。通过这样做，旧的列标题（A、B 和 C）将被替换为 ProductID、ProductName 和 ProductPrice。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **自定义列的宽度和样式**
为了进一步改善工作表的外观，可以设置列的宽度和样式。例如，有时列标题或列内的值包括大量字符，无法适应单元格。为了解决此类问题，Aspose.Cells.GridDesktop 支持更改列的宽度。

将以下代码附加到**绑定工作表**按钮。根据新设置，列宽度将被自定义。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop 还支持将自定义样式应用到列。附加到**绑定工作表**按钮的以下代码将自定义列样式，使其更具表现力。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


现在运行应用程序并单击**绑定工作表**按钮。
## **添加行**
要将新行添加到工作表，使用 Worksheet 类的 AddRow 方法。这会在底部追加一个空行，并向数据源（这里是向 DataSet 的 DataTable 添加新的 DataRow）添加新的 DataRow。开发人员可以通过反复调用 AddRow 方法添加任意多行。添加行后，用户可以输入值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **删除行**
Aspose.Cells.GridDesktop 还支持通过调用 Worksheet 类的 RemoveRow 方法删除行。使用 Aspose.Cells.GridDesktop 删除行需要提供要删除行的索引。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


将上述代码添加到**删除行**按钮，然后运行应用程序。删除选定行前，会显示几条记录。选择行并单击**删除行**按钮将删除所选行。
## **保存更改到数据库**
最后，要将用户对工作表所做的任何更改保存到数据库，使用 OleDbDataAdapter 对象的 Update 方法。Update 方法接受用于更新数据库的工作表的数据源（DataSet、DataTable 等）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. 将上述代码添加到**更新到数据库**按钮。
1.运行应用程序
1. 对工作表数据执行一些操作，例如添加新行以及编辑或删除现有数据。
1. 然后单击**更新到数据库**，将更改保存到数据库。
1. 检查数据库，以查看表记录是否已相应更新。
