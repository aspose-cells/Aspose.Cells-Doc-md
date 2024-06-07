---
title: 复制和移动工作表
type: docs
weight: 20
url: /zh/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

有时，您需要一些具有共同格式和数据的工作表。例如，如果您处理季度预算，可能希望创建包含相同列标题、行标题和公式的工作簿。有一种方法可以做到这一点：创建一个工作表，然后复制它。

Aspose.Cells支持在工作簿内部或之间复制和移动工作表。工作表完整地复制了数据、格式、表、矩阵、图表、图像和其他对象，精度最高。

{{% /alert %}}

## **使用Microsoft Excel移动或复制工作表**

以下是在工作簿内或在工作簿之间复制和移动工作表的步骤

1. 要将工作表移动或复制到另一个工作簿中，请打开将接收工作表的工作簿。
1. 切换到包含要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在**编辑**菜单上，单击**移动或复制工作表**。
1. 在目标工作簿框中，单击要接收工作表的工作簿
1. 要将选定的工作表移动或复制到新工作簿，请单击 **新建工作簿**
1. 在**工作表之前**框中，单击要插入已移动或复制的工作表之前的工作表。
1. 要复制工作表而不是移动它们，请选中**创建副本**复选框。

## **在工作簿内复制工作表**

Aspose.Cells提供了一个重载方法，[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)，用于向集合中添加工作表并从现有工作表复制数据。该方法的一个版本以源工作表的索引作为参数。另一个版本以源工作表的名称作为参数。

以下示例显示如何在工作簿内复制现有工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **在工作簿之间复制工作表**

Aspose.Cells提供了一个方法，[**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)，用于从源工作表复制数据和格式到工作簿内或工作簿之间的另一个工作表。该方法以源工作表对象作为参数。

以下示例显示如何将一个工作表从一个工作簿复制到另一个工作簿。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

以下示例显示如何将一个工作表从一个工作簿复制到另一个工作簿。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **在工作簿内移动工作表**

Aspose.Cells提供了一个方法，[**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)，用于将工作表移动到同一电子表格中的另一个位置。

以下示例显示了如何将工作表移动到工作簿中的另一个位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
