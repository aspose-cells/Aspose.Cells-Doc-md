---
title: 操作工作簿中的命名范围
type: docs
weight: 90
url: /zh/cpp/manipulate-named-range-in-a-workbook/
---
## **可能的使用场景**
Aspose.Cells 支持对现有命名范围的操作。可以从访问所有现有的命名范围[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa)收藏。一旦访问命名范围，就可以更改其各种方法，例如[获取全文](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)和[获取引用](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **操作工作簿中的命名范围**
以下示例代码读取[源文件](23167008.xlsx)并打印其[全文](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)和[指的是](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36)控制台上的属性。之后，它修改 `RefersTo` 属性并保存[输出excel文件](23167009.xlsx).
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **控制台输出**
以下控制台输出打印值[全文](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)和[指的是](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36)现有成员*命名范围*在上面的代码中。

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
