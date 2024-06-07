---
title: 查找具有特定样式的单元格
type: docs
weight: 80
url: /zh/java/find-cells-with-specific-style/
description: 本文演示了如何使用MS Excel和Aspose.Cells for Java API查找具有特定样式的单元格。
keywords: 查找具有特定样式的单元格，查找具有指定样式的单元格excel，查找具有指定样式的单元格excel java，搜索具有特定样式的单元格，搜索具有特定样式的单元格excel，搜索具有指定样式的单元格excel java，如何查找具有指定样式的单元格，如何查找具有指定样式的单元格excel，如何查找具有指定样式的单元格excel java
---

{{% alert color="primary" %}}

有时，您需要查找具有某些特定样式的单元格。本文演示了如何通过使用Microsoft Excel和Aspose.Cells for Java API来实现。

{{% /alert %}}

## 使用Microsoft Excel

以下是在MS Excel中搜索具有特定样式的单元格所需的步骤。

1. 在**主页**选项卡中选择**查找和选择**。
1. 选择**查找**。
1. 如果高级选项不可见，请单击**选项**。
1. 从**格式**下拉列表中选择**从单元格选择格式**。
1. 选择具有要搜索的样式的单元格。
1. 单击**查找所有**以查找所有具有与所选单元格类似的样式的单元格。

## 使用 Aspose.Cells for Java

Aspose.Cells for Java提供了查找工作表中具有特定样式的单元格的功能。 对此，API提供[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style)属性。

###示例代码

以下代码片段查找所有具有与单元格**A1**相同样式的单元格，并更改这些单元格内的文本。 请查看源文件和输出文件的屏幕截图以分析示例代码的输出。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

执行代码后，所有具有与单元格A1相同样式的单元格将具有文本"Found"。

### 屏幕截图

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**图：** 具有样式的单元格的源文件

以下代码生成的输出文件如下。 您可以看到所有具有与单元格**A1**相同样式的单元格都带有文本"Found"。

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**图：** **A1**样式搜索后找到的单元格的输出文件
