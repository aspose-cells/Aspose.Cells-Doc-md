---
title: 管理Microsoft Excel文件的工作表
linktitle: 工作表
type: docs
weight: 90
url: /zh/net/manage-worksheets/
description: 使用Aspose.Cells添加工作表、删除工作表和激活工作表。
---


{{% alert color="primary" %}}

开发人员可以利用Aspose.Cells灵活的API以编程方式轻松创建和管理Microsoft Excel文件中的工作表。本主题描述了在Microsoft Excel文件中添加和移除工作表的方法。

{{% /alert %}}

Aspose.Cells提供了一个表示Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。

## **向新的Excel文件添加工作表**

要通过程序创建新的Excel文件:

1. 创建[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的对象。
1. 调用 [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) 类的 [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) 方法。自动向 Excel 文件中添加一个空工作表。可以通过将新工作表的索引传递给 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合来引用它。
1. 获取工作表引用。
1. 对工作表进行操作。
1. 调用 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) 方法，保存带有新工作表的新 Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **向设计电子表格添加工作表**

向设计电子表格添加工作表的过程与添加新工作表的过程相同，只是 Excel 文件已经存在，所以在添加工作表之前应该打开它。可以通过 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类打开设计电子表格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **使用工作表名称访问工作表**

通过指定名称或索引来访问任何工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **使用工作表名称移除工作表**

要从文件中删除工作表，调用 [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) 类的 [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) 方法。将工作表的名称传递给 [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) 方法以删除特定工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **通过页索引删除工作表**

当知道工作表的名称时，通过名称删除工作表很方便。如果不知道工作表的名称，则可以使用重载版本的 [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) 方法，该方法接受工作表的索引而不是工作表名称。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **激活工作表并使工作表中的单元格处于活动状态**

有时，您需要让特定工作表在用户在 Excel 中打开 Microsoft Excel 文件时处于活动状态并显示。同样，您可能希望激活特定单元格并设置滚动条以显示活动单元格。
Aspose.Cells 能够执行所有这些任务。

**活动工作表** 是您正在处理的工作表：标签上的活动工作表名称默认为粗体。

**活动单元格** 是所选单元格，也就是在开始输入数据时输入数据的单元格。一次只有一个单元格处于活动状态。活动单元格由粗边框突出显示。

### **激活工作表并使单元格处于活动状态**

Aspose.Cells 提供特定的 API 调用来激活工作表和单元格。例如，[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) 属性可用于在工作簿中设置活动工作表。
类似地，[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) 属性用于设置和获取工作表中的活动单元格。

要确保水平或垂直滚动条位于要显示特定数据的行和列索引位置，请使用 [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) 和 [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn) 属性。

以下示例显示了如何激活工作表并将其中一个单元格设为活动单元格。在生成的输出中，滚动条将滚动以使第二行和第二列成为它们的第一个可见行和列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **高级主题**
- [复制和移动工作表](/cells/zh/net/copying-and-moving-worksheets/)
- [计算工作表中单元格的数量](/cells/zh/net/count-number-of-cells-in-the-worksheet/)
- [检测空工作表](/cells/zh/net/detecting-empty-worksheets/)
- [查找工作表是否为对话框工作表](/cells/zh/net/find-if-the-worksheet-is-dialog-sheet/)
- [获取工作表的唯一标识](/cells/zh/net/get-worksheet-unique-id/)
- [在工作表中创建、操作或移除场景](/cells/zh/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [管理分页](/cells/zh/net/managing-page-breaks/)
- [页面设置功能](/cells/zh/net/page-setup-features/)
- [打印工作表的多个副本](/cells/zh/net/print-multiple-copies-of-a-worksheet/)
- [使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性](/cells/zh/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [工作表视图](/cells/zh/net/worksheet-views/)

