---
title: 管理工作表中的超链接
type: docs
weight: 90
url: /zh/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop,超链接,链接,超级链接,超链接
description: 本文介绍了如何在GridDesktop中处理超链接。
---

{{% alert color="primary" %}} 

使用Aspose.Cells.GridDesktop，还可以向工作表的单元格中存储的简单值添加超链接。假设在某些单元格中，您可能有一些值，您希望将其与网页上的更详细信息进行链接。在这种情况下，将希望为该单元格添加一个超链接，以便如果用户点击该单元格，则会被引导到该网页。在本主题中，我们将解释开发人员如何向其工作表中添加和操纵超链接。

{{% /alert %}} 
## **添加超链接**
使用Aspose.Cells.GridDesktop向单元格添加超链接，请按以下步骤操作：

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 访问工作表中将要设置超链接的所需**单元格**
- 在要设置超链接的单元格中添加一些值
- 通过指定应用超链接的单元格名称向工作表添加**超链接**

**工作表**对象中的**超链接**集合提供了多载入的**添加**方法。开发人员可以根据特定需求使用任何多载入版本的**添加**方法。

下面的代码将在工作表的**B2**和**C3**单元格中添加超链接。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **访问超链接**
一旦向单元格添加了超链接，可能还需要在运行时访问和修改超链接。为此，开发人员可以通过指定已添加超链接的单元格（使用单元格名称或行和列号来表示位置）简单地访问**工作表**的**超链接**集合中的超链接。一旦访问超链接，开发人员可以在运行时修改其URL。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **删除超链接**
要删除现有的超链接，开发人员可以简单地访问所需的工作表，然后通过指定超链接单元格的名称或行列号，从**工作表**的**超链接**集合中**删除**超链接。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

如果要向单元格添加超链接并希望在单元格中显示超链接URL而不是某个值，则不向单元格添加任何值，只需向该单元格添加超链接即可。这样做，单元格将成为超链接，其超链接URL也将显示为其值。

{{% /alert %}}
