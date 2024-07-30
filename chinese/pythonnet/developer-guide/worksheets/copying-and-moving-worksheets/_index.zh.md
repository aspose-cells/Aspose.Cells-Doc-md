---
title: 复制和移动工作表
type: docs
weight: 10
url: /zh/python-net/copying-and-moving-worksheets/
description: 本文包括示例代码，描述了如何使用Aspose.Cells for Python via .NET API在Excel工作簿内和工作簿之间程序化地复制和移动工作表。
keywords: Python Excel库，Python复制工作表，Python移动工作表，Python在工作簿之间复制工作表，Python在工作簿内移动工作表，Python在工作簿之间复制工作表，Python在工作簿内复制工作表。
---

{{% alert color="primary" %}}

有时，您确实需要一些具有共同格式和数据的工作表。例如，如果您在季度预算上工作，您可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后进行复制。

Aspose.Cells for Python via .NET支持在工作簿内或工作簿之间复制和移动工作表。工作表以数据、格式、表格、矩阵、图表、图像和其他对象完整地精确复制。

{{% /alert %}}

## **如何使用Microsoft Excel移动或复制工作表**

以下是在Microsoft Excel中在工作簿内部或不同工作簿之间复制和移动工作表所涉及的步骤。

1. 要将工作表移动或复制到另一个工作簿中，请打开将要接收工作表的工作簿。
1. 切换到包含您想要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在“编辑”菜单上，单击“移动或复制工作表”
1. 在“选择工作簿”对话框中，单击要接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿中，请单击“新建工作簿”
1. 在“工作表之前”框中，单击要在其之前插入移动或复制的工作表。
1. 要复制工作表而不是移动它们，请选择“创建副本”复选框。

## **如何使用Aspose.Cells for Python Excel库在工作簿内复制工作表**

Aspose.Cells for Python via .NET提供了一个重载的方法，[**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str)，用于向集合中添加工作表并从现有工作表复制数据。该方法的一个版本以源工作表的索引作为参数。另一个版本以源工作表的名称作为参数。

以下示例显示了如何在工作簿内复制现有工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **如何在工作簿之间复制工作表**

Aspose.Cells for Python via .NET提供了一个方法，[**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet)，用于在工作簿内或工作簿之间从源工作表复制数据和格式到另一个工作表。该方法以源工作表对象作为参数。

以下示例显示了如何将一个工作表从一个工作簿复制到另一个工作簿。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

以下示例显示了如何将一个工作表从一个工作簿复制到另一个。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **如何在工作簿内移动工作表**

Aspose.Cells for Python via .NET提供了一个方法[**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int)，用于将工作表移动到同一电子表格中的另一个位置。该方法以目标工作表的索引作为参数。

以下示例显示了如何将工作表移动到工作簿内的另一个位置。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
