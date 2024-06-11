---
title: 在工作表中管理图片
type: docs
weight: 100
url: /zh/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop，图片，图片
description: 本文介绍如何在GridDesktop工作表中处理图片。
---

{{% alert color="primary" %}} 

大多数人认为图片比言辞更能解释事物。这就是为什么Aspose.Cells.GridDesktop支持向工作表添加图片以实现人们的这一理念。在本主题中，我们将讨论如何向工作表添加和操作图片。

{{% /alert %}} 
## **添加图片**
使用Aspose.Cells.GridDesktop向单元格添加超链接，请按以下步骤操作：

- 向您的**表单**中添加Aspose.Cells.GridDesktop控件
- 访问任何所需的**工作表**
- 通过指定图片的文件路径和将插入图片的单元格名称向工作表添加**图片**

**工作表**对象中的**图片**集合提供了多载入的**添加**方法。开发人员可以根据特定需求使用任何多载入版本的**添加**方法。使用这些多载入版本的**添加**方法，可以从文件、流或**Image**对象添加图片。

以下是向工作表添加图片的示例代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **访问图片**
要访问和修改工作表中的现有图片，开发人员可以通过指定图片插入的单元格（使用单元格名称或行和列号来指定位置）简单地从**工作表**的**图片**集合中访问图片。一旦访问图片，开发人员可以在运行时修改其图像。

以下是访问和修改工作表中图片的示例代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **移除图片**
要删除现有图片，开发人员可以简单地访问所需的工作表，然后通过指定包含图片的单元格（使用其名称或行和列号）来从**工作表**的**图片**集合中**移除**图片。

下面的代码显示了如何从工作表中移除图片。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
