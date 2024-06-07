---
title: 在工作表中管理图片
type: docs
weight: 100
url: /zh/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop，picture，pictures
description: 本文介绍了如何在GridDesktop中的工作表中使用图片。
---

{{% alert color="primary" %}} 

大多数人相信图片比文字更能说明事情。这就是为什么Aspose.Cells.GridDesktop支持向工作表添加图片来执行人们的这一信仰。在本主题中，我们将讨论在工作表中添加和操作图片。

{{% /alert %}} 
## **添加图片**
要使用Aspose.Cells.GridDesktop向单元格添加超链接，请按照以下步骤进行：

- 将Aspose.Cells.GridDesktop控件添加到您的**表单**中
- 访问任何所需的**工作表**
- 通过指定图片的文件路径和要插入图片的单元格名称，将**图片**添加到工作表

**Worksheet**对象中的**Pictures**集合提供了一个方法重载的**Add**方法。开发人员可以根据自己的特定需求使用任何重载版本的**Add**方法。使用这些重载版本的**Add**方法，可以从文件、流或**Image**对象中添加图片。

以下是将图片添加到工作表的示例代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **访问图片**
要访问和修改工作表中的现有图片，开发人员可以从**Worksheet**的**Pictures**集合中访问图片，指定插入图片的单元格（使用单元格名称或以行和列号表示的位置）。一旦访问图片，开发人员可以在运行时修改其图像。

以下是访问和修改工作表中图片的示例代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **移除图片**
要移除现有图片，开发人员可以简单地访问所需工作表，然后从**Worksheet**的**Pictures**集合中**Remove**图片，通过指定包含图片的单元格（使用名称或行和列号）。

在下面的代码中展示了如何从工作表中移除图片。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
