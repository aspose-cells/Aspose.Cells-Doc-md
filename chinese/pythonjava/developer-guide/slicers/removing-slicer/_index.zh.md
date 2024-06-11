---
title: 移除切片器
type: docs
weight: 40
url: /zh/python-java/removing-slicer/
---

## **移除切片器**
要在Microsoft Excel中删除分层切片器，只需选择分层切片器，然后按下*删除*按钮。要实现Aspose.Cells for Python via Java中的这一操作，请使用Worksheet.getSlicers().remove()方法。它将从工作表中删除分层切片器。 

以下代码段加载包含现有分层切片器的[样本Excel文件](106364970.xlsx)，然后访问分层切片器，删除它，并保存为[输出Excel文件](106364971.xlsx)。以下屏幕截图显示了将被删除的分层切片器。

![todo:image_alt_text](Removing-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
