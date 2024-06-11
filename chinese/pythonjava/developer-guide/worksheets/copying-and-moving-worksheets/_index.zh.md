---
title: 复制和移动工作表
type: docs
weight: 20
url: /zh/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

有时，您确实需要一些具有共同格式和数据的工作表。例如，如果您在季度预算上工作，您可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后进行复制。

Aspose.Cells支持在工作簿内或工作簿之间复制和移动工作表。工作表、数据、格式、表、矩阵、图表、图像和其他对象都会以最高精度复制。

{{% /alert %}} 
## **使用Microsoft Excel移动或复制工作表**
以下是在工作簿内或工作簿之间复制和移动工作表涉及的步骤。

1. 打开要接收工作表的工作簿。
1. 切换到包含您想要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在**编辑**菜单上，单击**移动或复制工作表**。
1. 在“接收工作簿”框中，单击要接收工作表的工作簿。
1. 若要将所选工作表移动或复制到新工作簿，请单击**新建**。
1. 在**之前工作表**框中，单击要将移动或复制的工作表插入到其前面的工作表。
1. 若要复制工作表而不是移动它们，请选中**创建副本**复选框。
### **在工作簿内复制工作表**
Aspose.Cells提供了一个重载的[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\))方法，用于复制现有工作表。该方法的一个版本以源工作表的索引作为参数。另一个版本以源工作表的名称作为参数。

以下示例显示了如何在工作簿内复制现有工作表。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **在工作簿之间复制工作表**
Aspose.Cells提供了[Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\))方法，用于将工作表复制到其他工作簿。该方法以源工作表对象作为参数。

以下示例显示了如何将一个工作表从一个工作簿复制到另一个工作簿。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **在工作簿内部移动工作表**
Aspose.Cells提供了[Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\))方法，用于将工作表移到同一电子表格中的另一个位置。

以下示例显示了如何将工作表移动到工作簿内的另一个位置。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
