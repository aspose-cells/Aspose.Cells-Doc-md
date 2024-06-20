---
title: 管理Microsoft Excel文件的工作表
linktitle: 工作表
type: docs
weight: 90
url: /zh/python-net/manage-worksheets/
description: 本文展示了如何使用Aspose.Cells for Python via .NET API管理Microsoft Excel文件的工作表。
keywords: Python Excel库，Python管理Microsoft Excel文件的工作表，Python在Python中添加工作表，Python删除工作表，Python如何在新的Excel文件中添加工作表，Python如何将工作表添加到设计师电子制表文档，Python如何使用工作表名访问工作表，Python如何使用工作表名删除工作表，Python如何使用工作表索引删除工作表，Python如何激活工作表并使单元格活动。
---


{{% alert color="primary" %}}

开发人员可以利用Aspose.Cells灵活的API以编程方式轻松创建和管理Microsoft Excel文件中的工作表。本主题描述了在Microsoft Excel文件中添加和移除工作表的方法。

{{% /alert %}}

Aspose.Cells提供了一个表示Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。

## **如何将工作表添加到新的Excel文件**

要通过程序创建新的Excel文件:

1. 创建[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的对象。
1. 调用 [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) 类的 [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) 方法。自动向 Excel 文件中添加一个空工作表。可以通过将新工作表的索引传递给 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) 集合来引用它。
1. 获取工作表引用。
1. 对工作表进行操作。
1. 调用 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类的 [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) 方法，保存带有新工作表的新 Excel 文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **如何将工作表添加到设计师中的电子制表文档**

向设计电子表格添加工作表的过程与添加新工作表的过程相同，只是 Excel 文件已经存在，所以在添加工作表之前应该打开它。可以通过 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类打开设计电子表格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **如何使用工作表名访问工作表**

通过指定名称或索引来访问任何工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **如何使用工作表名删除工作表**

要从文件中删除工作表，调用 [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) 类的 [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) 方法。将工作表的名称传递给 [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) 方法以删除特定工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **如何使用工作表索引删除工作表**

当知道工作表的名称时，通过名称删除工作表的方法效果很好。如果不知道工作表的名称，请使用[**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int)方法，该方法使用工作表的索引而不是工作表的名称。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **如何激活工作表并使工作表单元格活动**

有时，您需要让特定工作表在用户在 Excel 中打开 Microsoft Excel 文件时处于活动状态并显示。同样，您可能希望激活特定单元格并设置滚动条以显示活动单元格。
Aspose.Cells 能够执行所有这些任务。

**活动工作表** 是您正在处理的工作表：标签上的活动工作表名称默认为粗体。

**活动单元格** 是所选单元格，也就是在开始输入数据时输入数据的单元格。一次只有一个单元格处于活动状态。活动单元格由粗边框突出显示。

### **如何激活工作表并激活单元格**

Aspose.Cells 提供特定的 API 调用来激活工作表和单元格。例如，[**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) 属性可用于在工作簿中设置活动工作表。
类似地，[**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) 属性用于设置和获取工作表中的活动单元格。

要确保水平或垂直滚动条位于要显示特定数据的行和列索引位置，请使用 [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) 和 [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/) 属性。

以下示例显示了如何激活工作表并将其中一个单元格设为活动单元格。在生成的输出中，滚动条将滚动以使第二行和第二列成为它们的第一个可见行和列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

