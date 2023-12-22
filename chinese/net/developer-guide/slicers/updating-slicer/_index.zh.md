---
title: 更新切片器
type: docs
weight: 50
url: /zh/net/updating-slicer/
description: 本文介绍如何通过 Aspose.Cells for .NET API 更新切片器来更新链接的数据透视表。
keywords: Aspose.Cells C# Update slicer, C# how to change the slicer, how to adjust the slicer in C#, how to select or unselect he slicer items.
---
##  **可能的使用场景**

如果要更新 Microsoft Excel 中的切片器，请选择或取消选择其项目，它将相应地更新切片器表或数据透视表。请用[**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems)使用 Aspose.Cells 选择或取消选择切片器项目，然后调用[**切片器.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh)更新切片器表或数据透视表的方法。

##  **如何更新切片器**

以下示例代码加载[Excel 文件示例](67338475.xlsx)包含现有切片器。它取消选择切片器的第二个和第三个项目并刷新切片器。然后将工作簿另存为[输出Excel文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。正如您在屏幕截图中看到的，使用所选项目刷新切片器也会相应地刷新数据透视表。

![待办事项：图像_替代_文本](updating-slicer_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
