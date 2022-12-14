---
title: 删除切片器
type: docs
weight: 30
url: /zh/net/removing-slicer/
---
## **可能的使用场景**

如果要删除 Microsoft Excel 中的切片器，只需选择它并按*删除*按钮。同样，如果您想以编程方式使用 Aspose.Cells API 将其删除，请使用[**工作表.Slicers.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/remove)方法。它将从工作表中删除切片器。

## **删除切片器**

下面的示例代码加载[示例 Excel 文件](67338478.xlsx)包含一个现有的切片器。它访问切片器然后将其删除。最后，它将工作簿另存为[输出Excel文件](67338477.xlsx).以下屏幕截图显示了在执行示例代码后将被删除的切片器。

![待办事项：图片_替代_文本](removing-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-RemovingSlicer.cs" >}}
