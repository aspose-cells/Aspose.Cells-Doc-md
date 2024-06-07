---
title: 管理工作表
type: docs
weight: 20
url: /zh/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

开发人员可以使用Aspose.Cells灵活的API在Microsoft Excel文件中以编程方式轻松创建和管理工作表。本主题描述了在Microsoft Excel文件中添加和删除工作表的方法。

{{% /alert %}} 

Aspose.Cells提供了一个表示Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了广泛的方法来管理工作表。
## **向新的Excel文件中添加工作表**
要以编程方式创建新的Excel文件：

1. 创建[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的对象。
1. 调用[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合的[Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/)方法。一个空的工作表将自动添加到Excel文件中。可以通过将新工作表的索引传递给[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合来引用它。
1. 获取工作表引用。
1. 对工作表执行操作。
1. 通过调用[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法将带有新工作表的新Excel文件保存。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **按工作表索引访问工作表**
以下示例代码显示了如何通过指定其索引访问或获取任何工作表。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **使用工作表索引删除工作表**
当知道工作表的名称时，通过名称删除工作表效果很好。如果您不知道工作表的名称，可以使用[RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)方法的重载版本，该版本使用工作表的索引而不是名称。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
