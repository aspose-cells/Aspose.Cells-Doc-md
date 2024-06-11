---
title: 更新切片器
type: docs
weight: 60
url: /zh/python-java/updating-slicer/
---

## **更新分析器**
Aspose.Cells for Python via Java支持更新分层切片器。为此，API提供了Slicer.SlicerCache.SlicerCacheItems属性，用于选择或取消选择分层切片器项目。以下代码段加载包含分层切片器的[样本Excel文件](106365050.xlsx)，取消选择分层切片器的第2和第3项，并使用Slicer.refresh()方法刷新分层切片器。然后将工作簿保存为 [输出Excel文件](106365051.xlsx)。以下屏幕截图显示了样本代码对样本Excel文件的影响。从屏幕截图中可以看到，刷新带有所选项的分层切片器还相应地刷新了数据透视表。

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
