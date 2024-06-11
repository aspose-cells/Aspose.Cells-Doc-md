---
title: 复制和移动工作表
type: docs
weight: 10
url: /zh/cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

有时，您确实需要一些具有共同格式和数据的工作表。例如，如果您在季度预算上工作，您可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后进行复制。

Aspose.Cells支持在工作簿内部或之间复制和移动工作表。工作表、数据、格式、表格、矩阵、图表、图像和其他对象都可以以最高程度的精度复制。

{{% /alert %}} 
## **使用Microsoft Excel移动或复制工作表**
以下是在Microsoft Excel中复制和移动工作表的步骤。

1. 要将工作表移动或复制到另一个工作簿中，请打开将要接收工作表的工作簿。
1. 切换到包含您想要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在“编辑”菜单上，单击“移动或复制工作表”
1. 在“选择工作簿”对话框中，单击要接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿中，请单击“新建工作簿”
1. 在“工作表之前”框中，单击要在其之前插入移动或复制的工作表。
1. 要复制工作表而不是移动它们，请选择“创建副本”复选框。
### **在Aspose.Cells中复制工作表**
Aspose.Cells提供了一个重载的方法[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)，用于将工作表添加到集合并从现有工作表中复制数据。该方法的一个版本将源工作表的索引作为参数。另一个版本将源工作表的名称作为参数。以下示例显示了如何在工作簿内部复制现有工作表。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
### **在工作簿内部移动工作表**
Aspose.Cells提供了一个[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)方法，用于将工作表移动到同一电子表格中的另一个位置。该方法将目标工作表的索引作为参数。以下示例显示了如何将工作表移动到工作簿内的另一个位置。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
