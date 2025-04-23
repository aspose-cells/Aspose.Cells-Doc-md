---
title: 如何在Excel中更改评论的背景
linktitle: 评论背景
type: docs
weight: 190
url: /zh/python-net/how-to-set-comment-background/
description: 如何在Excel中更改评论的颜色。如何在Excel中评论中插入图片或图像。
keywords: 在Excel中添加插入图片、颜色和评论背景
---

{{% alert color="primary" %}}

评论被添加到单元格中以记录评论，包括公式运行的详细信息、值的来源或审阅人员的问题。当多个人在不同时间讨论或审查同一份文件时，评论起着极其重要的作用。如何区分不同人的评论？是的，我们可以为每个评论设置不同的背景颜色。但是当我们需要处理大量文档和大量评论时，手动操作是一场灾难。幸运的是[**Aspose.Cells for Python via .NET**](https://products.aspose.com/cells/python-net/)提供了一个允许你在代码中完成这项工作的API。

{{% /alert %}}

## **如何在Excel中更改评论的颜色**

当你不需要默认的评论背景颜色时，你可能希望用你感兴趣的颜色来替换它。如何在Excel中更改评论框的背景颜色？

以下代码将指导你如何使用[**Aspose.Cells for Python via .NET**](https://products.aspose.com/cells/python-net/)为你自己选择的评论添加喜欢的背景颜色。

在这里，我们已为您准备了一个[样本文件](exmaple.xlsx)。这个文件用于在下面的代码中初始化Workbook对象。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-HowToSetCommentBackground.py" >}}

执行上述代码，你将得到一个[输出文件](result.xlsx)。

## **如何在Excel中评论中插入图片或图像**

微软Excel允许用户在很大程度上自定义电子表格的外观。甚至可以向评论中添加背景图片。添加背景图片可以是一种美学选择，也可以用于加强品牌形象。

下面的示例代码使用[**Aspose.Cells for Python via .NET**](https://products.aspose.com/cells/python-net/) API从头开始创建一个XLSX文件，并向单元A1添加具有图片背景的评论。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddPictureToExcelComment-1.py" >}}

