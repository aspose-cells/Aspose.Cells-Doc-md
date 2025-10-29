---
title: 管理工作表
type: docs
weight: 20
url: /zh/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

开发人员可以利用Aspose.Cells灵活的API在Microsoft Excel文件中以程序方式轻松创建和管理工作表。本主题描述了在Microsoft Excel文件中添加和移除工作表的方法。

{{% /alert %}} 

Aspose.Cells提供了一个[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类，表示一个Excel文件。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

一个工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一系列方法来管理工作表。
## **向新的Excel文件添加工作表**
要通过程序创建新的Excel文件:

1. 创建 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的对象。
1. 调用 [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合的 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) 方法。空工作表会自动添加到Excel文件. 可以通过向 [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合传递新工作表的页索引来引用它。
1. 获取工作表引用。
1. 对工作表进行操作。
1. 调用 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的 [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法保存新的带有工作表的Excel文件。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **通过页索引访问工作表**
以下示例代码展示了如何通过指定索引访问或获取任何工作表。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **通过页索引删除工作表**
当已知工作表的名称时，通过名称来删除工作表是有效的。 如果不知道工作表的名称，可使用 [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) 方法的重载版本，该方法将工作表的页索引传递给它而不是工作表的名称。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
