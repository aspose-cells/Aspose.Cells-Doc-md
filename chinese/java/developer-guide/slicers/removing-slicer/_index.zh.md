---
title: 移除缩略图
type: docs
weight: 30
url: /zh/java/removing-slicer/
---

## **可能的使用场景**
如果您想要在Microsoft Excel中移除切片器，只需选择它，然后按"删除"按钮。同样，如果您想要使用Aspose.Cells API以编程方式移除它，请使用 [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)) 方法。它会从工作表中移除切片器。 
## **移除分割器**
以下示例代码会加载包含现有切片器的 [示例Excel文件](67338504.xlsx)。它访问切片器，然后将其移除。最后，它将工作簿另存为 [输出Excel文件](67338502.xlsx)。以下截屏显示将在执行示例代码后移除的切片器。

![todo:image_alt_text](removing-slicer_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
