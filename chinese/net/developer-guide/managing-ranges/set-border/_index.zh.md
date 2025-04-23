---
title: 设置范围边框
type: docs
weight: 600
url: /zh/net/set-range-border/
---

## **可能的使用场景**
当您想要为范围设置边框时，不需要逐个设置每个单元格。您可以为范围设置边框。Aspose.Cells提供了此功能。
本文提供了一个使用Aspose.Cells设置范围边框的示例代码。

## **在Excel中设置范围边框**
要在Excel中设置范围的边框，可以按照以下步骤进行：
1. 选择要应用边框的单元格范围。
2. 在功能区“主页”选项卡中，找到“字体”组。
3. 在“字体”组内，单击“边框”下拉按钮。
<br>
<img src="border.png" />
4. 从下拉菜单中选择要应用的边框类型。您可以选择预设的边框样式或自定义您自己的边框。
5. 选择所需的边框样式后，边框将应用于所选的单元格范围。

## **使用Aspose.Cells设置范围边框**
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 创建[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)。
1. 设置范围内的边框。
1. 设置范围外的边框。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}
{{< app/cells/assistant language="csharp" >}}
