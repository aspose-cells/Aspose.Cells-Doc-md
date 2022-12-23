---
title: 更新切片器
type: docs
weight: 50
url: /zh/net/updating-slicer/
---
## **可能的使用场景**

如果要在 Microsoft Excel 中更新切片器，选择或取消选择其项目，它将相应地更新切片器表或数据透视表。请用[**切片器.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)使用 Aspose.Cells 选择或取消选择切片器项目，然后调用[**切片器.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)更新切片器表或数据透视表的方法。

## **更新切片器**

下面的示例代码加载[示例 Excel 文件](67338475.xlsx)包含一个现有的切片器。它取消选择切片器的第 2 项和第 3 项并刷新切片器。然后将工作簿另存为[输出Excel文件](67338476.xlsx).以下屏幕截图显示了示例代码对示例 Excel 文件的影响。正如您在屏幕截图中所见，使用所选项目刷新切片器也相应地刷新了数据透视表。

![待办事项：图片_替代_文本](updating-slicer_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
