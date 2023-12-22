---
title: 修改现有样式
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，允许用户修改现有的单元格样式。本文将介绍如何使用Aspose.Cells库修改现有的单元格样式，以便用户可以根据需要更改单元格的外观。
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /zh/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

要将相同的格式设置选项应用于单元格，请创建一个新的格式设置样式对象。格式化样式对象是格式化特征的组合，例如字体、字体大小、缩进、数字、边框、图案等，作为集合命名和存储。应用后，将应用该样式中的所有格式。

您还可以使用现有样式，将其与工作簿一起保存，并用于设置具有相同属性的信息格式。

当单元格没有显式格式化时，**普通的**应用样式（工作簿的默认样式）。 Microsoft 除普通样式外，Excel 还预定义了多种样式，包括逗号、货币和百分比。

Aspose.Cells 允许修改任何这些样式或您使用所需属性定义的任何其他样式。

{{% /alert %}}

##  **使用 Microsoft Excel**

要更新 Microsoft Excel 97-2003 中的样式：

1. 上**格式**菜单，单击*样式**。
1. 从中选择您要修改的样式**款式名称**列表。
1. 单击*修改**。
1. 使用“格式 Cells”对话框中的选项卡选择所需的样式选项。
1. 单击*确定**。
1. 在*样式包括**下，指定所需的样式功能。
1. 点击**OK**保存样式并将其应用到所选范围。

##  **使用Aspose.Cells**

以下示例演示了如何使用[**风格更新**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)方法。

###  **创建和修改样式**

这个例子创建了一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象，将其应用于一系列单元格并修改[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。修改会自动应用于单元格以及样式所应用的范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

###  **修改现有样式**

此示例使用一个简单的 Excel 模板文件，其中已将名为“百分比”的样式应用于某个范围。这个例子：

1. 得到风格，
1. 创建一个样式对象并
1. 修改样式格式。

修改会自动应用到样式所应用的范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
