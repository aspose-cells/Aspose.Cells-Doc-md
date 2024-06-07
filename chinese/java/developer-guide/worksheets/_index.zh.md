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

使用Aspose.Cells管理工作表像ABC一样简单。 在本部分中，我们将描述我们如何：

1. 从头开始创建一个新的Excel文件并向其中添加一个工作表
1. 将工作表添加到设计师电子表格中
1. 使用工作表名称访问工作表
1. 使用工作表名称从Excel文件中删除工作表
1. 使用工作表索引从Excel文件中删除工作表

Aspose.Cells提供一个代表Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了一系列属性和方法来管理工作表。 让我们看看如何使用这些基本API。

## **向新的Excel文件中添加工作表**

要通过编程方式创建一个新的Excel文件，开发人员需要创建一个代表Excel文件的 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类对象。 然后开发人员可以调用 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add()） [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 的方法。 当我们调用 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add()） 方法时，将自动向Excel文件中添加一个空白工作表，可以通过将新添加的工作表的工作表索引传递给 [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 来引用。 获得工作表引用后，开发人员可以根据需求处理工作表。 在工作表上的工作完成后，开发人员可以通过调用 [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)） [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的方法将其保存为具有新工作表的新创建的Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **向设计者电子表格添加工作表**

向设计师电子表格中添加工作表的过程与上述方法完全相同，只是Excel文件已经创建，并且我们需要首先打开该Excel文件才能向其添加工作表。 可以通过在初始化 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类时传递文件路径或流来打开设计师电子表格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **使用工作表名称访问工作表**

开发人员可以通过指定名称或索引来访问或获取任何工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **使用表名删除工作表**

有时，开发人员可能需要从现有的Excel文件中删除工作表，这项任务可以通过调用 [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)） [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) 集合的方法来完成。 我们可以将工作表名称传递给 [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)） 方法以移除特定工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **使用工作表索引删除工作表**

上述删除工作表的方法对于已经知道要删除的工作表的工作表名的开发人员很有效。 但是，如果您不知道要从Excel文件中删除的工作表的工作表名是什么怎么办？

好吧，在这种情况下，开发人员可以使用 [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)） 方法的重载版本，该重载版本以工作表索引而不是其工作表名来执行任务。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **高级主题**
- [激活工作表和激活工作表中的单元格](/cells/zh/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [在工作簿内部和工作簿之间复制和移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets/)
- [计算工作表中的单元格数](/cells/zh/java/count-number-of-cells-in-the-worksheet/)
- [检测空白工作表](/cells/zh/java/detecting-empty-worksheets/)
- [查找工作表是否为对话框工作表](/cells/zh/java/find-if-the-worksheet-is-dialog-sheet/)
- [获取工作表唯一标识符](/cells/zh/java/get-worksheet-unique-id/)
- [在Excel中插入背景图像](/cells/zh/java/insert-background-image-to-excel/)
- [在工作表中创建、操作或移除场景](/cells/zh/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [管理分页符](/cells/zh/java/managing-page-breaks/)
- [页面设置功能](/cells/zh/java/page-setup-features/)
- [在删除工作表中的空白列和行时更新其他工作表中的引用](/cells/zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [利用Aspose.Cells使用OpenXml的Sheet.SheetId属性](/cells/zh/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [处理ODS文件中的背景](/cells/zh/java/working-with-background-in-ods-files/)
- [工作表视图](/cells/zh/java/worksheet-views/)
