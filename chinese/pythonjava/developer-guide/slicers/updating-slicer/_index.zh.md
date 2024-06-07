---
title: 更新切片器
type: docs
weight: 60
url: /zh/python-java/updating-slicer/
---

## **更新分割器**
Aspose.Cells for Python通过Java支持更新切片器。API提供了Slicer.SlicerCache.SlicerCacheItems属性，用于选择或取消选择切片器元素。以下代码片段加载了包含切片器的[示例Excel文件](106365050.xlsx)。它取消选择切片器的第2和第3个元素，并使用Slicer.refresh()方法刷新切片器。然后将工作簿保存为[输出Excel文件](106365051.xlsx)。下面的屏幕截图展示了示例代码对示例Excel文件产生的效果。正如您在屏幕截图中看到的，刷新具有选定元素的切片器也相应地刷新了数据透视表中的内容。

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
