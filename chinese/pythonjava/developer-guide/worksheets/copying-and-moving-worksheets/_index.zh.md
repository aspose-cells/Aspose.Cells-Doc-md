---
title: 复制和移动工作表
type: docs
weight: 20
url: /zh/python-java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

有时，您确实需要许多具有通用格式和数据的工作表。例如，如果您处理季度预算，您可能希望创建一个工作簿，其中的工作表包含相同的列标题、行标题和公式。有一种方法可以做到这一点：创建一张纸然后复制它。

Aspose.Cells 支持在工作簿内或工作簿之间复制和移动工作表。包含数据、格式、表格、矩阵、图表、图像和其他对象的工作表以最高精度复制。

{{% /alert %}} 
## **使用 Microsoft Excel 移动或复制工作表**
以下是在工作簿内或工作簿之间复制和移动工作表所涉及的步骤。

1. 打开将接收工作表的工作簿。
1. 切换到包含要移动或复制的工作表的工作簿，然后选择工作表。
1. 在**编辑**菜单，点击**移动或复制工作表**.
1. 在“到书”框中，单击要接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿，请单击**新书**.
1. 在里面**片前**框，单击要在其前插入移动或复制的工作表的工作表。
1. 要复制工作表而不是移动它们，请选择**创建副本**复选框。
### **在工作簿中复制工作表**
Aspose.Cells 提供重载[工作表集合.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)用于复制现有工作表的方法。该方法的一个版本将源工作表的索引作为参数。另一个版本采用源工作表的名称。

以下示例显示如何复制工作簿中的现有工作表。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **在工作簿之间复制工作表**
Aspose.Cells 提供了[工作表.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) 方法用于将工作表复制到其他工作簿。该方法将源工作表对象作为参数。

下面的示例演示如何将工作表从一个工作簿复制到另一个工作簿。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **在工作簿中移动工作表**
Aspose.Cells 提供了[工作表.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) 方法用于将工作表移动到同一电子表格中的另一个位置。

下面的示例演示如何将工作表移动到工作簿中的另一个位置。



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
