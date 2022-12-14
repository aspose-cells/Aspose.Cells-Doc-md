---
title: 管理工作表
linktitle: 工作表
type: docs
weight: 60
url: /zh/java/manage-worksheets/
---
{{% alert color="primary" %}}

开发人员可以使用 Aspose.Cells 的灵活 API 以编程方式轻松地在其 Excel 文件中创建和管理工作表。在本主题中，我们将讨论在 Excel 文件中添加和删除工作表的一些方法。

{{% /alert %}}

使用 Aspose.Cells 管理工作表就像 ABC 一样简单。在本节中，我们将描述我们如何：

1. 从头开始创建一个新的 Excel 文件并向其中添加一个工作表
1. 将工作表添加到设计器电子表格
1. 使用工作表名称访问工作表
1. 使用工作表名称从 Excel 文件中删除工作表
1. 使用工作表索引从 Excel 文件中删除工作表

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示一个 Excel 文件。[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。让我们看看如何使用这些基本的 API 集。

## **将工作表添加到新的 Excel 文件**

要以编程方式创建新的 Excel 文件，开发人员需要创建一个对象[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Excel 文件的类。然后开发者可以调用[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() 的方法[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).当我们打电话[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add())方法，会自动在Excel文件中添加一个空工作表，可以通过将新添加的工作表的工作表索引传递给[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).获得工作表引用后，开发人员可以根据自己的需求对工作表进行处理。在工作表上完成工作后，开发人员可以通过调用[**节省**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) 的方法[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)班级。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **将工作表添加到 Designer 电子表格**

将工作表添加到设计器电子表格的过程与上述方法完全相同，只是 Excel 文件已经创建，我们需要先打开该 Excel 文件，然后再向其添加工作表。可以通过在初始化时传递文件路径或流来打开设计器电子表格[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)班级。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **使用工作表名称访问工作表**

开发人员可以通过指定其名称或索引来访问或获取任何工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **使用工作表名称删除工作表**

有时，开发人员可能需要从现有 Excel 文件中删除工作表，可以通过调用[**移除点**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) 的方法[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)收藏。我们可以将工作表名称传递给[**移除点**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)方法删除特定工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **使用工作表索引删除工作表**

如果开发人员已经知道要删除的工作表的工作表名称，则上述删除工作表的方法很有效。但是，如果您不知道要从 Excel 文件中删除的工作表的工作表名称怎么办？

那么，在这种情况下，开发人员可以使用重载版本[**移除点**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)方法，它采用工作表的工作表索引而不是其工作表名称。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **推进主题**
- [激活工作表并在工作表中激活 Cell](/cells/zh/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [在工作簿内和工作簿之间复制和移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets/)
- [计算工作表中的单元格数](/cells/zh/java/count-number-of-cells-in-the-worksheet/)
- [检测空工作表](/cells/zh/java/detecting-empty-worksheets/)
- [查找工作表是否为对话框表](/cells/zh/java/find-if-the-worksheet-is-dialog-sheet/)
- [获取工作表唯一ID](/cells/zh/java/get-worksheet-unique-id/)
- [将背景图像插入 Excel](/cells/zh/java/insert-background-image-to-excel/)
- [从工作表中创建、操作或删除场景](/cells/zh/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [管理分页符](/cells/zh/java/managing-page-breaks/)
- [页面设置功能](/cells/zh/java/page-setup-features/)
- [更新其他工作表中的引用，同时删除工作表中的空白列和行](/cells/zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性](/cells/zh/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [在 ODS 文件中使用背景](/cells/zh/java/working-with-background-in-ods-files/)
- [工作表视图](/cells/zh/java/worksheet-views/)
