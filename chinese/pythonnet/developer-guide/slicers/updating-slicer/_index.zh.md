---
title: 更新切片器
type: docs
weight: 50
url: /zh/python-net/updating-slicer/
---
##  **可能的使用场景**

如果要更新 Microsoft Excel 中的切片器，请选择或取消选择其项目，它将相应地更新切片器表或数据透视表。请用[**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/)使用 Aspose.Cells for Python via .NET 选择或取消选择切片器项目，然后调用[**切片器.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)更新切片器表或数据透视表的方法。

##  **更新切片器**

以下示例代码加载[Excel 文件示例](67338475.xlsx)包含现有切片器。它取消选择切片器的第二个和第三个项目并刷新切片器。然后将工作簿另存为[输出Excel文件](67338476.xlsx)。以下屏幕截图显示了示例代码对示例 Excel 文件的效果。正如您在屏幕截图中看到的，使用所选项目刷新切片器也会相应地刷新数据透视表。

![待办事项：图像_替代_文本](updating-slicer_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
