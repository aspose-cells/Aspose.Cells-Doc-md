---
title: 移除切片器
type: docs
weight: 30
url: /zh/net/removing-slicer/
---

## **可能的使用场景**

如果要在Microsoft Excel中移除切片器，只需选择它并按下*Delete*按钮。同样，如果要使用Aspose.Cells API编程方式移除它，请使用[**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/remove)方法。这将从工作表中移除切片器。

## **移除切片器**

以下示例代码加载了包含现有切片器的[sample Excel file](67338478.xlsx)。它访问切片器，然后将其移除，最后将工作簿保存为[output Excel file](67338477.xlsx)。以下截图展示了在执行示例代码后将要移除的切片器。

![todo:image_alt_text](removing-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-RemovingSlicer.cs" >}}
