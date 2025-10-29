---
title: 用Golang通过C++设置范围边框
type: docs
weight: 600
url: /zh/go-cpp/set-range-border/
description: 学习如何使用Golang通过C++中的Aspose.Cells设置范围边框。
---

## **可能的使用场景**
当你想为范围设置边框时，不需要逐个设置每个单元格。你可以直接在范围上设置边框。Aspose.Cells提供了此功能。本文提供了使用Aspose.Cells设置范围边框的示例代码。

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
2. 在第一个工作表的单元格中添加数据。
3. 创建一个[**Range**](https://reference.aspose.com/cells/go-cpp/range)。
4. 设置范围的内部边框。
5. 设置范围的外部边框。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetBorder.go" >}}
