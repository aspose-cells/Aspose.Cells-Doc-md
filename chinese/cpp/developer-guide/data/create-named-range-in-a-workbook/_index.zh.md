---
title: 在工作簿中创建命名范围
type: docs
weight: 60
url: /zh/cpp/create-named-range-in-a-workbook/
---
## **可能的使用场景**
Aspose.Cells 支持命名范围的创建。有多种方法可以创建命名范围。最简单的方法之一是首先创建[范围](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range)对象，然后使用设置其名称[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb)方法。您可以通过 Microsoft Excel 查看 excel 文件中的所有命名范围*名称管理器*界面。
## **在工作簿中创建命名范围**
下面的示例代码解释了如何创建一个*命名范围*通过 Aspose.Cells。曾经，*命名范围*被创建，它在里面是可见的[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa)收藏。请参阅[输出excel文件](23167006.xlsx)生成的代码供参考。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **控制台输出**
以下控制台输出打印值[获取全文](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)和 `GetRefersTo` 创建的方法*命名范围*在上面的代码中。

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
