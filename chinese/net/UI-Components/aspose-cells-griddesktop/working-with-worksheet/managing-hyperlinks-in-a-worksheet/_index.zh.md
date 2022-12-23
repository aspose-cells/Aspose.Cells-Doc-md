---
title: 管理工作表中的超链接
type: docs
weight: 90
url: /zh/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

使用 Aspose.Cells.GridDesktop，还可以将超链接添加到存储在工作表单元格中的简单值。假设在某些单元格中，您可能希望将某些值链接到网页上的更详细信息。在这种情况下，最好向该单元格添加一个超链接，这样如果用户单击该单元格，他就会被定向到该网页。在本主题中，我们将解释开发人员如何在工作表中添加和操作超链接。

{{% /alert %}} 
## **添加超链接**
要使用 Aspose.Cells.GridDesktop 添加到单元格的超链接，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 访问一个想要的**Cell**在将被超链接的工作表中
- 向要超链接的单元格添加一些值
- 添加**超级链接**通过指定要应用超链接的单元格名称到工作表

**超级链接**收集在**工作表**对象提供重载**添加**方法。开发人员可以使用任何重载版本**添加**方法根据自己的具体需要。

下面的代码将添加一个超链接到**B2**和**C3**工作表的单元格。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **访问超链接**
将超链接添加到单元格后，可能还需要在运行时访问和修改超链接。为此，开发人员只需从**超级链接**的集合**工作表**通过指定要添加超链接的单元格（使用单元格名称或其在行号和列号方面的位置）。访问超链接后，开发人员可以在运行时修改其 URL。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **删除超链接**
要删除现有的超链接，开发人员只需访问所需的工作表，然后**去掉**超链接来自**超级链接**的集合**工作表**通过指定超链接单元格（使用其名称或行和列号）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

如果要向单元格添加超链接并希望在单元格中显示超链接 URL 而不是某个值，则不要向单元格添加任何值，只需将超链接添加到该单元格即可。这样做，单元格将被超链接，超链接 URL 也将作为其值显示在单元格中。

{{% /alert %}}
