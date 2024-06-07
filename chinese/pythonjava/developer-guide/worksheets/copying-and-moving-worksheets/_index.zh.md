---
title: 复制和移动工作表
type: docs
weight: 20
url: /zh/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

有时，您需要一些具有共同格式和数据的工作表。例如，如果您处理季度预算，可能希望创建包含相同列标题、行标题和公式的工作簿。有一种方法可以做到这一点：创建一个工作表，然后复制它。

Aspose.Cells支持工作表在工作簿内或工作簿之间的复制和移动。工作表包含的数据、格式、表、矩阵、图表、图像和其他对象复制的精度最高。

{{% /alert %}} 
## **使用Microsoft Excel移动或复制工作表**
在工作簿内或工作簿之间复制和移动工作表涉及的步骤如下。

1. 打开将接收工作表的工作簿。
1. 切换到包含要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在**编辑**菜单上，单击**移动或复制工作表**。
1. 在目标工作簿框中，单击要接收工作表的工作簿
1. 要将所选工作表移动或复制到新工作簿，单击**新建工作簿**。
1. 在**在工作表之前**框中，单击要将移动或复制的工作表插入的工作表。
1. 要复制工作表而不是移动它们，请选择**创建副本**复选框。
### **在工作簿内复制工作表**
Aspose.Cells提供了重载的[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\))方法，用于复制现有工作表。该方法的一个版本以源工作表的索引作为参数。另一个版本以源工作表的名称作为参数。

以下示例显示如何在工作簿内复制现有工作表。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **在工作簿之间复制工作表**
Aspose.Cells提供了[Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\))方法，用于将工作表复制到其他工作簿。该方法以源工作表对象作为参数。

以下示例显示如何将一个工作表从一个工作簿复制到另一个工作簿。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **在工作簿内移动工作表**
Aspose.Cells提供了[Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\))方法，用于将工作表移动到同一电子表格中的另一个位置。

以下示例显示了如何将工作表移动到工作簿中的另一个位置。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
