---
title: 复制和移动工作表
type: docs
weight: 10
url: /zh/net/copying-and-moving-worksheets/
description: 本文包括示例代码，并描述了如何使用C# API或.NET库在Excel工作簿内和跨Excel工作簿中以编程方式复制和移动工作表。
keywords: 复制工作表 c#，移动工作表 c#
---

{{% alert color="primary" %}}

有时，您需要一些具有共同格式和数据的工作表。例如，如果您处理季度预算，可能希望创建包含相同列标题、行标题和公式的工作簿。有一种方法可以做到这一点：创建一个工作表，然后复制它。

Aspose.Cells支持在工作簿内部或之间复制和移动工作表。工作表完整地复制了数据、格式、表、矩阵、图表、图像和其他对象，精度最高。

{{% /alert %}}

## **使用Microsoft Excel移动或复制工作表**

以下是在Microsoft Excel中在工作簿内或工作簿之间复制和移动工作表涉及的步骤。

1. 要将工作表移动或复制到另一个工作簿中，请打开将接收工作表的工作簿。
1. 切换到包含要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在**编辑**菜单上，单击**移动或复制工作表**。
1. 在**要移动到的工作簿**对话框中，单击接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿中，请单击**新建工作簿**。
1. 在**工作表之前**框中，单击要插入已移动或复制的工作表之前的工作表。
1. 要复制工作表而不是移动它们，请选中**创建副本**复选框。

### **在Aspose.Cells内在工作簿中复制工作表**

Aspose.Cells提供了一个重载的方法，[**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index)，用于将工作表添加到集合中，并从现有工作表复制数据。该方法的一个版本以源工作表的索引作为参数。另一个版本以源工作表的名称作为参数。

以下示例显示如何在工作簿内复制现有工作表。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **在工作簿之间复制工作表**

Aspose.Cells提供了一个方法，[**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) 用于在工作簿内部或之间将源工作表的数据和格式复制到另一个工作表。该方法以源工作表对象为参数。

以下示例显示如何将一个工作表从一个工作簿复制到另一个工作簿。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

以下示例显示如何将一个工作表从一个工作簿复制到另一个工作簿。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **在工作簿内移动工作表**

Aspose.Cells提供一个方法[**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto)，用于将工作表移动到同一电子表格中的另一个位置。该方法以目标工作表索引作为参数。

以下示例显示了如何将工作表移动到工作簿中的另一个位置。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
