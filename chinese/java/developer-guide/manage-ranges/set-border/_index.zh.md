---
title: 设置范围边框
type: docs
weight: 600
url: /zh/net/set-range-border/
---
##  **可能的使用场景**
当你想为 Range 设置边框时，你不需要单独设置每个单元格。您可以在范围上设置边框。 Aspose.Cells 提供此功能。
本文提供了使用Aspose.Cells设置范围边框的示例代码。

##  **在 Excel 中设置范围边框**
要在 Excel 中设置范围的边框，您可以按照以下步骤操作：
1. 选择要应用边框的单元格范围。
2. 在功能区的“主页”选项卡中，找到“字体”组。
3. 在“字体”组中，单击“边框”下拉按钮。
<br>
<img src="border.png" />
4. 从下拉菜单的选项中选择您要应用的边框类型。您可以从预设边框样式中进行选择或自定义您自己的边框。
5. 选择所需的边框样式后，边框将应用于选定的单元格范围。

##  **使用 Aspose.Cells 设置范围边界**
此示例显示如何：

1. 创建工作簿。
1. 将数据添加到第一个工作表中的单元格。
1. 创建一个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. 设置 Range 的内边框。
1. 设置范围的外边界。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}