---
title: 更新切片器
type: docs
weight: 60
url: /zh/python-java/updating-slicer/
---
## **更新切片器**
Aspose.Cells for Python via Java 支持更新切片器。为此，API 提供了用于选择或取消选择切片器项目的 Slicer.SlicerCache.SlicerCacheItems 属性。以下代码片段加载[示例 Excel 文件](106365050.xlsx)包含一个切片器。它取消选择切片器的第 2 项和第 3 项，并使用 Slicer.refresh() 方法刷新切片器。然后将工作簿另存为[输出Excel文件](106365051.xlsx).以下屏幕截图显示了示例代码对示例 Excel 文件的影响。正如您在屏幕截图中所见，使用所选项目刷新切片器也相应地刷新了数据透视表。

![待办事项：图像_替代_文本](Updating-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
