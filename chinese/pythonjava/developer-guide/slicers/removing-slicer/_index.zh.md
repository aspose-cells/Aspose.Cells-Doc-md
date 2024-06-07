---
title: 移除缩略图
type: docs
weight: 40
url: /zh/python-java/removing-slicer/
---

## **移除分割器**
要在Microsoft Excel中移除切片器，您只需选择切片器，然后按*删除*按钮。要使用Aspose.Cells for Python via Java来实现此操作，使用Worksheet.getSlicers().remove()方法。它将从工作表中移除切片器。 

以下代码片段加载了包含现有切片器的[示例Excel文件](106364970.xlsx)。它访问了切片器，删除了它，并将[输出Excel文件](106364971.xlsx)保存。以下屏幕截图显示了将要删除的切片器。

![todo:image_alt_text](Removing-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
