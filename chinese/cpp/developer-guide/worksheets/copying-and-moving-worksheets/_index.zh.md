---
title: 复制和移动工作表
type: docs
weight: 10
url: /zh/cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

有时，您需要一些具有共同格式和数据的工作表。例如，如果您处理季度预算，可能希望创建包含相同列标题、行标题和公式的工作簿。有一种方法可以做到这一点：创建一个工作表，然后复制它。

Aspose.Cells支持在工作簿内或工作簿之间复制和移动工作表。工作表连同数据、格式、表、矩阵、图表、图像和其他对象完全精确地复制。

{{% /alert %}} 
## **使用Microsoft Excel移动或复制工作表**
在Microsoft Excel中复制和移动工作表内或工作表之间的步骤如下。

1. 要将工作表移动或复制到另一个工作簿中，请打开将接收工作表的工作簿。
1. 切换到包含要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在**编辑**菜单上，单击**移动或复制工作表**。
1. 在**要移动到的工作簿**对话框中，单击接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿中，请单击**新建工作簿**。
1. 在**工作表之前**框中，单击要插入已移动或复制的工作表之前的工作表。
1. 要复制工作表而不是移动它们，请选中**创建副本**复选框。
### **在Aspose.Cells内在工作簿中复制工作表**
Aspose.Cells提供了重载的方法[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)，用于向集合中添加工作表并从现有工作表复制数据。该方法的一个版本将源工作表的索引作为参数。另一个版本接受源工作表的名称。以下示例显示了如何复制工作簿中的现有工作表。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
### **在工作簿内移动工作表**
Aspose.Cells提供了一个方法[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)，用于将工作表移动到同一电子表格中的另一个位置。该方法接受目标工作表索引作为参数。以下示例显示了如何将工作表移动到工作簿内的另一个位置。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
