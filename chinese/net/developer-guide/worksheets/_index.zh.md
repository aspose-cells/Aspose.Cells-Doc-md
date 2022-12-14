---
title: 管理 Microsoft Excel 文件的工作表。
linktitle: 工作表
type: docs
weight: 90
url: /zh/net/manage-worksheets/
description: 使用 Aspose.Cells 添加工作表、删除工作表和活动工作表。
---
{{% alert color="primary" %}}

开发人员可以使用 Aspose.Cells 灵活的 API 以编程方式轻松地在 Microsoft Excel 文件中创建和管理工作表。本主题介绍在 Microsoft Excel 文件中添加和删除工作表的方法。

{{% /alert %}}

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。

## **将工作表添加到新的 Excel 文件**

要以编程方式创建新的 Excel 文件：

1. 创建对象的[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级。
1. 打电话给[**添加**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add)的方法[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)班级。一个空工作表会自动添加到 Excel 文件中。可以通过将新工作表的工作表索引传递给[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)收藏。
1. 获取工作表参考。
1. 在工作表上执行工作。
1. 通过调用[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级'[**节省**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **将工作表添加到 Designer 电子表格**

将工作表添加到设计器电子表格的过程与添加新工作表的过程相同，只是 Excel 文件已经存在，因此应在添加工作表之前打开。可以通过以下方式打开设计器电子表格[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **使用工作表名称访问工作表**

通过指定其名称或索引访问任何工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **使用工作表名称删除工作表**

要从文件中删除工作表，请调用[**移除位置**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index)的方法[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)班级。将工作表名称传递给[**移除位置**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)删除特定工作表的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **使用工作表索引删除工作表**

当工作表的名称已知时，按名称删除工作表效果很好。如果您不知道工作表的名称，请使用[**移除位置**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)采用工作表的工作表索引而不是其工作表名称的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **激活工作表并在工作表中激活 Cell**

有时，当用户在 Excel 中打开 Microsoft Excel 文件时，您需要激活并显示特定的工作表。同样，您可能想要激活特定单元格并设置滚动条以显示活动单元格。
Aspose.Cells 能够完成所有这些任务。

一个**活动表**是您正在处理的工作表：选项卡上的活动工作表名称默认为粗体。

一个**活性细胞**是一个选定的单元格，当您开始键入时，数据将被输入到该单元格中。一次只有一个细胞处于活动状态。活动单元格以粗边框突出显示。

### **激活工作表并激活 Cell**

Aspose.Cells 提供用于激活工作表和单元格的特定 API 调用。例如，[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)属性对于在工作簿中设置活动工作表很有用。
相似地，[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)属性用于设置和获取工作表中的活动单元格。

要确保水平或垂直滚动条位于要显示特定数据的行和列索引位置，请使用[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow)和[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)特性。

以下示例显示如何激活工作表并在其中创建活动单元格。在生成的输出中，滚动条将滚动以使第 2 行和第 2 列成为它们的第一个可见行和列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **推进主题**
- [复制和移动工作表](/cells/zh/net/copying-and-moving-worksheets/)
- [计算工作表中的单元格数](/cells/zh/net/count-number-of-cells-in-the-worksheet/)
- [检测空工作表](/cells/zh/net/detecting-empty-worksheets/)
- [查找工作表是否为对话框表](/cells/zh/net/find-if-the-worksheet-is-dialog-sheet/)
- [获取工作表唯一ID](/cells/zh/net/get-worksheet-unique-id/)
- [从工作表中创建、操作或删除场景](/cells/zh/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [管理分页符](/cells/zh/net/managing-page-breaks/)
- [页面设置功能](/cells/zh/net/page-setup-features/)
- [打印工作表的多份副本](/cells/zh/net/print-multiple-copies-of-a-worksheet/)
- [使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性](/cells/zh/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [工作表视图](/cells/zh/net/worksheet-views/)

