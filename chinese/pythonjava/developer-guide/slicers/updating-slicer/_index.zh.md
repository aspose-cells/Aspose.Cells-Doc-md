---
title: 更新切片器
type: docs
weight: 60
url: /zh/python-java/updating-slicer/
---

## **更新分割器**
Aspose.Cells for Python via Java支持更新切片器。为此，API提供了Slicer.SlicerCache.SlicerCacheItems属性，用于选择或取消选择切片器项。以下代码片段加载包含切片器的[示例Excel文件](106365050.xlsx)，取消选择切片器的第2和第3项，并使用Slicer.refresh()方法刷新切片器。然后将工作簿保存为[输出Excel文件](106365051.xlsx)。以下屏幕截图显示了示例代码对示例Excel文件的影响。正如您在屏幕截图中所看到的，刷新带有选定项目的切片器还会相应地刷新数据透视表。

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
