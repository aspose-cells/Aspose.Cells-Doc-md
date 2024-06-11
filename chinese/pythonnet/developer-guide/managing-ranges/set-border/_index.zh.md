---
title: 设置范围边框
type: docs
weight: 600
url: /zh/python-net/set-range-border/
description: 本文展示了如何使用Aspose.Cells for Python通过.NET API设置范围边框。
keywords: Python Excel库，Python设置范围边框，Python添加范围边框。
---

## **可能的使用场景**
当您想要为范围设置边框时，无需单独设置每个单元格。您可以在范围上设置边框。Aspose.Cells for Python通过.NET提供了这一功能。
本文提供了一个使用Aspose.Cells for Python通过.NET设置范围边框的示例代码。

## **如何在Excel中设置范围边框**
要在Excel中设置范围边框，可以按照以下步骤进行：
1. 选择要应用边框的单元格范围。
2. 在功能区的“主页”选项卡中，找到“字体”组。
3. 在“字体”组内，单击“边框”下拉按钮。
<br>
<img src="border.png" />
4. 从下拉菜单中选择要应用的边框类型。您可以从预设边框样式中进行选择，也可以自定义自己的边框。
5. 选择所需的边框样式后，边框将应用于所选单元格范围。

## **使用Aspose.Cells for Python Excel库设置范围边框的方法**
此示例显示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格添加数据。
1. 创建一个[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)。
1. 设置范围的内边框。
1.设置区域的外边框。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-set-border.py" >}}
