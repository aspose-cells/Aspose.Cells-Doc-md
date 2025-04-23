---
title: 管理工作表
type: docs
weight: 20
url: /zh/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

开发人员可以利用Aspose.Cells灵活的API在Microsoft Excel文件中以程序方式轻松创建和管理工作表。本主题描述了在Microsoft Excel文件中添加和移除工作表的方法。

{{% /alert %}}

Aspose.Cells 提供了 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类，代表一个Excel文件。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类包含 [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) 集合，可访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类表示。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类提供了管理工作表的各种方法。

## **向新的Excel文件添加工作表**

要通过程序创建新的Excel文件:

1. 创建一个 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类的对象。
1. 调用 [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) 集合的 [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) 方法。一个空工作表会自动添加到Excel文件中，可以通过传递新工作表的索引来引用它。
1. 获取工作表引用。
1. 对工作表进行操作。
1. 调用 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类的 [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) 方法，保存包含新工作表的Excel文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **通过页索引访问工作表**

以下示例代码展示了如何通过指定索引访问或获取任何工作表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **通过页索引删除工作表**

当已知工作表名称时，删除工作表效果良好。如果不知道工作表的名称，可以使用 [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) 方法的重载版本，该版本接受工作表的索引而非名字。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
