---
title: 移除切片器
type: docs
weight: 30
url: /zh/java/removing-slicer/
---

## **可能的使用场景**
如果想在 Microsoft Excel 中删除切片器，只需选择它并按[删除]键。同样，如果希望通过 Aspose.Cells API 编程删除，可以使用 [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove-com.aspose.cells.Slicer-) 方法。它会从工作表中移除切片器。 
## **移除切片器**
以下示例代码加载包含现有分析器的 [示例 Excel 文件](67338504.xlsx)。访问分析器，然后移除它​​。最后，将工作簿另存为 [输出 Excel 文件](67338502.xlsx)。截图显示示例代码执行后将要移除的分析器。

![todo:image_alt_text](removing-slicer_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
