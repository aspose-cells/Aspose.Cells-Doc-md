---
title: 删除切片器
type: docs
weight: 40
url: /zh/python-java/removing-slicer/
---
## **删除切片器**
要删除 Microsoft Excel 中的切片器，只需选择切片器并按*删除*按钮。要通过 Java 为 Python 实现使用 Aspose.Cells 的保存，请使用 Worksheet.getSlicers().remove() 方法。它将从工作表中删除切片器。

以下代码片段加载[示例 Excel 文件](106364970.xlsx)包含一个现有的切片器。它访问切片器，删除它，并保存[输出Excel文件](106364971.xlsx).以下屏幕截图显示了将被删除的切片器。

![待办事项：图片_替代_文本](Removing-Slicer-using-Aspose.Cells.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
