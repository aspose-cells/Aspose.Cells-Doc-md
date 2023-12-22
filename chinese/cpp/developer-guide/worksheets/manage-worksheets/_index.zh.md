---
title: 管理工作表
type: docs
weight: 20
url: /zh/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

开发人员可以使用 Aspose.Cells 灵活 API 以编程方式轻松创建和管理 Microsoft Excel 文件中的工作表。本主题介绍在 Microsoft Excel 文件中添加和删除工作表的方法。

{{% /alert %}} 

 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表一个 Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种管理工作表的方法。
##  **将工作表添加到新的 Excel 文件**
要以编程方式创建新的 Excel 文件：

1. 创建一个对象[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。
1. 致电[添加](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/)的方法[工作表集合](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)收藏。空工作表会自动添加到 Excel 文件中。可以通过将新工作表的工作表索引传递给[工作表集合](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)收藏。
1. 获取工作表参考。
1. 在工作表上执行工作。
1. 通过调用以下命令保存带有新工作表的新 Excel 文件[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)班级[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **使用工作表索引访问工作表**
以下示例代码演示如何通过指定索引来访问或获取任何工作表。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **使用工作表索引删除工作表**
当工作表的名称已知时，按名称删除工作表效果很好。如果您不知道工作表的名称，请使用该工作表的重载版本[删除于](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)方法，采用工作表的工作表索引而不是其工作表名称。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
