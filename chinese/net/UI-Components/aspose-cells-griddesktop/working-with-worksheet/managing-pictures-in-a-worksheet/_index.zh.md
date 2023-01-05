---
title: 管理工作表中的图片
type: docs
weight: 100
url: /zh/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

大多数人认为图片比文字更能说明问题。这就是为什么Aspose.Cells.GridDesktop支持在工作表中添加图片来执行人们的这一信念。在本主题中，我们将讨论在工作表中添加和操作图片。

{{% /alert %}} 
## **添加图片**
要使用 Aspose.Cells.GridDesktop 添加到单元格的超链接，请按照以下步骤操作：

- 将 Aspose.Cells.GridDesktop 控件添加到您的**形式**
- 访问任何想要的**工作表**
- 添加**图片**通过指定图片的文件路径和将插入图片的单元格名称到工作表

**图片**收集在**工作表**对象提供重载**添加**方法。开发人员可以使用任何重载版本**添加**方法根据自己的具体需要。使用这些重载版本**添加**方法，可以从文件、流或**图片**目的。

下面是将图片添加到工作表中的示例代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **访问图片**
要访问和修改工作表中的现有图片，开发人员可以从**图片**的集合**工作表**通过指定插入图片的单元格（使用单元格名称或其在行号和列号方面的位置）。一旦图片被访问，开发者就可以在运行时修改它的Image。

下面是访问和修改工作表中图片的示例代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **删除图片**
要删除现有图片，开发人员可以简单地访问所需的工作表，然后**去掉**图片来自**图片**的集合**工作表**通过指定包含图片的单元格（使用其名称或行号和列号）。

在下面的代码中显示了如何从工作表中删除图片。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
