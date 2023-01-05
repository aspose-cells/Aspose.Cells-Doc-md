---
title: 管理工作表
type: docs
weight: 20
url: /zh/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

开发人员可以使用 Aspose.Cells 灵活 API 以编程方式轻松地在 Microsoft Excel 文件中创建和管理工作表。本主题介绍在 Microsoft Excel 文件中添加和删除工作表的方法。

{{% /alert %}} 

 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示一个 Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了多种管理工作表的方法。
## **将工作表添加到新的 Excel 文件**
要以编程方式创建新的 Excel 文件：

1. 创建对象的[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。
1. 打电话给[添加](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55)的方法[IWorksheet 集合](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)收藏。一个空工作表会自动添加到 Excel 文件中。可以通过将新工作表的工作表索引传递给[IWorksheet 集合](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)收藏。
1. 获取工作表参考。
1. 在工作表上执行工作。
1. 通过调用[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)班级[救球](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **使用工作表索引访问工作表**
以下示例代码显示如何通过指定其索引来访问或获取任何工作表。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **使用工作表索引删除工作表**
当工作表的名称已知时，按名称删除工作表效果很好。如果您不知道工作表的名称，请使用[移除位置](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)采用工作表的工作表索引而不是其工作表名称的方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
