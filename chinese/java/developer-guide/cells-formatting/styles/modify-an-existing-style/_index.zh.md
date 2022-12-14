---
title: 修改现有样式
type: docs
weight: 50
url: /zh/java/modify-an-existing-style/
description: 通过 Microsoft Excel 和 Aspose.Cells for Java API 了解如何在 Excel 中更改样式。
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

要将相同的格式选项应用于单元格，请创建一个新的格式样式对象。格式样式对象是将字体、字号、缩进、数字、边框、样式等格式特征组合命名并存储为一个集合。应用时，将应用该样式中的所有格式。

您还可以使用现有样式，将其与工作簿一起保存，并使用它来格式化具有相同属性的信息。

当单元格未明确格式化时，**普通的**样式（工作簿的默认样式）被应用。 Microsoft 除了普通样式外，Excel 还预定义了几种样式，包括逗号、货币和百分比。

Aspose.Cells 允许修改任何这些样式或您使用所需属性定义的任何其他样式。

{{% /alert %}}

## **使用 Microsoft Excel**

要更新 Microsoft Excel 97-2003 中的样式：

1. 在**格式**菜单，点击**风格**.
1. 从中选择要修改的样式**款式名称**列表。
1. 点击**调整**.
1. 使用格式 Cells 对话框中的选项卡选择所需的样式选项。
1. 点击**好的**.
1. 在下面**样式包括**指定你想要的样式特征。
1. 点击**好的**保存样式并将其应用于所选范围。

## **使用 Aspose.Cells**

Aspose.Cells 提供了[**样式更新**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()更新现有样式的方法。

要更改命名样式，无论是使用 Aspose.Cells 动态创建的还是预定义的，请调用[**样式更新**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()方法来反映应用于单元格或范围的样式的任何更改。

这[**样式更新**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) 方法的行为类似于**好的**样式对话框中的按钮：对现有样式进行更改后，调用以实现更改。如果您已经将样式应用于一系列单元格，修改样式属性并调用该方法，这些单元格的格式将自动更新

### **创建和修改样式**

此示例创建一个样式对象，将其应用于一系列单元格并修改样式对象。修改会自动应用于单元格和应用样式的范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **修改现有样式**

此示例使用一个简单的模板 Excel 文件，其中已将名为百分比的样式应用于范围。这个例子：

1. 获得风格，
1. 创建一个样式对象和
1. 修改样式格式。

修改会自动应用于应用样式的范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
