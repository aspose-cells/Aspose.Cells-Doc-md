---
title: 操作工作簿中的命名范围
type: docs
weight: 90
url: /zh/cpp/manipulate-named-range-in-a-workbook/
---
##  **可能的使用场景**
Aspose.Cells 支持对现有命名范围的操作。所有现有的命名范围都可以从[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/)收藏。一旦访问命名范围，您就可以更改其各种方法，例如[获取全文](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[获取参考](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **操作工作簿中的命名范围**
以下示例代码读取第一个命名范围[源 Excel 文件](23167008.xlsx)并打印它的[全文](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[指的是](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)控制台上的属性。之后，它修改 `RefersTo` 属性并保存[输出Excel文件](23167009.xlsx).
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **控制台输出**
以下控制台输出打印以下值[全文](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[指的是](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)现有成员*命名范围*在上面的代码中。

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
