---
title: 在工作簿中创建命名范围
type: docs
weight: 60
url: /zh/cpp/create-named-range-in-a-workbook/
---
##  **可能的使用场景**
Aspose.Cells 支持创建命名范围。创建命名范围有多种方法。最简单的方法之一是首先创建[范围](https://reference.aspose.com/cells/cpp/aspose.cells/range)对象，然后使用设置其名称[范围.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname)方法。您可以通过 Microsoft Excel 查看 Excel 文件中的所有命名范围*姓名经理*界面。
##  **在工作簿中创建命名范围**
以下示例代码说明了如何创建*命名范围*通过Aspose.Cells。有一次，*命名范围*创建后，它在内部可见[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames)收藏。请参阅[输出Excel文件](23167006.xlsx)代码生成，供参考。
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **控制台输出**
以下控制台输出打印以下值[获取全文](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)和[获取参考](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/)所创建的方法*命名范围*在上面的代码中。

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
