---
title: 管理工作表
linktitle: 工作表
type: docs
weight: 60
url: /zh/java/manage-worksheets/
---

{{% alert color="primary" %}}

开发人员可以利用Aspose.Cells灵活的API在其Excel文件中以编程方式轻松创建和管理工作表。在本主题中，我们将讨论一些在Excel文件中添加和删除工作表的方法。

{{% /alert %}}

使用Aspose.Cells管理工作表易如反掌。在本节中，我们将描述如何:

1. 从头开始创建新的Excel文件并向其添加工作表
1. 向设计电子表格添加工作表
1. 使用工作表名称访问工作表
1. 使用工作表名称从Excel文件中移除工作表
1. 使用工作表索引从Excel文件中移除工作表

Aspose.Cells提供了一个表示Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。让我们看看如何使用这些基本API集。

## **向新的Excel文件添加工作表**

要以编程方式创建新的Excel文件，开发人员需要创建一个表示Excel文件的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类的对象。然后开发人员可以调用[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add()方法。当我们调用[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)方法时，会自动向Excel文件添加一个空的工作表，可以通过将新添加的工作表的索引传递给[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add()来引用。获得工作表引用后，开发人员可以根据自己的需要在工作表上进行操作。在完成工作表上的工作后，开发人员可以通过调用[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)方法将带有新工作表的新创建的Excel文件保存在[**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)类中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **向设计电子表格添加工作表**

将工作表添加到设计电子表格的过程与上述方法完全相同，只是Excel文件已经创建，我们需要在向其添加工作表之前首先打开该Excel文件。可以通过在初始化[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类时传递文件路径或流来打开设计电子表格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **使用工作表名称访问工作表**

开发人员可以通过指定工作表名称或索引来访问或获取任何工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **使用工作表名称移除工作表**

有时，开发人员可能需要从现有的 Excel 文件中移除工作表，这个任务可以通过调用 [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) 方法的 [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 集合来完成。我们可以将工作表名称传递给 [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) 方法来移除特定的工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **通过页索引删除工作表**

如果开发人员已经知道要删除的工作表的工作表名称，则上述移除工作表的方法效果良好。但是，如果您不知道要从 Excel 文件中删除的工作表的工作表名称，该怎么办呢？

在这种情况下，开发人员可以使用重载版本的 [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)) 方法，该方法接受工作表的索引而不是工作表名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **高级主题**
- [激活工作表和激活工作表中的单元格](/cells/zh/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [复制和移动工作表在工作簿内及工作簿之间](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets/)
- [计算工作表中单元格的数量](/cells/zh/java/count-number-of-cells-in-the-worksheet/)
- [检测空工作表](/cells/zh/java/detecting-empty-worksheets/)
- [查找工作表是否为对话框工作表](/cells/zh/java/find-if-the-worksheet-is-dialog-sheet/)
- [获取工作表的唯一标识](/cells/zh/java/get-worksheet-unique-id/)
- [在Excel中插入背景图片](/cells/zh/java/insert-background-image-to-excel/)
- [在工作表中创建、操作或移除场景](/cells/zh/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [管理分页](/cells/zh/java/managing-page-breaks/)
- [页面设置功能](/cells/zh/java/page-setup-features/)
- [删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性](/cells/zh/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [在ODS文件中处理背景](/cells/zh/java/working-with-background-in-ods-files/)
- [工作表视图](/cells/zh/java/worksheet-views/)
