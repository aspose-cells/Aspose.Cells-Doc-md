---
title: 设置范围边框
type: docs
weight: 600
url: /zh/java/set-range-border/
---

## **可能的使用场景**
当您要为范围设置边框时，不需要逐个设置每个单元格。您可以在范围上设置边框。Aspose.Cells提供了这个功能。
本文提供了一个使用Aspose.Cells设置范围边框的示例代码。

## **在Excel中设置范围边框**
要在Excel中设置范围边框，可以按照以下步骤进行：
1. 选择要应用边框的单元格范围。
2. 在功能区的“主页”选项卡中，找到“字体”组。
3. 在“字体”组内，单击“边框”下拉按钮。
<br>
<img src="border.png" />
4. 从下拉菜单中选择要应用的边框类型。您可以从预设边框样式中进行选择，也可以自定义自己的边框。
5. 选择所需的边框样式后，边框将应用于所选单元格范围。

## **使用Aspose.Cells设置范围边框**
此示例显示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格添加数据。
1. 创建一个[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/range/)。
1. 设置范围的内边框。
1.设置区域的外边框。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Range-set-border.java" >}}
