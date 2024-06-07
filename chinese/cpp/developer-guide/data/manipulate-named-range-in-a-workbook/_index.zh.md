---
title: 在工作簿中操作命名范围
type: docs
weight: 90
url: /zh/cpp/manipulate-named-range-in-a-workbook/
---

## **可能的使用场景**
Aspose.Cells支持操作现有的命名范围。所有现有的命名范围可以从Workbook.GetWorksheets().GetNames()集合中访问。一旦访问了命名范围，您可以更改其各种方法，例如GetFullText和GetRefersTo。
## **在工作簿中操作命名范围**
以下示例代码读取源excel文件中的第一个命名范围，并在控制台上打印其FullText和RefersTo属性。之后，修改RefersTo属性并保存输出excel文件。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **控制台输出**
以下控制台输出打印了上述代码中现有*命名范围*的FullText和RefersTo成员的值。

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
