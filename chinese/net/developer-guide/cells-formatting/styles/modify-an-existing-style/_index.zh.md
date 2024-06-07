---
title: 修改现有样式
description: Aspose.Cells是一个用于处理电子表格文件的.NET库，允许用户修改现有的单元格样式。本文将介绍如何使用Aspose.Cells库修改现有单元格样式，以便用户可以根据需要更改单元格的外观。
keywords: 修改现有样式，自定义应用程序的外观和感觉，指南，教程，帮助文档，开发文档，API参考，示例代码，下载，支持。
type: docs
weight: 90
url: /zh/net/modify-an-existing-style/
---

{{% alert color="primary" %}}

要将相同的格式选项应用于单元格，请创建一个新的格式样式对象。格式样式对象是格式特性的组合，例如字体、字体大小、缩进、数字、边框、图案等，以集合命名和存储。应用时，该样式中的所有格式都会被应用。

您也可以使用现有样式，将其保存在工作簿中，并使用相同属性格式化信息。

当单元格没有明确定义格式时，默认应用“Normal”样式（工作簿的默认样式）。Microsoft Excel除“Normal”样式外，还预定义了几种样式，包括逗号、货币和百分比。

Aspose.Cells允许修改这些样式中的任何一个或您定义的任何其他样式，并具有所需的属性。

{{% /alert %}}

## **使用Microsoft Excel**

要在Microsoft Excel 97-2003中更新样式:

1.在**格式**菜单上，单击**样式**。
1.从**样式名称**列表中选择要修改的样式。
1.单击**修改**。
1.使用“格式单元格”对话框中的选项卡选择要使用的样式选项。
1. 单击**确定**。
1.在**样式包括**下，指定要使用的样式特征。
1.单击**确定**以保存样式并将其应用于所选范围。

## **使用Aspose.Cells**

以下示例演示如何使用[**Style.Update**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)方法。

### **创建和修改样式**

该示例创建一个[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象，将其应用于一系列单元格，并修改[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象。修改将自动应用于应用样式的单元格和范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **修改现有样式**

此示例使用一个简单的模板Excel文件，其中已经应用了一个名为“百分比”的样式到一个范围。示例：

1.获取样式，
1.创建一个样式对象，
1.修改样式格式。

修改将自动应用于应用样式的范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
