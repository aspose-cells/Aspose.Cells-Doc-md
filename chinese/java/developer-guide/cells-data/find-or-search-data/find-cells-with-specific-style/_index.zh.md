---
title: 查找具有特定样式的单元格
type: docs
weight: 80
url: /zh/java/find-cells-with-specific-style/
description: 本文演示如何使用 MS Excel 和 Aspose.Cells for Java API 查找具有特定样式的单元格。
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

有时，您需要找到具有某种特定样式的单元格。本文演示了如何使用 Microsoft Excel 以及 Aspose.Cells for Java API 来实现这一点。

{{% /alert %}}

## 使用 Microsoft Excel

这些是在 MS Excel 中搜索具有特定样式的单元格所需的步骤。

1. 选择**查找并选择**在里面**主页选项卡**.
1. 选择**寻找**.
1. 点击**选项**如果高级选项不可见。
1. 选择**从 Cell 选择格式...**来自**格式**落下。
1. 选择具有要搜索的样式的单元格。
1. 点击**找到所有**查找所有样式与所选单元格相似的单元格。

## 使用 Aspose.Cells for Java

 Aspose.Cells for Java 提供在工作表中查找具有特定样式的单元格的功能。为此，API 提供[**FindOptions.setStyle() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style)财产。

### 示例代码

以下代码片段查找所有与 cell 具有相同样式的单元格**A1**并更改这些单元格内的文本。请查看源文件和输出文件的屏幕截图以分析示例代码的输出。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

执行代码后，所有与单元格 A1 具有相同样式的单元格都会显示文本“Found”。

### 截图

![待办事项：图片_替代_文本](find-cells-with-specific-style_1.png)

**数字：**包含具有样式的单元格的源文件

这是由以下代码生成的输出文件。可以看到所有和of cell样式相同的cell**A1**有一个文本“找到”

![待办事项：图片_替代_文本](find-cells-with-specific-style_2.png)

**数字：**搜索后包含找到的单元格的输出文件**A1**风格
