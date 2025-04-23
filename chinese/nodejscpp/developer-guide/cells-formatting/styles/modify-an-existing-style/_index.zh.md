---
title: 修改现有风格
linktitle: 修改现有风格
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库，允许用户修改现有的单元格样式。本文将介绍如何使用 Aspose.Cells 库修改现有的单元格样式，以便用户根据需要更改单元格的外观。
keywords: 修改现有样式，自定义应用程序的外观，指南，教程，帮助文档，开发文档，API参考，示例代码，下载，支持。
type: docs
weight: 90
url: /zh/nodejs-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

要将相同的格式选项应用于单元格，请创建一个新的格式样式对象。格式样式对象是格式特性的组合，如字体、字体大小、缩进、数字、边框、模式等，命名并存储为一组。应用时，该样式中的所有格式都会被应用。

您也可以使用现有的样式，将其与工作簿一起保存，并使用其格式化具有相同属性的信息。

当单元格没有明确格式化时，将应用**普通**样式（工作簿的默认样式）。除了普通样式之外，Microsoft Excel还预定义了几种样式，包括逗号、货币和百分号。

Aspose.Cells允许修改任何这些样式或您使用所需属性定义的任何其他样式。

{{% /alert %}}

## **使用Microsoft Excel**

更新Microsoft Excel 97-2003中的样式：

1. 单击**格式**菜单上的**样式**。
1. 从**样式名称**列表中选择要修改的样式。
1. 单击**修改**。
1. 使用格式单元格对话框中的选项卡选择要使用的样式选项。
1. 点击**确定**。
1. 在**样式包括**下，指定您想要的样式特征。
1. 单击**确定**以保存样式并将其应用于所选范围。

## **使用 Aspose.Cells for Node.js via C++**

以下示例演示了如何使用[**Style.update()**](https://reference.aspose.com/cells/nodejs-cpp/style/#update--)方法。

### **创建和修改样式**

此示例创建一个 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象，将其应用于一块区域的单元格，并修改 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象。所做的更改会自动应用到单元格及其所应用的区域。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-CreateAndModifyStyle.js" >}}


### **修改现有样式**

此示例使用一个简单的模板Excel文件，其中已经应用了一个名为“Percent”的样式到一个范围中。该示例：

1. 获取样式，
1. 创建一个样式对象，并
1. 修改样式格式。

修改将自动应用于应用了样式的范围。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ModifyExistingStyle.js" >}}


