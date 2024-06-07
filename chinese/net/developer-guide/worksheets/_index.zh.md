---
title: 管理Microsoft Excel文件的工作表
linktitle: 工作表
type: docs
weight: 90
url: /zh/net/manage-worksheets/
description: 使用Aspose.Cells添加工作表，删除工作表和活动工作表。
---


{{% alert color="primary" %}}

开发人员可以利用Aspose.Cells灵活的API来通过编程方式轻松创建和管理Microsoft Excel文件中的工作表。本主题描述了在Microsoft Excel文件中添加和删除工作表的方法。

{{% /alert %}}

Aspose.Cells提供了一个代表Excel文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一系列属性和方法来管理工作表。

## **向新的Excel文件中添加工作表**

要以编程方式创建新的Excel文件：

1. 创建一个[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的对象。
1. 调用[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)类的[**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add)方法。一个空的工作表将自动添加到Excel文件中。可以通过将新工作表的索引传递给[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合来引用它。
1. 获取工作表引用。
1. 对工作表执行操作。
1. 调用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)方法保存包含新工作表的新Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **向设计者电子表格添加工作表**

向设计者电子表格添加工作表的过程与添加新工作表的过程相同，只是Excel文件已经存在，所以需要在添加工作表之前打开文件。设计者电子表格可以通过[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类打开。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **使用工作表名称访问工作表**

通过指定名称或索引访问任意工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **使用表名删除工作表**

要从文件中删除工作表，调用[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)类的[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index)方法。将工作表名称传递给[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)方法以删除特定工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **使用工作表索引删除工作表**

当已知工作表名称时，通过名称删除工作表很有效。如果不知道工作表的名称，可以使用[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)方法的重载版本，它接受工作表索引而不是工作表名称。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **激活工作表并使工作表中的单元格为活动单元格**

有时，需要具体的工作表在用户在Excel中打开文件时是活动的并显示。同样，可能需要激活特定单元格并设置滚动条以显示活动单元格。
Aspose.Cells能够执行所有这些任务。

**活动工作表**是您正在操作的工作表：标签上的活动工作表名称默认为粗体。

**活动单元格**是选定的单元格，开始输入数据时将数据输入的单元格。一次只能激活一个单元格。活动单元格由粗边框突出显示。

### **激活工作表并使单元格为活动状态**

Aspose.Cells提供了激活工作表和单元格的特定API调用。例如，[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)属性对于设置工作簿中的活动工作表很有用。
同样，[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)属性用于设置和获取工作表中的活动单元格。

要确保水平或垂直滚动条处于要显示特定数据的行和列索引位置，请使用[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow)和[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)属性。

以下示例显示了如何激活工作表并使其内的单元格为活动单元格。生成的输出中，滚动条将滚动以使第2行和第2列作为第一个可见的行和列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **高级主题**
- [复制和移动工作表](/cells/zh/net/copying-and-moving-worksheets/)
- [计算工作表中的单元格数](/cells/zh/net/count-number-of-cells-in-the-worksheet/)
- [检测空白工作表](/cells/zh/net/detecting-empty-worksheets/)
- [查找工作表是否为对话框工作表](/cells/zh/net/find-if-the-worksheet-is-dialog-sheet/)
- [获取工作表唯一标识符](/cells/zh/net/get-worksheet-unique-id/)
- [在工作表中创建、操作或移除场景](/cells/zh/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [管理分页符](/cells/zh/net/managing-page-breaks/)
- [页面设置功能](/cells/zh/net/page-setup-features/)
- [打印工作表的多份副本](/cells/zh/net/print-multiple-copies-of-a-worksheet/)
- [利用Aspose.Cells使用OpenXml的Sheet.SheetId属性](/cells/zh/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [工作表视图](/cells/zh/net/worksheet-views/)

