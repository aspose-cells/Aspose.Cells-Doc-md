---
title: 修改现有风格
type: docs
weight: 50
url: /zh/java/modify-an-existing-style/
description: 了解如何使用 Microsoft Excel 和 Aspose.Cells for Java API 在 Excel 中更改样式。
keywords: 修改现有样式Excel，修改现有样式Excel（Java），修改现有样式Excel，修改现有样式Excel（Java），更改Excel中的现有样式，更改Excel中的现有样式（Java），如何在Excel中更改样式，如何在Excel中使用Java更改样式，如何在Excel中使用Java更改样式，如何在Excel中使用Java更改样式，更改Excel中的现有样式Java，更改Excel中的现有样式Excel
---

{{% alert color="primary" %}}

要应用相同的格式选项到单元格，需要创建一个新的格式化样式对象。格式化样式对象是格式特征的组合，例如字体、字体大小、缩进、数字、边框、模式等，以命名方式存储并作为一组存储。应用时，该样式中的所有格式将被应用。

你还可以使用现有样式，将其保存与工作簿一起，并用其格式化具有相同属性的信息。

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

## **使用Aspose.Cells**

Aspose.Cells 提供 [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) 方法用于更新现有的样式。

要更改已创建动态使用 Aspose.Cells 或预定义的命名样式，请调用 [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) 方法，以反映对应用于单元格或范围的样式的任何更改。

[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) 方法的行为类似于样式对话框中的 **确定** 按钮：在对现有样式进行更改后，请调用以实现更改。如果已经将样式应用于一系列单元格，请修改样式属性并调用该方法，那些单元格的格式将自动更新

### **创建和修改样式**

此示例创建一个样式对象，将其应用于一系列单元格并修改样式对象。修改将自动应用于应用样式的单元格和范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **修改现有样式**

此示例使用一个简单的模板Excel文件，其中已经应用了一个名为“Percent”的样式到一个范围中。该示例：

1. 获取样式，
1. 创建一个样式对象，并
1. 修改样式格式。

修改将自动应用于应用了样式的范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
