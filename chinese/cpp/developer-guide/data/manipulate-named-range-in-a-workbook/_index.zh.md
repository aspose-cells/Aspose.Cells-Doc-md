---
title: 在工作簿中操作命名范围
type: docs
weight: 90
url: /zh/cpp/manipulate-named-range-in-a-workbook/
---

## **可能的使用场景**
Aspose.Cells支持对现有命名范围进行操作。可以从[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/)集合中访问所有现有的命名范围。一旦访问了命名范围，就可以更改它的各种方法，例如[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)。
## **在工作簿中操作命名范围**
以下示例代码读取了[源Excel文件](23167008.xlsx)中的第一个命名范围，并在控制台上打印了它的[FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)属性。之后，修改了`RefersTo`属性并保存了[输出Excel文件](23167009.xlsx)。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **控制台输出**
以下控制台输出打印了上述代码中现有*命名范围*的[FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)成员的值。

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
