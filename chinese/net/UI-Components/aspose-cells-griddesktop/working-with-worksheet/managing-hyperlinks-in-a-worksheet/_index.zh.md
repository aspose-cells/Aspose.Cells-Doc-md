---
title: 在工作表中管理超链接
type: docs
weight: 90
url: /zh/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop，hyper，link，hyperlink，hyperlinks
description: 本文介绍了如何在GridDesktop中使用超链接。
---

{{% alert color="primary" %}} 

使用Aspose.Cells.GridDesktop，还可以将超链接添加到工作表单元格中存储的简单值。假设在某些单元格中，您可能有一些值，希望将其与网页上的更详细信息链接起来。在这种情况下，希望向该单元格添加超链接，以便用户单击该单元格后，将被定位到该网页。在本主题中，我们将解释开发人员如何在其工作表中添加和操作超链接。

{{% /alert %}} 
## **添加超链接**
要使用Aspose.Cells.GridDesktop向单元格添加超链接，请按照以下步骤进行：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 访问工作表中将添加超链接的所需**单元格**
- 向待添加超链接的单元格添加一些值
- 通过指定要应用超链接的单元格名称来向工作表添加**超链接**

**Hyperlinks**集合中的**Worksheet**对象提供了一个重载的**Add**方法。开发人员可以根据其特定需求使用任何重载版本的**Add**方法。

下面的代码将在工作表的**B2**和**C3**单元格中添加一个超链接。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **访问超链接**
一旦将超链接添加到单元格中，可能还需要在运行时访问和修改超链接。为此，开发人员可以简单地从**Worksheet**的**Hyperlinks**集合中访问超链接，指定超链接所添加的单元格（使用单元格名称或其行和列号的位置）。一旦访问超链接，开发人员可以在运行时修改其URL。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **删除超链接**
要删除现有超链接，开发人员可以简单地访问所需的工作表，然后从**Worksheet**的**Hyperlinks**集合中删除超链接，指定超链接的单元格（使用其名称或行和列号）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

如果您想要向单元格添加超链接，并希望在单元格中显示超链接URL而不是某些值，则不要向单元格添加任何值，只需将超链接添加到该单元格。这样做，该单元格将成为超链接，并且超链接URL也将显示为其值。

{{% /alert %}}
