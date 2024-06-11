---
title: 在工作表中实现 GridDesktop 数据绑定功能
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop，数据绑定，数据，绑定
description: 该文章介绍了如何在GridDesktop中进行数据绑定。
---

{{% alert color="primary" %}} 

数据绑定是Microsoft .NET Framework提供的一个令人兴奋的功能。我们知道，Microsoft提供的DataGrid控件支持数据绑定，这意味着DataGrid可以绑定到任何数据源（使用DataSet、DataTable和DataView对象）。这一特性使开发人员的工作变得更容易。基于相同的概念，Aspose.Cells.GridDesktop也支持数据绑定，允许开发人员将工作表绑定到任何数据源。本文探讨了这一特性。

{{% /alert %}} 
## **创建样本数据库**
1. 创建一个用于示例的数据库。我们使用Microsoft Access创建了一个具有Products表（下面是模式）的示例数据库。 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. 在Products表中添加了三条虚拟记录。
   **Products表中的记录** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **创建一个示例应用程序**
现在在Visual Studio中创建一个简单的桌面应用程序，并执行以下操作。

1. 从工具箱中拖动"GridControl"控件并将其放在窗体上。
1. 从工具箱中拖动四个按钮到窗体底部，分别设置它们的文本属性为**绑定工作表**，**添加行**，**删除行**和**更新数据库**。
## **添加命名空间和声明全局变量**
因为这个示例使用的是Microsoft Access数据库，在代码顶部添加System.Data.OleDb命名空间。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


现在可以使用打包在此命名空间下的类。

1. 声明全局变量。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **用数据库中的数据填充DataSet**
现在连接到示例数据库，获取并填充数据到一个DataSet对象中。

1. 使用OleDbDataAdapter对象连接到我们的示例数据库，并将从数据库的Products表中获取的数据填充到一个DataSet中，如下所示的代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **将工作表与DataSet绑定**
将工作表与数据集的 Products 表绑定：

1. 访问所需的工作表。
1. 将工作表与 DataSet 的 Products 表绑定。

在 **绑定工作表** 按钮的单击事件中添加以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **设置工作表的列标题**
现在绑定的工作表成功加载数据，但默认标记为 A、 B 和 C 的列标题，最好将列标题设置为数据库表中的列名。

设置工作表的列标题:

1. 获取 DataSet 的 DataTable(Products) 中每个列的标题。
1. 将标题分配到工作表列的标题。

在 **绑定工作表** 按钮的单击事件中添加以下代码片段。通过这样做，旧的列标题(A、 B 和 C)将被替换为 ProductID、 ProductName 和 ProductPrice。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **自定义列的宽度和样式**
要进一步改善工作表的外观，可以设置列的宽度和样式。例如，有时，列标题或列内的值包含大量字符，无法适应单元格。为解决此类问题，Aspose.Cells.GridDesktop 支持更改列的宽度。

将以下代码追加到 **绑定工作表** 按钮。列宽将根据新设置进行自定义。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop 还支持对列应用自定义样式。追加到 **绑定工作表** 按钮的以下代码将自定义列样式，使它们更具有吸引力。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


现在运行应用程序并单击 **绑定工作表** 按钮。
## **添加行**
要向工作表添加新行，使用 Worksheet 类的 AddRow 方法。这会在底部追加一个空行，并向数据源（这里是向 DataSet 的 DataTable 中）添加新的 DataRow。开发人员可以通过多次调用 AddRow 方法添加任意数量的行。添加行后，用户可以输入值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **删除行**
Aspose.Cells.GridDesktop 还支持通过调用 Worksheet 类的 RemoveRow 方法删除行。使用 Aspose.Cells.GridDesktop 删除行需要提供要删除的行的索引。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


将上述代码添加到 **删除行** 按钮并运行应用程序。在删除行之前，会显示一些记录。选择一行并单击 **删除行** 按钮可删除所选行。
## **将更改保存到数据库**
最后，要将用户对工作表所做的任何更改保存到数据库中，请使用 OleDbDataAdapter 对象的 Update 方法。Update 方法接受用于更新数据库的工作表的数据源（DataSet、DataTable 等）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. 将上述代码添加到**更新到数据库**按钮。
1. 运行应用程序。
1. 对工作表数据执行一些操作，可能添加新行并编辑或删除现有数据。
1. 然后单击**更新到数据库**以保存对数据库的更改。
1. 检查数据库以查看表记录是否已相应更新。
