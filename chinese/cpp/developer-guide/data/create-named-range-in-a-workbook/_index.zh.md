---
title: 在工作簿中创建命名范围
type: docs
weight: 60
url: /zh/cpp/create-named-range-in-a-workbook/
---

## **可能的使用场景**
Aspose.Cells支持创建命名范围。创建命名范围的方式有很多种。其中一种最简单的方式是首先创建 [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) 对象，然后使用 [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) 方法设置其名称。您可以通过微软Excel的 *名称管理器* 接口在您的Excel文件中查看所有的命名范围。
## **在工作簿中创建命名范围**
以下示例代码解释了如何通过Aspose.Cells创建一个 *命名范围*。一旦创建了 *命名范围*，它就会出现在 [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) 集合中。请参考代码生成的 [输出Excel文件](23167006.xlsx)。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **控制台输出**
以下控制台输出打印了上述代码中创建的 *命名范围* 的 [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) 和 [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) 方法的值。

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
